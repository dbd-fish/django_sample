# logging_config.py

import os
import logging
from datetime import datetime
from pytz import timezone

# 日本時間を取得
japan_timezone = timezone('Asia/Tokyo')
japan_time = datetime.now(japan_timezone)

# ログフォルダのパスを取得
log_folder_path = 'log'
if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)

# ロギングの設定
log_file_format = japan_time.strftime('%Y-%m-%d')
log_file_path = os.path.join(log_folder_path, f'api_logs_{log_file_format}.log')

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
