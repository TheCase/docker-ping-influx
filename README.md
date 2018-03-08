ENV VARS:

INFLUXHOST - influxdb host
INFLUXPORT - influxdb port
INFLUXDB -   influxdb database
POLL_INTERVAL - # seconds between API connections

TARGETS - space separated string of hostnames/IPs to ping

docker run -d -e TARGETS='google.com yahoo.com' --restart=always --name ping thecase/ping-influx
