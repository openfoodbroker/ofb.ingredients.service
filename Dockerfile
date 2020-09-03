FROM python:3.8.5

COPY . /app/
WORKDIR /app/

RUN pip3 install -r requirements.txt
RUN useradd -ms /bin/bash admin
USER admin
WORKDIR /app
CMD flask run --host=0.0.0.0


