FROM python:3.11.4-slim
RUN mkdir /app
COPY ./api_requirements.txt /app/api_requirements.txt
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r /app/api_requirements.txt
EXPOSE 8000

CMD ["sh", "-c", "cd /app && uvicorn main:app --reload --host 0.0.0.0 --port 8000"]