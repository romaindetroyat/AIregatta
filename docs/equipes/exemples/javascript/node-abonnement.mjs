#!/usr/bin/env node
// AI Regatta — exemple d'abonnement au flux équipes avec Node.js (mqtt.js 5).
//
// Installation :  npm install mqtt@5.10.1
// Lancement :     AIR_USER=equipe-fra07 AIR_PASSWORD='...' AIR_CA=./ca-ai-regatta.crt node node-abonnement.mjs
//
// Variables d'environnement :
//   AIR_URL       adresse du broker (défaut mqtts://10.20.0.10:8883 ; bac à sable : mqtts://bac-a-sable.[domaine à définir]:8883)
//   AIR_CA        certificat de l'autorité de l'organisation (facultatif : sinon certificats du système)
//   AIR_USER      compte, ex. equipe-fra07 (obligatoire)
//   AIR_PASSWORD  mot de passe (obligatoire)
//   AIR_BOAT      votre bateau (défaut FRA-07)
//
// Le script suit la course indiquée par race/current, tient l'état de la flotte et affiche chaque seconde
// le compte à rebours (calculé localement) et la liste des bateaux.

import mqtt from "mqtt";
import { readFileSync } from "node:fs";

const URL = process.env.AIR_URL ?? "mqtts://10.20.0.10:8883";
const USER = process.env.AIR_USER;
const PASSWORD = process.env.AIR_PASSWORD;
const MY_BOAT = process.env.AIR_BOAT ?? "FRA-07";
if (!USER || !PASSWORD) {
  console.error("AIR_USER et AIR_PASSWORD sont obligatoires.");
  process.exit(1);
}

const GPS_EPOCH_UNIX_MS = 315964800000;
const state = { raceId: null, clock: null, boats: new Map(), lastSeq: new Map(), gpsUtcOffsetS: 18 };

/** Heure GPS selon l'horloge locale (synchronisée par chrony sur 10.20.0.1). */
const nowGpsMs = () => Date.now() - GPS_EPOCH_UNIX_MS + 1000 * state.gpsUtcOffsetS;

/** Écarte doublons et messages en retard ; accepte un grand recul de seq (bascule de serveur). */
function accept(key, msg) {
  const last = state.lastSeq.get(key);
  if (last !== undefined && msg.seq <= last && msg.seq > last - 1000) return false;
  state.lastSeq.set(key, msg.seq);
  return true;
}

const client = mqtt.connect(URL, {
  username: USER,
  password: PASSWORD,
  clientId: `${USER}-node`,   // stable : permet de retrouver la session persistante
  clean: false,               // session persistante (§3.2 du contrat)
  protocolVersion: 4,         // MQTT 3.1.1
  keepalive: 10,
  reconnectPeriod: 2000,
  resubscribe: false,         // on se réabonne nous-mêmes à chaque connexion (§8.4)
  ca: process.env.AIR_CA ? readFileSync(process.env.AIR_CA) : undefined,
});

function followRace(raceId) {
  if (!raceId || raceId === state.raceId) return;
  if (state.raceId) client.unsubscribe(`race/${state.raceId}/#`);
  Object.assign(state, { raceId, clock: null });
  state.boats.clear();
  state.lastSeq.clear();
  client.subscribe(`race/${raceId}/#`, { qos: 1 });
  console.log(`[course] suivi de ${raceId}`);
}

client.on("connect", (connack) => {
  console.log(`[connexion] établie (session reprise : ${connack.sessionPresent})`);
  client.subscribe({ "race/current": { qos: 1 }, "sys/time": { qos: 0 } });
  if (state.raceId) client.subscribe(`race/${state.raceId}/#`, { qos: 1 });
});
client.on("reconnect", () => console.error("[connexion] reconnexion…"));
client.on("error", (err) => console.error(`[connexion] erreur : ${err.message}`));

client.on("message", (topic, payload) => {
  let msg;
  try {
    msg = JSON.parse(payload.toString("utf8"));
  } catch {
    return;
  }
  if (topic === "race/current") return followRace(msg.race_id);
  if (topic === "sys/time") {
    state.gpsUtcOffsetS = msg.gps_utc_offset_s;
    return;
  }
  const p = topic.split("/");
  if (p[0] !== "race" || p[1] !== state.raceId) return;
  if (p[2] === "boats" && p[4] === "pos") {
    if (accept(`pos/${p[3]}`, msg)) state.boats.set(p[3], msg);
  } else if (p[2] === "clock") {
    if (accept("clock", msg)) {
      state.clock = msg;
      state.gpsUtcOffsetS = msg.gps_utc_offset_s;
    }
  } else if (p[2] === "events") {
    console.log(`[événement] ${msg.type} (${msg.status}) : ${msg.text_fr}`);
  }
});

function fmt(ms) {
  const sign = ms < 0 ? "-" : "";
  ms = Math.abs(ms);
  return `${sign}${String(Math.floor(ms / 60000)).padStart(2, "0")}:${String(Math.floor(ms / 1000) % 60).padStart(2, "0")}`;
}

setInterval(() => {
  const now = nowGpsMs();
  const c = state.clock;
  let chrono = "chrono inconnu";
  if (c && c.start_t_gps_ms !== null && !["postponed", "general_recall", "abandoned"].includes(c.step)) {
    const remaining = c.start_t_gps_ms - now; // calcul local, jamais à l'arrivée du message
    chrono = remaining > 0 ? `départ dans ${fmt(remaining)}` : `course +${fmt(-remaining)}`;
  } else if (c) {
    chrono = `chrono : ${c.step}`;
  }
  const fleet = [...state.boats.values()]
    .sort((a, b) => a.boat_id.localeCompare(b.boat_id))
    .map((b) => `${b.boat_id === MY_BOAT ? "*" : ""}${b.boat_id} ${b.sog_kn?.toFixed(1) ?? "—"}nd${b.stale ? " PERDU" : ""}`)
    .join("  ");
  console.log(`${state.raceId ?? "—"} | ${chrono} | ${fleet}`);
}, 1000);

process.on("SIGINT", () => client.end(false, {}, () => process.exit(0)));
