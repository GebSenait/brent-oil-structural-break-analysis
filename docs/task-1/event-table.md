# Event dataset — summary table (10–15 events)

Below is the curated list of events in `data/events/geopolitical_economic_opec_events.csv`. Schema and timing assumptions: `data/events/README.md` and `docs/task-1/event-assumptions.md`.

| event_id | date       | category     | short_name                    |
|----------|------------|--------------|-------------------------------|
| EVT_001  | 2003-03-20 | geopolitical | Iraq invasion                 |
| EVT_002  | 2008-09-15 | economic     | Lehman collapse               |
| EVT_003  | 2011-02-17 | geopolitical | Arab Spring / Libya           |
| EVT_004  | 2014-11-27 | opec_policy  | OPEC no cut Nov 2014          |
| EVT_005  | 2016-09-28 | opec_policy  | OPEC Algiers agreement        |
| EVT_006  | 2018-05-08 | geopolitical | US Iran sanctions             |
| EVT_007  | 2020-03-06 | opec_policy  | OPEC+ Vienna meeting Mar 2020 |
| EVT_008  | 2020-03-09 | economic     | COVID demand shock / price crash |
| EVT_009  | 2020-04-12 | opec_policy  | OPEC+ historic cut Apr 2020   |
| EVT_010  | 2021-11-04 | opec_policy  | OPEC+ gradual increase Nov 2021 |
| EVT_011  | 2022-02-24 | geopolitical | Russia-Ukraine invasion       |
| EVT_012  | 2022-10-05 | opec_policy  | OPEC+ cut Oct 2022            |
| EVT_013  | 2023-04-02 | opec_policy  | OPEC+ voluntary cuts Apr 2023 |
| EVT_014  | 2023-10-07 | geopolitical | Hamas-Israel conflict         |

**Total: 14 events** (geopolitical, economic, OPEC-related). Use `date` as reference; align to first trading day on or after when joining to price data.
