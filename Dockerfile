FROM sagnik106/ubuntu-r

RUN apt-get update -y
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip

COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]