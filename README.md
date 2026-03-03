🛡️ LogiSafe Sentinel | Ultra
Containerized Security Operations Center (SOC) Simulator

LogiSafe Sentinel is a high-performance microservice designed to demonstrate real-world security monitoring, incident response, and resource protection. It features a Python Flask engine and a Real-time Vanilla JS dashboard, all orchestrated within a Docker environment.

🚀 Advanced Features
DDoS Mitigation (Rate Limiting): Implements a sliding-window algorithm to detect and throttle high-frequency request bursts.

Real-Time Heartbeat: Asynchronous polling of the /health endpoint to monitor engine stability and latency.

Persistent Audit Trail: State-of-the-art logging using Python's logging library, synchronized to the host machine via Docker Volumes.

Data Lifecycle Suite: Integrated tools for Incident Generation, Audit Exporting, and Cryptographic Purging (Log Sanitization).

SOC UI: A professional, SVG-enhanced dashboard supporting both Dark and Light modes for administrative flexibility.

🛠️ Technical Architecture
| **Layer**   | **Technology**           | **Function**                           |
| ----------- | ------------------------ | -------------------------------------- |
| Backend     | Python 3.10 / Flask      | RESTful Security Engine                |
| Frontend    | HTML5 / CSS3 / ES6+      | Real-time SOC Dashboard                |
| Security    | Sliding Window Algorithm | DDoS / Rate Limit Protection           |
| Persistence | Docker Volumes           | Host-to-Container Data Synchronization |
| DevOps      | Docker Compose           | Microservice Orchestration             |

🧪 Security Testing (QA)
Triggering a DDoS Alert
The system is configured to allow 3 requests per 5 seconds. To test the Rate Limiter:

Navigate to the dashboard.

Click the "Log Injection" button 4 times rapidly.

The UI will trigger a CRITICAL alert status, and the backend will return an HTTP 429 (Too Many Requests) status code.

Inspecting the Audit Trail
The persistent logs are stored in security.log in the root directory. This file remains intact even if the Docker container is destroyed, demonstrating Data Persistence.

📊 API Reference
GET /: Serves the SOC Dashboard.

GET /health: System diagnostic and heartbeat endpoint.

GET /simulate: Triggers a security incident (protected by Rate Limiter).

GET /download-logs: Serves the security.log as a downloadable attachment.

POST /clear-logs: Sanitizes the audit trail and records a system-wide purge.

| Member           | Responsibility                   |
| ---------------- | -------------------------------- |
| Anushka Gaur     | CI/CD pipeline (Jenkins), GitHub |
| Aditi Madhusudan | Docker & Kubernetes              |
| Ayushi Ghosh     | Monitoring & Security            |
