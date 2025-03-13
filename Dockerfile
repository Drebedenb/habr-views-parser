FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y tree && apt-get clean

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "app.py"]