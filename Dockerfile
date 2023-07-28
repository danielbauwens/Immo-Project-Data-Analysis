FROM python:3.9-slim

RUN mkdir /app
RUN mkdir /app/code
COPY src/ /app/code/
WORKDIR /app
CMD ["uvicorn", "main:app", "--reload"]