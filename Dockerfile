FROM alpine
MAINTAINER anonymousyisan@gmail.com

RUN apk add --update --no-cache python3  py-pip && ln -sf python3 /usr/bin/python
RUN pip install requests pprint

COPY assets/check.py /opt/resource/check
COPY assets/in.py /opt/resource/in
COPY assets/out.py /opt/resource/out

RUN chmod +x /opt/resource/*


