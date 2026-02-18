# Task-3: Interactive Dashboard

**Objective:** Expose Task-2 change point results and Task-1 event context through a Flask API and a React frontend so that stakeholders can explore regime shifts, filter events by category, and view decision-ready summaries without running notebooks or code.

---

## 1. Objective

- Provide **REST APIs** for returns, prices, events (with optional category filter), and the change point posterior summary.
- Build an **interactive React dashboard** that visualizes returns and price levels, highlights the posterior break date, and lists/filters events.
- Ensure **responsive layout** and **clear, probabilistic narratives** (no causal claims).

---

## 2. System Architecture (Flask + React)

- **Backend:** Flask app in `backend/` (Python). Serves JSON from `data/processed/` and `data/events/`. CORS enabled for local frontend.
- **Frontend:** React (Vite) in `frontend/`. Uses Recharts for time series; fetches from backend via proxy in dev (`/api` → `http://localhost:5000`).
- **Data flow:** Task-1 → processed CSVs. Task-2 notebook → `change_point_posterior.json`. Backend reads these; frontend calls `/api/*`.

---

## 3. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check; returns `{ "status": "ok" }`. |
| GET | `/api/returns` | Brent daily returns: `{ "data": [ { "Date", "value" } ], "count": N }`. |
| GET | `/api/prices` | Brent price levels: same shape. |
| GET | `/api/events` | Events (aligned if available). Query: `?category=geopolitical\|economic\|opec_policy`. |
| GET | `/api/change-point` | Change point posterior summary (from Task-2 export). 404 if `change_point_posterior.json` missing. |

---

## 4. Frontend Components

- **Dashboard** (`pages/Dashboard.jsx`): Loads all API data; passes to chart and table.
- **ReturnsChart** (`components/ReturnsChart.jsx`): Line chart of returns or prices; optional vertical reference line at break date.
- **ChangePointSummary** (`components/ChangePointSummary.jsx`): Cards for break date, regime means/volatilities, impact (Δμ, volatility ratio).
- **EventsTable** (`components/EventsTable.jsx`): Sortable list of events; category filter in Dashboard.

---

## 5. Dashboard Features

- View **Brent returns** and **price level** time series with posterior break date highlighted.
- View **change point summary**: break date (median + 95% CI), before/after μ and σ, impact metrics.
- **Filter events** by category (geopolitical, economic, OPEC policy).
- Responsive layout; dark theme for readability.

---

## 6. Screenshots

*(Placeholder: add screenshots of the dashboard and event filter after running the app.)*

---

## 7. Setup & Execution Instructions

### React dashboard execution plan (copy-paste)

**Prerequisites:** Node.js and npm installed. Verify in **Windows Command Prompt** or **PowerShell**: `node --version` and `npm --version`.  
**Cursor terminal:** The repo’s `.vscode/settings.json` adds the default Node paths to the integrated terminal on Windows — **open a new terminal** in Cursor and `npm` should work. If Node is in a custom location (nvm, fnm), set **NODE_HOME** to that folder. If npm is still not found, restart Cursor or run the frontend from system CMD/PowerShell.

**Two terminals required:**

| Step | Terminal | Command | Notes |
|------|----------|---------|--------|
| 1 | **Terminal 1** (Cursor or CMD) | `cd "d:\Senait Doc\KAIM 8 Doc\brent-oil-structural-break-analysis"` then activate venv (e.g. `.\.venv\Scripts\Activate.ps1`) then `python -m backend.app` | Leave running. Backend on http://localhost:5000 |
| 2 | **Terminal 2** (CMD where `npm` works) | See **Frontend (CMD)** below | Leave running. Frontend on http://localhost:3000 |
| 3 | Browser | Open **http://localhost:3000** | Dashboard loads; it talks to backend on port 5000 |

**Frontend (CMD) – project on a different drive (e.g. D:) than current drive (e.g. C:):**  
In Windows CMD, `cd "d:\...\frontend"` does **not** switch the current drive, so `npm install` runs in the wrong folder and fails with "Could not read package.json". Use either:

- **Option 1 – `cd /d`** (change drive and directory):  
  `cd /d "d:\Senait Doc\KAIM 8 Doc\brent-oil-structural-break-analysis\frontend"`  
  then `npm install` then `npm run dev`

- **Option 2 – run helper script from project root:**  
  `cd /d "d:\Senait Doc\KAIM 8 Doc\brent-oil-structural-break-analysis"`  
  then `scripts\run_frontend.cmd`  
  (the script changes into `frontend` and runs `npm install` and `npm run dev`).

**Frontend (PowerShell):** Same drive or use `Set-Location "d:\...\frontend"`; then `npm install`; `npm run dev`.

**One-liners (when already in project root on the correct drive):**

- Terminal 1: `python -m backend.app`
- Terminal 2: `scripts\run_frontend.cmd` **or** `cd frontend` → `npm install` → `npm run dev`

---

1. **Backend (Flask)**  
   From project root, with venv activated and `requirements.txt` installed:
   ```bash
   python -m backend.app
   ```
   Or: `flask --app backend.app:app run --port 5000`  
   API base: `http://localhost:5000`.

2. **Frontend (React)**  
   From project root, in a **second** terminal where `node`/`npm` are available (system CMD/PowerShell or Cursor after restart):
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   Open `http://localhost:3000`. The dev server proxies `/api` to port 5000.

3. **Change point data**  
   Run `notebooks/task-2-change-point-analysis.ipynb` (Run All) to generate `data/processed/change_point_posterior.json`. Without it, `/api/change-point` returns 404 and the dashboard shows a message to run the notebook.

4. **Production build**  
   `cd frontend && npm run build`. Serve `frontend/dist` with a static server and point API requests to your deployed Flask backend.
