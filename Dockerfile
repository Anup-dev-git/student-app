FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]

