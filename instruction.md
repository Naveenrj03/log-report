An Apache-style HTTP access log is located at /app/access.log. Parse this log file to analyze traffic statistics and save a JSON summary report to /app/report.json.

The output report at /app/report.json must be a JSON object containing the following exact keys:
1. `total_requests` (integer): The total number of valid non-empty log entries in /app/access.log.
2. `unique_ips` (integer): The count of distinct client IP addresses initiating requests.
3. `top_path` (string): The request URL path (e.g. /index.html) that appears most frequently in the log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
