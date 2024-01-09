import os
from UpsDataProcurer import UpsDataProcurer

def getConfigValue(key):
    value = os.environ.get(key, None)
    if value == None:
        raise Exception(f'Missing environment variable: {key}')
    print(f'INFO - Procured {key} value from env: {value}')
    return value
unraidUrlBase = getConfigValue('UNRAID_URL_BASE').strip(' ').strip('/')
sessionCookie = getConfigValue('SESSION_COOKIE')
scanIntervalSeconds = getConfigValue('SCAN_INTERVAL_SECONDS')
scanOutputFilePath = getConfigValue('SCAN_OUTPUT_FILE_PATH')


upsDataProcurer = UpsDataProcurer(unraidUrlBase)
upsData = upsDataProcurer.procure(sessionCookie)
print(upsData)