# Use official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker's caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app

# Expose the port Chainlit runs on
EXPOSE 8000

# Command to run the app
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "8000"]
