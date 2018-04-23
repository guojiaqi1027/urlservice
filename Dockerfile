FROM python:2.7.13-alpine
ADD . /code
WORKDIR /code
EXPOSE 8001
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:7000", "run:app"]
