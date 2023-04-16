# Use an official Python runtime as a parent image
FROM python:3-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

ENV PYTHONPATH "${PYTHONPATH}:/app/"

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define the command to run your Python script using the main method as the entry point
CMD [ "python", "drs_compliance/drs_compliance_runner.py" ]