FROM python:3.7-alpine 
EXPOSE 8000
COPY . . 
WORKDIR /certificate 
RUN pip3 install -r requirements.txt 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]