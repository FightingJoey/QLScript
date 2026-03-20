# space 保活，每十分钟请求一次
# cron: 0 */3 * * *

import requests
import time

SPACE_URL = "https://devqy-selkies.hf.space"

def keep_alive():
    try:
        response = requests.get(SPACE_URL, timeout=30)
        print(f"Pinged at {time.ctime()}: Status {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    keep_alive()