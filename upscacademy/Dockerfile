FROM python:3.10-alpine3.15

# install mysqlclient 
RUN apt-get update && \
    apt-get install -y build-essential default-libmysqlclient-dev mariadb-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# create Environment 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create working directory
WORKDIR /app

# Copy just the requirements file first to leverage Docker caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# update all migrations 
RUN python manage.py makemigrations
RUN python manage.py migrate
# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]