# Use an official Python runtime as a parent image
FROM python:3.9-alpine AS base

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Use a smaller base image for the final image
FROM python:3.9-alpine AS final

# Set the working directory in the container
WORKDIR /app

# Copy the application code from the first stage
COPY --from=base /app /app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
