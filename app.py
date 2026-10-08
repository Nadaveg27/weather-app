"""Minimal Flask weather app with hardcoded data (no external API calls)."""

import socket

from flask import Flask, jsonify

app = Flask(__name__)

WEATHER_DATA = {
    "London": {"temperature_c": 15, "condition": "Cloudy"},
    "Tokyo": {"temperature_c": 22, "condition": "Sunny"},
    "Cairo": {"temperature_c": 30, "condition": "Clear"},
}


@app.route("/")
def index():
    """Return the hardcoded weather data along with the hostname that served it."""
    response = {
        "weather": WEATHER_DATA,
        "served_by": socket.gethostname(),
    }
    return jsonify(response)


@app.route("/health")
def health():
    """Simple health check endpoint."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
