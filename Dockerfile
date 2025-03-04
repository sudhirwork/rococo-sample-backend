# Use Python 3.11 base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]
