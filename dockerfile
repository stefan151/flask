FROM python:3

WORKDIR ./

RUN pip install flask

COPY . .

CMD ["python", "app.py"]