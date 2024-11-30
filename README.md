### docker-ping-influx

Sends ping results to an InfluxDB (v1) server

### Environment Variables 

---------------------
| variable | description | default |
---------------------
| INFLUXHOST | influxdb host | "localhost" |
| INFLUXPORT | influxdb port | 8086 |
| INFLUXDB | influxdb database | ping |
| POLL_INTERVAL | interval, in seconds |
| TARGETS | space separated string of hostnames/IPs to ping
---------------------

### command line example

docker run -d -e TARGETS='google.com yahoo.com' --restart=always --name ping thecase/ping-influx

### docker-compose example

'''yaml
services:

  ping-recorder:
    image: thecase/ping-influx
    container_name: ping-recorder
    environment:
      INFLUXHOST: "influx.local"
      INFLUXPORT: 8086
      INFLUXDB: "pings"
      POLL_INTERVAL: 60
      TARGETS: "somehost.local otherhost.local"
    restart: always
'''
