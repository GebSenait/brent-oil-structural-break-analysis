import React from 'react';

export default function EventsTable({ events }) {
  if (!events?.length) {
    return <p className="muted">No events to display.</p>;
  }

  return (
    <div className="table-wrap">
      <table className="events-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Category</th>
            <th>Event</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {events.map((ev) => (
            <tr key={ev.event_id || ev.short_name}>
              <td>{ev.trading_date || ev.date}</td>
              <td><span className={`category category-${(ev.category || '').replace('_', '-')}`}>{ev.category}</span></td>
              <td>{ev.short_name}</td>
              <td className="desc">{ev.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
