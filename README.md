# Backend Setup and Deployment

## Prerequisites
Ensure you have the following installed on your machine:
- **Docker** and **Docker Compose**
- **Bash (for running scripts)** (Use Git Bash on Windows if needed)

## Project Structure
```
.
├── docker-compose.yml    # Docker Compose configuration
├── run.sh                # Script to start the backend
├── .env                  # Environment variables (non-sensitive)
├── .env.example          # Example environment variables file
├── table.sql             # SQL schema for PostgreSQL
└── backend/              # Backend source code
    ├── src/              # Source code
    ├── tests/            # Test cases
    ├── package.json      # Node.js dependencies
    └── tsconfig.json     # TypeScript configuration
```

## Environment Variables
- Store non-sensitive variables in `.env`.
- Copy `.env.example` to `.env` and fill in the environment variables accordingly.

## Running the Backend
To start the backend, run:
```sh
./run.sh
```
This will:
1. Load environment variables.
2. Start the backend using Docker Compose.

To stop the backend, run:
```sh
./run.sh stop
```

## Troubleshooting
- If you change database credentials, delete old volumes:
  ```sh
  docker-compose down
  docker volume rm <your_project>_postgres_data
  docker-compose up --build -d
  ```
- Check running containers:
  ```sh
  docker ps
  ```
- View logs:
  ```sh
  docker-compose logs -f
  ```

## Notes
- **Do not commit `.env` to Git.**
- Make sure Docker is running before executing `run.sh`.
- The backend runs on **port 5000** and PostgreSQL on **port 5432**.

---
