FROM python:3.9.6-alpine

# Create user and group
RUN addgroup -S mercari && adduser -S trainee -G mercari

# Set the working directory
WORKDIR /app

# Install dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set user to 'trainee'
USER trainee

# check python version
CMD ["python3", "-V"]
