FROM ubuntu

RUN apt update -y && apt install python3-pip -y && pip3 install pip --upgrade && apt clean

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]