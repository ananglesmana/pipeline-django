FROM django:latest

COPY coba /usr/share/coba
WORKDIR /usr/share/coba

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


