FROM python:3.11.4-slim
RUN mkdir /app
COPY ./scraping_requirements.txt /app/scraping_requirements.txt
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r /app/scraping_requirements.txt

CMD ["sh", "-c", "cd /app && python main.py"]
# CMD ["sh", "-c", "cd /app && python async_main.py"]