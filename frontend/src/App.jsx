import React from 'react';
import Dashboard from './pages/Dashboard';

export default function App() {
  return (
    <div className="app" style={{ padding: '1rem 2rem', maxWidth: 1200, margin: '0 auto' }}>
      <header className="app-header">
        <h1>Brent Change Point Dashboard</h1>
        <p className="subtitle">Birhan Energies — Structural break analysis & event context</p>
      </header>
      <main>
        <Dashboard />
      </main>
    </div>
  );
}
