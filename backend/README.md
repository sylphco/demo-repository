# Activate Development Environment
- `python -m venv <directory>`
- `source bin/activate`
- `python -m pip install -r dev-requirements.txt`

# Deactivating Development Environment
- `deactivate`

* Dev requirements includes dependencies for pre-commit hooks, linting, formatting, etc.

# Build Docker Image using Docker Compose:
- `docker compose build`

# Run Docker Compose for Application:
- `docker compose up`
- If you want to run it in detached mode `docker compose up -d`

# Gracefully Close Docker Container:
- `docker compose down`
