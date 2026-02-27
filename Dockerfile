FROM python:3.10

WORKDIR /app

# Install netcat to check MySQL port
RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD sh -c "until nc -z $DB_HOST 3306; do echo 'Waiting for MySQL port...'; sleep 3; done; echo 'MySQL is ready!'; pytest --html=report.html --self-contained-html"
