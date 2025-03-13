FROM python:3.9.6-alpine

# Create user and group
RUN addgroup -S mercari && adduser -S trainee -G mercari

# Set the working directory
WORKDIR /app

# Install dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . ./python/

# change permission 
RUN chown -R trainee:mercari /app/python

# Set user to 'trainee'
USER trainee

# Launch FastAPI
CMD ["uvicorn", "python.main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
