# Pull Base Image
FROM python:3.10-slim

# Create Virtual Environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTAUL_ENV/bin:$PATH"

# establishg working directory for image
WORKDIR /build/app

# copy dependency definitions from root context into build image ./build/app
COPY ../dev-requirements.txt .


# install dependencies WORKDIR
RUN pip install --no-cache-dir -r dev-requirements.txt

# copy source files into build files
COPY ../app/ .

# Expose Port in Container
EXPOSE 8765

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765", "--reload"]
