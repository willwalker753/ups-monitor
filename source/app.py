import time
import config

from UpsDataProcurer import UpsDataProcurer
upsDataProcurer = UpsDataProcurer(config.UNRAID_IP)

from JsonFileArrayAppender import JsonFileArrayAppender
jsonFileArrayAppender = JsonFileArrayAppender(config.SCAN_OUTPUT_FILE_PATH, 'results')

def scan_ups_data():
    upsData = upsDataProcurer.procure(config.SESSION_COOKIE)
    jsonFileArrayAppender.append(upsData)

# scan the ups data on a loop
try:
    while True:
        scan_ups_data()
        time.sleep(config.SCAN_INTERVAL_SECONDS)
except KeyboardInterrupt:
    print("Loop interrupted by user")
except Exception as e:
    print(e)