from flask import Flask, jsonify
import logging
import time
import random

app = Flask(__name__)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():
    logging.info("Home endpoint accessed")
    return jsonify({"message": "Welcome to LogiSafe v2"})

@app.route("/health")
def health():
    logging.info("Health check endpoint accessed")
    return jsonify({"status": "UP"})

@app.route("/simulate")
def simulate_error():
    value = random.choice([0, 1])
    if value == 0:
        logging.error("Simulated application error occurred")
        return jsonify({"error": "Something went wrong"}), 500
    else:
        logging.warning("Simulated warning triggered")
        return jsonify({"warning": "This is a warning"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
