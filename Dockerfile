FROM python:3.8-slim-buster
COPY ./certificate .
CMD [ "python3", "manage.py", "runserver" ]
