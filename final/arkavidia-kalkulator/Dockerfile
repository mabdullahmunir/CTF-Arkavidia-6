FROM python:3.6-alpine

RUN adduser -D -u 1001 -s /bin/bash arkavidia

COPY chall/requirements.txt /
RUN pip install -r /requirements.txt

COPY chall /app
WORKDIR /app

# Flag placeholder
RUN mkdir /var/flag
RUN printf "Arkav6{flag}" > /var/flag/00000000000000000000000000000000
RUN chmod -R 555 /var/flag

RUN chown -R root:root /app
RUN chmod -R 555 /app
USER arkavidia
WORKDIR /app

CMD ["python", "/app/app.py"]
