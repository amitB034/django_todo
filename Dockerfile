FROM python:3.11

WORKDIR /todo

COPY requirements.txt /todo/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./todo /todo

EXPOSE 8000

CMD ["python", "/todo/manage.py", "runserver", "0.0.0.0:8000"]