FROM python:3.8-alpine

# Set our working directory
WORKDIR /home

# Ensure PIP updated
RUN pip install --upgrade pip

# Copy our dependencies
COPY ./requirements.txt /home/requirements.txt

# Install our dependencies
RUN pip install -r requirements.txt

# Copy our Project code
COPY ./trading_app /home/trading_app/