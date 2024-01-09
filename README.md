# ups-monitor

Collect historical UPS (power supply) data on an Unraid server

## env variables

| Key  | Value |
| ------------- | ------------- |
| SESSION_COOKIE  | Your unraid session cookie. Grab it from the inspector  |
| UNRAID_URL_BASE  | Example: http://192.168.0.5 |
| SCAN_INTERVAL_SECONDS  | The UPS data will be scanned on this interval |
| SCAN_OUTPUT_FILE_PATH  | Example: /home/user/output.json |