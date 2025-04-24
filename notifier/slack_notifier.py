import json
import urllib.request
from pathlib import Path

def load_webhook_url():
    config_path = Path.home() / "ml_notify" / "slack_config.json"
    if not config_path.exists():
        return None
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        return config.get("slack_webhook_url")
    except Exception:
        return None

def notify_slack(message: str, webhook_url: str = None):
    if webhook_url is None:
        webhook_url = load_webhook_url()
    if not webhook_url:
        return  # No-op if webhook is missing

    payload = {"text": message}
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as res:
            print(f"Slack notification succeeded: HTTP {res.status}")
    except Exception as e:
        print(f"Slack notification failed: {e}")
