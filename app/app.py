from flask import Flask, jsonify, send_from_directory, send_file
import datetime
import logging
import os

app = Flask(__name__, static_folder="frontend")

# Ensure the log file exists immediately on startup
if not os.path.exists("security.log"):
    with open("security.log", "w") as f:
        f.write(f"--- LOGISAFE AUDIT TRAIL INITIALIZED: {datetime.datetime.now()} ---\n")

# Configure logging to write to 'security.log'
logging.basicConfig(
    filename='security.log',
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

@app.route("/logs")
def logs():
    # Returns a quick snapshot of the latest system status
    return jsonify({
        "timestamp": str(datetime.datetime.now()),
        "level": "INFO",
        "message": "Sentinel Core Operational"
    })

@app.route("/simulate")
def simulate():
    incident_msg = "Unauthorized access attempt detected"
    # Write to the persistent security.log file
    logging.warning(f"SECURITY ALERT: {incident_msg}")
    
    return jsonify({
        "incident": incident_msg,
        "severity": "HIGH",
        "action": "LOGGED_TO_AUDIT_TRAIL"
    })

@app.route("/clear-logs", methods=["POST"])
def clear_logs():
    try:
        # Re-initialize the file as empty
        with open("security.log", "w") as f:
            f.write(f"--- LOGISAFE AUDIT TRAIL PURGED: {datetime.datetime.now()} ---\n")
        return jsonify({"status": "success", "message": "Audit trail wiped."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route("/download-logs")
def download_logs():
    try:
        if os.path.exists("security.log"):
            return send_file("security.log", as_attachment=True)
        return jsonify({"status": "error", "message": "Log file not found."}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # 0.0.0.0 is required for Docker to allow external access
    app.run(host="0.0.0.0", port=5001)