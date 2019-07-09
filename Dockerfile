FROM alpine:latest

RUN apk add --update python py-pip
RUN pip install --upgrade pip

RUN pip install influxdb ping

COPY *.py /

ENV INFLUXHOST localhost
ENV INFLUXPORT 8086
ENV INFLUXUSER root
ENV INFLUXPASS root
ENV INFLUXDB   ping 

# time between pings in seconds
ENV POLL_INTERVAL 2  
ENV RUNTIME_SECS 60  

CMD [ "python", "ping-stats.py" ]
