import React from 'react';

export default function ChangePointSummary({ data }) {
  if (!data) {
    return (
      <section className="dashboard-section summary-card">
        <h2>Change point (posterior)</h2>
        <p className="muted">
          Run the Task-2 notebook to generate <code>change_point_posterior.json</code> and reload.
        </p>
      </section>
    );
  }

  const cp = data.change_point || {};
  const before = data.regime_before || {};
  const after = data.regime_after || {};
  const impact = data.impact || {};

  return (
    <section className="dashboard-section summary-card">
      <h2>Change point (posterior summary)</h2>
      <div className="summary-grid">
        <div className="summary-block">
          <h3>Break date</h3>
          <p className="value">{cp.date_median || '—'}</p>
          <p className="muted small">95% CI: {cp.date_lo} to {cp.date_hi}</p>
        </div>
        <div className="summary-block">
          <h3>Regime before</h3>
          <p className="value">μ = {(before.mu_mean * 100).toFixed(4)}%</p>
          <p className="muted small">σ = {(before.sigma_mean * 100).toFixed(4)}%</p>
        </div>
        <div className="summary-block">
          <h3>Regime after</h3>
          <p className="value">μ = {(after.mu_mean * 100).toFixed(4)}%</p>
          <p className="muted small">σ = {(after.sigma_mean * 100).toFixed(4)}%</p>
        </div>
        <div className="summary-block">
          <h3>Impact</h3>
          <p className="value">Δμ = {(impact.delta_mu_mean * 100).toFixed(4)}%</p>
          <p className="muted small">Vol ratio σ₂/σ₁ = {impact.volatility_ratio_mean?.toFixed(3) ?? '—'}</p>
        </div>
      </div>
      <p className="disclaimer">
        Structural break is consistent with event timing where relevant; no causal claim is made.
      </p>
    </section>
  );
}
