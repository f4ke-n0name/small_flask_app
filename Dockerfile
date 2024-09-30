FROM ubuntu:latest
LABEL authors="Данил"

ENTRYPOINT ["top", "-b"]

FROM python:3.11
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements.txt
RUN python -m unittest discover -s test -p "*.py"


COPY . .

EXPOSE 5000
