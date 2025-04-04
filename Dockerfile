# official python image
FROM python:3.11-slim-bullseye

# workspace in the container
WORKDIR /proveeagro/backend

# install all the pip dependencies from requirements.txt
COPY requirements.txt ./

RUN pip install --upgrade pip --no-cache-dir

RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the directory to the container
COPY . .

# Run the server
CMD ["gunicorn", "proveeagro.wsgi:application", "--bind", "0.0.0.0:8000"]