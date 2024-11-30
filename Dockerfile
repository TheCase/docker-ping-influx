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
ENV POLL_INTERVALs 10  

CMD [ "python", "ping-influx.py" ]
