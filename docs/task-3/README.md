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

1. **Backend (Flask)**  
   From project root, with venv activated and `requirements.txt` installed:
   ```bash
   python -m backend.app
   ```
   Or: `flask --app backend.app:app run --port 5000`  
   API base: `http://localhost:5000`.

2. **Frontend (React)**  
   From project root:
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
