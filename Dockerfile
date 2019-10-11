# Python2 Alpine

# Geschrieben von
# Matthias Pröll <proell.matthias@gmail.com>
# Staudigl-Druck GmbH & Co. KG
# Letzte Anpassung: 2019/09/17

FROM alpine:latest

# Labels
LABEL vendor="Staudigl-Druck GmbH & Co. KG"
LABEL maintainer="Matthias Pröll (proell.matthias@gmail.com)"
LABEL release-date="2019-09-17"

RUN apk add docker bash curl python python-dev build-base py-pip && \
    rm -rf /var/cache/apk/*

RUN pip install uptime telepot requests

RUN cd /

CMD ["python", "bot.py"]
