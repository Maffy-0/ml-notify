# ml_notify

機械学習など時間がかかる実験前後にSlackへ通知を送ります．
モデルの学習や検証処理の前後に，Slackへ開始・終了・エラー情報などを自動通知するためのデコレータや関数を提供します．

## セットアップ手順

1. ホームディレクトリにSlackのWebhook URLを記述した設定ファイルを用意します。

   - パス： `~/ml_notify/slack_config.json`
   - 例：

```json
{
  "slack_webhook_url": "https://hooks.slack.com/services/XXX/YYY/ZZZ"
}
```

通知機能を使用したいプロジェクト内で，ml-notify をパスに追加します．

```python
import sys
from pathlib import Path
sys.path.append(str(Path.home() / "ml-notify"))

from notifier.decorators import slack_notify

@slack_notify(task_name="モデル学習")
def train_model(params):
    # 学習処理など
    return {"loss": 0.123, "accuracy": 0.95}
```

Slack設定ファイルが存在しない場合や無効な場合は、通知はスキップされます。