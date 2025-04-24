from pathlib import Path
import sys

# ホームディレクトリにあることを想定
sys.path.append(str(Path.home() / "ml_notify"))

from notifier.decorators import slack_notify

@slack_notify(task_name="Model training")
def train_model(params):
    print("Training with:", params)
    return {"loss": 0.123, "accuracy": 0.95}

if __name__ == "__main__":
    params = {"lr": 0.001, "epoch": 10}
    train_model(params)
