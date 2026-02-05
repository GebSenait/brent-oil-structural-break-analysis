# Event dataset: assumptions and timing

## Reference date rule

- **CSV `date`** = calendar date we assign to the event (announcement, start of conflict, or key decision day).
- **In analysis**: When joining to price data, we map this to the **first trading day on or after** that date (e.g. London/ICE or NYMEX business days). Weekends and holidays are thus handled consistently.

## Single-date representation

- Each event has one row and one reference date. For multi-day events (e.g. OPEC meeting 5–6 March), we pick one date (e.g. last day of meeting or day of press release) and document in `notes` if ambiguous.

## Categories

- **geopolitical**: Wars, sanctions, major political crises affecting oil-producing or transit regions.
- **economic**: Recessions, major policy (e.g. Fed), financial crises.
- **opec_policy**: OPEC/OPEC+ meetings and announced production cuts or increases.
- **supply_shock**: Disruptions to physical supply (e.g. hurricanes, attacks on infrastructure).
- **demand_shock**: Large demand-side shifts (e.g. COVID lockdowns).
- **other**: Events that do not fit above; use sparingly and explain in notes.

## Limitations

- **Timing**: News may leak before the “official” date; markets may react the day before or after. We do not model lead/lag explicitly in this dataset.
- **Attribution**: Coincidence in time does not imply causation; multiple events can cluster, and confounding is possible.
- **Coverage**: List is curated for interpretability, not exhaustive. Omitted events may also matter.

## Versioning

- When adding or changing events, update the CSV and document the change in git history or a CHANGELOG in `data/events/`.
