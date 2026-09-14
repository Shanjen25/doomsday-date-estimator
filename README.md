# Doomsday Date Estimator

A simple tool to estimate the most probable timeframe for a global existential catastrophe from **nuclear war** or **natural disasters**, based on aggregated expert forecasts and historical data.

> **Disclaimer**: This is a probabilistic toy model for educational and discussion purposes only. It is **not** a prediction, forecast, or scientific claim. Existential risks are highly uncertain, and the future is not predetermined. Humanity has agency to reduce these risks.

## Key Assumptions (from public sources)

### Nuclear Risk
- Expert surveys (e.g., Forecasting Research Institute 2024): ~1–5% chance of nuclear catastrophe (killing ≥10 million) by 2045.
- Annualized estimates from various sources: roughly 0.25%–1% per year for significant nuclear use.
- Existential (near-extinction) risk from nuclear war this century: commonly estimated in the range of 0.01%–1% (see 80,000 Hours, Toby Ord’s *The Precipice*, etc.).

### Natural Catastrophe Risk
- Background rate of human extinction from natural causes (asteroids, supervolcanoes, etc.): upper bounds around 1 in 14,000 to 1 in 87,000 per year (Snyder-Beattie et al., 2019).
- Return periods for civilization-threatening events (e.g., large asteroid, VEI-8 supervolcano): typically 10,000–100,000+ years.
- Natural risks are currently much lower than anthropogenic ones in most expert assessments.

### Model Used
We use a simple constant annual probability model:
- Annual probability of catastrophe `p`
- Expected waiting time = `1 / p` years
- Median waiting time = `ln(2) / p` years (the date by which there is a 50% cumulative chance)

The app lets you adjust `p` and see the resulting dates.

## How to Use

### Option 1: Python CLI
```bash
python estimator.py
```

### Option 2: Static Web Version
Open `index.html` in any browser (or serve it).

## Sources
- Forecasting Research Institute – Nuclear risk surveys
- Bulletin of the Atomic Scientists – Doomsday Clock
- Our World in Data – Nuclear weapons
- Snyder-Beattie et al. (2019) – Natural extinction rate bounds
- 80,000 Hours problem profiles
- Toby Ord, *The Precipice*

## License
MIT – feel free to fork, improve, or argue with the assumptions.
