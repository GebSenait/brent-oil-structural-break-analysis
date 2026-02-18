# Event dataset

Structured list of **major geopolitical, economic, and OPEC-related events** used to interpret change points in Brent oil prices.

## CSV schema

| Column | Type | Description |
|--------|------|-------------|
| `event_id` | string | Unique identifier (e.g. `EVT_001`). |
| `date` | ISO date (YYYY-MM-DD) | **Reference date** for the event (see assumptions below). |
| `category` | string | One of: `geopolitical`, `economic`, `opec_policy`, `supply_shock`, `demand_shock`, `other`. |
| `short_name` | string | Brief label for reports and plots. |
| `description` | string | One or two sentences; optional. |
| `notes` | string | Optional: timing caveats, source, or ambiguity. |

## Assumptions on event timing

- **Reference date**: The `date` in the CSV is the **calendar date** we associate with the event (e.g. announcement day, start of conflict). For trading-day alignment, we use the **first trading day on or after** this date when merging with price data.
- **Single date per event**: Each row is one event with one reference date. Multi-day events (e.g. a meeting spanning 2 days) are represented by one chosen date (e.g. first day or decision day); see `notes` if needed.
- **No causality claim**: Inclusion in this list does not imply that the event *caused* any observed price break; it supports narrative and alignment analysis only.
- **Curated, not exhaustive**: The list is deliberately limited to 10–15 events for clarity; it can be extended in future iterations with versioning.

See `docs/task-1/event-assumptions.md` for full assumptions and limitations.
