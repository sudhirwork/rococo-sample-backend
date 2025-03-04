#!/bin/bash

echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL started!"

echo "Starting Flask app..."
exec python run.py
