# Use an official Python runtime as a parent image
FROM python:3.7

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /petology

# Copy the requirements file into the container
COPY requirements.txt /petology/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /petology/

# Expose port 8000 to the outside world
EXPOSE 8000

# Define the command to run your Django app
CMD ["python", "petology/manage.py", "runserver", "0.0.0.0:8000"]
