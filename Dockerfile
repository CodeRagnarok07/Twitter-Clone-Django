FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py runserver 0.0.0.0:8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]