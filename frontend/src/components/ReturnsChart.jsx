import React, { useMemo } from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  ReferenceLine,
} from 'recharts';

export default function ReturnsChart({ data, changePointDate, isPrice }) {
  const chartData = useMemo(() => {
    if (!Array.isArray(data)) return [];
    return data.map((d) => ({
      ...d,
      date: d.Date,
      value: typeof d.value === 'number' ? d.value : parseFloat(d.value),
    })).filter((d) => !Number.isNaN(d.value));
  }, [data]);

  if (!chartData.length) {
    return <p className="muted">No data available.</p>;
  }

  return (
    <div className="chart-container">
      <ResponsiveContainer width="100%" height={320}>
        <LineChart data={chartData} margin={{ top: 8, right: 8, left: 8, bottom: 8 }}>
          <XAxis
            dataKey="date"
            tick={{ fill: 'var(--muted)', fontSize: 11 }}
            tickFormatter={(v) => {
              const d = new Date(v);
              return d.getFullYear().toString();
            }}
          />
          <YAxis
            tick={{ fill: 'var(--muted)', fontSize: 11 }}
            tickFormatter={(v) => (isPrice ? v.toFixed(0) : v.toFixed(4))}
          />
          <Tooltip
            contentStyle={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
            labelStyle={{ color: 'var(--text)' }}
            formatter={([val]) => [isPrice ? Number(val).toFixed(2) : Number(val).toFixed(5), isPrice ? 'Price' : 'Return']}
            labelFormatter={(label) => label}
          />
          {changePointDate && (
            <ReferenceLine
              x={changePointDate}
              stroke="var(--danger)"
              strokeDasharray="4 4"
              strokeWidth={1.5}
            />
          )}
          <Line
            type="monotone"
            dataKey="value"
            stroke="var(--accent)"
            strokeWidth={1}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
