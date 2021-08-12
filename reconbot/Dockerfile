FROM ubuntu:latest
RUN mkdir bot
WORKDIR bot
COPY . .
RUN apt update
RUN apt install -y python
RUN apt install -y python-is-python3
RUN apt install -y python3-pip
RUN pip3 install discord
RUN pip3 install requests
CMD [ "python3", "app.py" ]
