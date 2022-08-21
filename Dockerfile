# syntax=docker/dockerfile:1

FROM python:3
LABEL author="Kishan"
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt 
COPY . .
ENTRYPOINT ["python3"]
CMD ["webp.py"]
