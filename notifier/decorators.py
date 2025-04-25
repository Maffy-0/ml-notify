import os
import traceback
from .slack_notifier import notify_slack, load_webhook_url

def slack_notify(task_name="Task"):
    webhook_url = load_webhook_url()

    if not webhook_url:
        print("Slack webhook config not found. Notifications are disabled.")
        def noop_decorator(func):
            return func
        return noop_decorator

    def decorator(func):
        def wrapper(*args, **kwargs):
            local_rank = os.environ.get("LOCAL_RANK")
            is_primary = (local_rank is None or local_rank == "0")

            if is_primary:
                notify_slack(f"{task_name} started.", webhook_url)
            try:
                result = func(*args, **kwargs)
                if is_primary:
                    notify_slack(f"{task_name} completed successfully.\nResult: {result}", webhook_url)
                return result
            except Exception:
                if is_primary:
                    error_message = f"{task_name} failed with an exception:\n{traceback.format_exc()}"
                    notify_slack(error_message, webhook_url)
                raise
        return wrapper
    return decorator