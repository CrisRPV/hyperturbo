# Formula RPV HyperTurbo Control System

Build 1.0.0 - First Racing Factory Release

---

## Descrizione

Sistema di controllo HyperTurbo per Formula RPV con gestione canali CH1–CH10, backend configuratore, mappatura HID, sistema fail-safe e supporto future UI racing.

---

## Struttura

- install-rpv-hyperturbo.sh ➔ installatore principale
- backend/ ➔ gestione configurazioni e backend API
- frontend/ ➔ interfaccia utente (in sviluppo)
- mapping/ ➔ gestione mappature periferiche
- config/ ➔ impostazioni di sistema

---

## Avvio backend

```bash
cd backend
bash start-backend.sh
