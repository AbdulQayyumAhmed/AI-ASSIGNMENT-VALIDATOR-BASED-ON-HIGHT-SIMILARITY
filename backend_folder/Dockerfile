FROM python:3.10-slim

# Set the working directory
WORKDIR /code

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    librandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install Playwright and Chromium
RUN playwright install --with-deps chromium

# Create a user to avoid running as root, which is best practice for HF Spaces
RUN useradd -m -u 1000 user
USER user

# Copy the application code
COPY --chown=user ./app /code/app

# Command to run the FastApi app
# Hugging Face Spaces expose port 7860 by default
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]

