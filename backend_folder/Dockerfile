FROM python:3.10-slim

# Set the working directory
WORKDIR /code

# Copy the requirements file into the container
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Create a user to avoid running as root, which is best practice for HF Spaces
RUN useradd -m -u 1000 user
USER user

# Copy the application code
COPY --chown=user ./app /code/app

# Command to run the FastApi app
# Hugging Face Spaces expose port 7860 by default
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
