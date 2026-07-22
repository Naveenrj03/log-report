import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def test_report_exists_and_valid_json():
    """Verify that /app/report.json exists and is valid JSON."""
    assert REPORT_PATH.exists(), "Report file /app/report.json does not exist."
    with open(REPORT_PATH, "r") as f:
        data = json.load(f)
    assert isinstance(data, dict), "Report content must be a JSON object."


def test_total_requests():
    """Criterion 1: Verify total_requests count in /app/report.json."""
    with open(REPORT_PATH, "r") as f:
        data = json.load(f)
    assert "total_requests" in data, "Key 'total_requests' missing from report."
    assert data["total_requests"] == 6, f"Expected total_requests=6, got {data.get('total_requests')}"


def test_unique_ips():
    """Criterion 2: Verify unique_ips count in /app/report.json."""
    with open(REPORT_PATH, "r") as f:
        data = json.load(f)
    assert "unique_ips" in data, "Key 'unique_ips' missing from report."
    assert data["unique_ips"] == 3, f"Expected unique_ips=3, got {data.get('unique_ips')}"


def test_top_path():
    """Criterion 3: Verify top_path string in /app/report.json."""
    with open(REPORT_PATH, "r") as f:
        data = json.load(f)
    assert "top_path" in data, "Key 'top_path' missing from report."
    assert data["top_path"] == "/index.html", f"Expected top_path='/index.html', got {data.get('top_path')}"
