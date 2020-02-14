FROM ubuntu:18.04

RUN apt update && \
	apt -y install socat

RUN useradd -ms /bin/bash arkavidia

RUN mkdir /home/arkavidia/chall

COPY chall/stringeditor /home/arkavidia/chall
COPY chall/run.sh /home/arkavidia/chall

# Flag placeholder
RUN mkdir /var/flag
RUN printf "Arkav6{flag}" > /var/flag/00000000000000000000000000000000
RUN chmod -R 555 /var/flag

RUN chown -R root:root /home/arkavidia/chall
RUN chmod -R 555 /home/arkavidia/chall
USER arkavidia
WORKDIR /home/arkavidia/chall

CMD ["./run.sh"]