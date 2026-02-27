FROM python:3.10
WORKDIR /app
RUN apt-get update && apt-get install -y default-mysql-client
COPY . .
RUN pip install -r requirements.txt
CMD sh -c "until mysqladmin ping -h $DB_HOST -u$DB_USER -p$DB_PASSWORD --silent; do echo 'Waiting for MySQL...'; sleep 3; done; echo 'MySQL is ready!'; pytest --html=report.html --self-contained-html"


