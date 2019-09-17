# Python2 Alpine

FROM alpine:latest

RUN apk add docker python python-dev build-base py-pip && \
    rm -rf /var/cache/apk/*

RUN pip install uptime telepot requests

RUN cd /

CMD ["python", "bot.py"]
