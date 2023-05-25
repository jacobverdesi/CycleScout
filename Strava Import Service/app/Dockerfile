FROM python:3.11
WORKDIR /code

COPY requirements.txt /code/requirements.txt
# install python dependencies
RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the Python script into the container
COPY . /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
