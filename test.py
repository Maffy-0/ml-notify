from pathlib import Path
import sys

# --- もしも ml_notify がインストールされていない場合のための処理 ---
# ホームディレクトリにあることを想定
sys.path.append(str(Path.home() / "ml_notify"))

try:
    from notifier.decorators import slack_notify
except ImportError:
    print("Warning: 'notifier.decorators' could not be imported. Slack notifications will be disabled.")
    
    def slack_notify(task_name="Task"):
        def noop_decorator(func):
            return func
        return noop_decorator
# --- ここまで ---
    
@slack_notify(task_name="Model training")
def train_model(params):
    print("Training with:", params)
    return {"loss": 0.123, "accuracy": 0.95}

if __name__ == "__main__":
    params = {"lr": 0.001, "epoch": 10}
    train_model(params)
