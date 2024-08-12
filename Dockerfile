FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt


COPY . /app


CMD ["sh", "-c", "python create_database.py && python create_tables.py"]
