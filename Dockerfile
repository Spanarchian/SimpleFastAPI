FROM python:3.10.11
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./src  /src
CMD [ "uvicorn", "api:api", "--host", "0.0.0.0", "--port", "8765"]
