# Weather App

Minimal Flask app serving hardcoded weather data for 3 cities, load-balanced
behind nginx.

## Build

```bash
docker compose build
```

## Run

```bash
docker compose up
```

The app is available at http://localhost:8000. Reload a few times and watch
the `served_by` field change between `app1` and `app2`.

## Test

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
```

Stop with `docker compose down`.
