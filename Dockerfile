FROM alpine
MAINTAINER anonymousyisan@gmail.com

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN pip install requests

COPY assets/check.py /opt/resource/check
COPY assets/in.py /opt/resource/in
COPY assets/out.py /opt/resource/out

RUN chmod +x /opt/resource/*


