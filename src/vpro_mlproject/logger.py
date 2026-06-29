import logging
import os
from datetime import datetime

LOG_FILE = f"vpro_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Logging setup complete. Log file created at: %s", LOG_FILE_PATH)