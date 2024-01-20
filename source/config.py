import os

def getConfigValue(key):
    value = os.environ.get(key, None)
    if value == None:
        raise Exception(f'Missing environment variable: {key}')
    print(f'INFO - Procured {key} value from env: {value}')
    return value

UNRAID_IP = getConfigValue('UNRAID_IP').strip(' ').strip('/')
SESSION_COOKIE = getConfigValue('SESSION_COOKIE')
SCAN_INTERVAL_SECONDS = int(getConfigValue('SCAN_INTERVAL_SECONDS'))
SCAN_OUTPUT_FILE_PATH = getConfigValue('SCAN_OUTPUT_FILE_PATH')