FROM python:3.13

WORKDIR /app

# RUN apt-get install -y tree # TODO: for dev

# Set environment variables 
# Prevents Python from writing pyc files to disk
# ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
# ENV PYTHONUNBUFFERED=1 

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/api
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:5000"]