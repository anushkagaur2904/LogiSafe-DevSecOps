<h1>🛡️ LogiSafe Sentinel</h1>
<h2>Ultra Containerized Security Operations Center (SOC) Simulator
</h2>
LogiSafe Sentinel is a high-performance microservice designed to demonstrate real-world security monitoring, incident response, and resource protection. It features a Python Flask engine and a Real-time Vanilla JS dashboard, all orchestrated within a Docker environment.


<h1>🚀 Advanced Features</h1>
<b>DDoS Mitigation (Rate Limiting):</b> Implements a sliding-window algorithm to detect and throttle high-frequency request bursts.

<b>Real-Time Heartbeat:</b> Asynchronous polling of the /health endpoint to monitor engine stability and latency.

<b>Persistent Audit Trail: </b>State-of-the-art logging using Python's logging library, synchronized to the host machine via Docker Volumes.

<b>Data Lifecycle Suite:</b> Integrated tools for Incident Generation, Audit Exporting, and Cryptographic Purging (Log Sanitization).

<b>SOC UI:</b> A professional, SVG-enhanced dashboard supporting both Dark and Light modes for administrative flexibility.


<h1>🛠️ Technical Architecture</h1>

| **Layer**   | **Technology**           | **Function**                           |
| ----------- | ------------------------ | -------------------------------------- |
| Backend     | Python 3.10 / Flask      | RESTful Security Engine                |
| Frontend    | HTML5 / CSS3 / ES6+      | Real-time SOC Dashboard                |
| Security    | Sliding Window Algorithm | DDoS / Rate Limit Protection           |
| Persistence | Docker Volumes           | Host-to-Container Data Synchronization |
| DevOps      | Docker Compose           | Microservice Orchestration             |

<h1>🧪 Security Testing (QA)</h1>
<h2>Triggering a DDoS Alert
</h2>
The system is configured to allow 3 requests per 5 seconds. To test the Rate Limiter:

Navigate to the dashboard.

Click the "Log Injection" button 4 times rapidly.

The UI will trigger a CRITICAL alert status, and the backend will return an HTTP 429 (Too Many Requests) status code.

<b>Inspecting the Audit Trail</b>
The persistent logs are stored in security.log in the root directory. This file remains intact even if the Docker container is destroyed, demonstrating Data Persistence.

<h1>📊 API Reference
</h1>
<b>GET /:</b> Serves the SOC Dashboard.


<b>GET /health:</b> System diagnostic and heartbeat endpoint.

<b>GET /simulate:</b> Triggers a security incident (protected by Rate Limiter).

<b>GET /download-logs: </b>Serves the security.log as a downloadable attachment.

<b>POST /clear-logs: </b>Sanitizes the audit trail and records a system-wide purge.

| Member           | Responsibility                   |
| ---------------- | -------------------------------- |
| Anushka Gaur     | CI/CD pipeline (Jenkins), GitHub |
| Aditi Madhusudan | Docker & Kubernetes              |
| Ayushi Ghosh     | Monitoring & Security            |
