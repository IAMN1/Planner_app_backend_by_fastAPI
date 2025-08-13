FROM python:latest

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

EXPOSE 8000

COPY ./ /app

CMD [ "python", "main.py" ]