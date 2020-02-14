FROM i386/ubuntu:18.04

RUN apt update && \
	apt -y install socat libsqlite3-0 sqlite3

RUN useradd -ms /bin/bash arkavidia
RUN mkdir /home/arkavidia/chall
RUN mkdir /home/arkavidia/chall/db

COPY chall/* /home/arkavidia/chall/
COPY chall/html/ /home/arkavidia/chall/html
COPY chall/static/ /home/arkavidia/chall/static

WORKDIR /home/arkavidia/chall
RUN sqlite3 db/probook.db -init db.sql

# Flag placeholder
RUN mkdir /var/flag
RUN printf "Arkav6{flag}" > /var/flag/00000000000000000000000000000000
RUN chmod -R 555 /var/flag

RUN chown -R root:root /home/arkavidia/chall
RUN chmod -R 555 /home/arkavidia/chall
RUN chown -R arkavidia:arkavidia /home/arkavidia/chall/db
RUN chmod -R 777 /home/arkavidia/chall/db
USER arkavidia

CMD ["./run.sh"]
