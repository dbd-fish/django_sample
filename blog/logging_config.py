import logging
import os
from datetime import datetime

from pytz import timezone


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name,
            "pathname": record.pathname,
            "lineno": record.lineno,
            "funcName": record.funcName,
        }

        if record.exc_info:
            log_record["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info:
            log_record["stack_info"] = record.stack_info

        formatted_log = (
            "{\n"
            f"\t'timestamp': '{log_record['timestamp']}',\n"
            f"\t'level': '{log_record['level']}',\n"
            f"\t'message': '{log_record['message']}',\n"
            f"\t'name': '{log_record['name']}',\n"
            f"\t'pathname': '{log_record['pathname']}',\n"
            f"\t'lineno': {log_record['lineno']},\n"
            f"\t'funcName': '{log_record['funcName']}',\n"
            f"\t'exc_info': '{log_record.get('exc_info', '')}',\n"
            f"\t'stack_info': '{log_record.get('stack_info', '')}'\n"
            "}"
        )

        return formatted_log


def setup_logging():
    # 日本時間を取得
    japan_timezone = timezone("Asia/Tokyo")
    japan_time = datetime.now(japan_timezone)

    # ログフォルダのパスを取得
    log_folder_path = "log"
    if not os.path.exists(log_folder_path):
        os.makedirs(log_folder_path)

    # ロギングの設定
    log_file_format = japan_time.strftime("%Y-%m-%d")
    log_file_path = os.path.join(log_folder_path, f"api_logs_{log_file_format}.log")

    # 構造化ログを使うように変更
    formatter = JsonFormatter()
    handler = logging.FileHandler(log_file_path)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


# インポート時にログ設定を行う
setup_logging()
