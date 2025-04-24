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
            notify_slack(f"{task_name} started.", webhook_url)
            try:
                result = func(*args, **kwargs)
                notify_slack(f"{task_name} completed successfully.\nResult: {result}", webhook_url)
                return result
            except Exception as e:
                error_message = f"{task_name} failed with an exception:\n{traceback.format_exc()}"
                notify_slack(error_message, webhook_url)
                raise e
        return wrapper
    return decorator
