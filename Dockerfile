# Use official Python image
FROM python:3.9

# Set the working directory inside the container to the root
WORKDIR /app

# Copy all project files into the container
COPY . /app/

# Set the working directory inside the container to the Django project folder
WORKDIR /app/petology

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose Django's default port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
