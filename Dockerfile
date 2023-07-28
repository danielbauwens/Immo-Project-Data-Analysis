FROM python:3.9

RUN mkdir /app
RUN mkdir /app/code
COPY app/ /app/code/
WORKDIR /app
RUN pip install --no-cache-dir -r code/requirements.txt
CMD ["python3", "code/main.py"]