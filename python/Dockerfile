FROM python:3.9.6-alpine

# Create user and group
RUN addgroup -S mercari && adduser -S trainee -G mercari

# Set the working directory
WORKDIR /python

# Install dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set user to 'trainee'
USER trainee

# Copy application code
COPY __init__.py .
COPY main.py .
COPY schemas.py .
COPY models.py .
COPY database.py .
COPY crud.py .
# Copy images directory
COPY images/default.jpg ./images
# Copy database
COPY db/mercari.sqlite3 ./db


# Launch FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
