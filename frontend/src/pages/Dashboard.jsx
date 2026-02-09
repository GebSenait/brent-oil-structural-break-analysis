import React, { useState, useEffect } from 'react';
import ReturnsChart from '../components/ReturnsChart';
import ChangePointSummary from '../components/ChangePointSummary';
import EventsTable from '../components/EventsTable';

const API = '/api';

export default function Dashboard() {
  const [returns, setReturns] = useState([]);
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePoint, setChangePoint] = useState(null);
  const [eventCategory, setEventCategory] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    Promise.all([
      fetch(`${API}/returns`).then((r) => (r.ok ? r.json() : { data: [] })),
      fetch(`${API}/prices`).then((r) => (r.ok ? r.json() : { data: [] })),
      fetch(`${API}/events`).then((r) => (r.ok ? r.json() : { data: [] })),
      fetch(`${API}/change-point`).then((r) => (r.ok ? r.json() : null)),
    ])
      .then(([ret, pr, ev, cp]) => {
        if (cancelled) return;
        setReturns(ret.data || []);
        setPrices(pr.data || []);
        setEvents(ev.data || []);
        setChangePoint(cp);
      })
      .catch((err) => {
        if (!cancelled) setError(err.message || 'Failed to load data');
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => { cancelled = true; };
  }, []);

  useEffect(() => {
    if (!eventCategory) return;
    let cancelled = false;
    fetch(`${API}/events?category=${encodeURIComponent(eventCategory)}`)
      .then((r) => r.json())
      .then((res) => {
        if (!cancelled) setEvents(res.data || []);
      })
      .catch(() => {});
    return () => { cancelled = true; };
  }, [eventCategory]);

  if (loading) {
    return (
      <section className="dashboard-section">
        <p className="muted">Loading dashboard data…</p>
      </section>
    );
  }

  if (error) {
    return (
      <section className="dashboard-section">
        <p className="error">Error: {error}. Ensure the Flask backend is running on port 5000.</p>
      </section>
    );
  }

  return (
    <div className="dashboard">
      <ChangePointSummary data={changePoint} />
      <section className="dashboard-section chart-section">
        <h2>Brent daily returns</h2>
        <ReturnsChart data={returns} changePointDate={changePoint?.change_point?.date_median} />
      </section>
      <section className="dashboard-section chart-section">
        <h2>Brent price level</h2>
        <ReturnsChart data={prices} changePointDate={changePoint?.change_point?.date_median} isPrice />
      </section>
      <section className="dashboard-section">
        <h2>Events</h2>
        <div className="filter-row">
          <label htmlFor="category">Filter by category:</label>
          <select
            id="category"
            value={eventCategory}
            onChange={(e) => setEventCategory(e.target.value)}
          >
            <option value="">All</option>
            <option value="geopolitical">Geopolitical</option>
            <option value="economic">Economic</option>
            <option value="opec_policy">OPEC policy</option>
          </select>
        </div>
        <EventsTable events={events} />
      </section>
    </div>
  );
}
