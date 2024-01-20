#!/bin/bash

watts=$(apcaccess | awk '/LOADPCT|NOMPOWER/ {print $3}' | paste -s -d ',' - | awk -F, '{printf $1 * $2 / 100}')
current_datetime=$(date +"%Y-%m-%dT%H:%M:%S")
echo "$current_datetime $watts" >> /mnt/user/trash/ups-power-usage.txt
