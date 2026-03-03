from flask import Flask, jsonify, send_from_directory, send_file, request
import datetime
import logging
import os
import time

app = Flask(__name__, static_folder="frontend")

# --- CONFIGURATION ---
LOG_FILE = "security.log"
# Rate Limiter: { "ip": [timestamps] }
request_history = {}
LIMIT_WINDOW = 5  # seconds
MAX_REQUESTS = 3  # allowed per window

# Ensure log file exists on startup
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write(f"--- LOGISAFE AUDIT TRAIL INITIALIZED: {datetime.datetime.now()} ---\n")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "logisafe",
        "timestamp": str(datetime.datetime.now())
    })

@app.route("/simulate")
def simulate():
    user_ip = request.remote_addr
    now = time.time()
    
    # --- RATE LIMITER LOGIC ---
    if user_ip not in request_history:
        request_history[user_ip] = []
        
    # Remove timestamps outside the 5-second window
    request_history[user_ip] = [t for t in request_history[user_ip] if now - t < LIMIT_WINDOW]
    
    # Check if threshold is exceeded
    if len(request_history[user_ip]) >= MAX_REQUESTS:
        incident_msg = f"DDoS Simulation Triggered: Rate Limit Exceeded by {user_ip}"
        logging.critical(f"SECURITY ALERT: {incident_msg}")
        return jsonify({
            "incident": incident_msg,
            "severity": "CRITICAL",
            "action": "THROTTLED"
        }), 429 

    # Normal Simulation
    request_history[user_ip].append(now)
    incident_msg = "Unauthorized access attempt detected"
    logging.warning(f"SECURITY ALERT: {incident_msg}")
    
    return jsonify({
        "incident": incident_msg,
        "severity": "HIGH",
        "action": "LOGGED"
    })

@app.route("/clear-logs", methods=["POST"])
def clear_logs():
    try:
        with open(LOG_FILE, "w") as f:
            f.write(f"--- LOGISAFE AUDIT TRAIL PURGED: {datetime.datetime.now()} ---\n")
        return jsonify({"status": "success", "message": "Audit trail wiped."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route("/download-logs")
def download_logs():
    try:
        return send_file(LOG_FILE, as_attachment=True)
    except Exception as e:
        return jsonify({"status": "error", "message": "Log file error."}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)