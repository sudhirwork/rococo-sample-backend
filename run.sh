#!/bin/bash

# Load environment variables from .env
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Function to start the backend
start_backend() {
    echo "Starting backend using Docker Compose..."
    docker-compose up --build -d
    echo "Backend is running!"
}

# Function to stop the backend
stop_backend() {
    echo "Stopping backend..."
    docker-compose down
    echo "Backend has stopped."
}

# Function to restart the backend
restart_backend() {
    stop_backend
    start_backend
}

# Function to show logs
show_logs() {
    docker-compose logs -f
}

# Handle command-line arguments
case "$1" in
    start)
        start_backend
        ;;
    stop)
        stop_backend
        ;;
    restart)
        restart_backend
        ;;
    logs)
        show_logs
        ;;
    *)
        echo "Usage: ./run.sh {start|stop|restart|logs}"
        exit 1
        ;;
esac
