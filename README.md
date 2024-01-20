# ups-monitor

This is used to collect historical UPS power usage data on an server. 

### Usage Notes

The shell script can be ran using a cron job. 
It parses output from the apcaccess command and then logs the datetime and watts to a text file.

The html is a self contained webapp (work in progress) to view the results from the text file.
