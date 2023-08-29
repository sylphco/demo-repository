# Pull Base Image
FROM python:3.10-slim

# Create Virtual Environment
# establishg working directory for image
WORKDIR /build

# copy dependency definitions from root context into build image ./build/app
COPY dev-requirements.txt /build
COPY requirements.txt /build


# install dependencies WORKDIR
RUN pip install --no-cache-dir -r dev-requirements.txt

# copy source files into build files
COPY app /build/app

# Expose Port in Container
EXPOSE 80

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765", "--reload"]
