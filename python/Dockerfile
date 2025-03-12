FROM python:3.9.6-alpine

# Create user and group
RUN addgroup -S mercari && adduser -S trainee -G mercari

# Set the working directory
WORKDIR /app
RUN mkdir python
RUN mkdir python/images
RUN mkdir python/db

# Install dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY __init__.py ./python/
COPY main.py ./python/
COPY schemas.py ./python/
COPY models.py ./python/
COPY database.py ./python/
COPY crud.py ./python/
# Copy images directory
COPY images/default.jpg ./python/images/
# Copy database
COPY db/mercari.sqlite3 ./python/db/

# change permission 
RUN chown -R trainee:mercari /app/python

# Set user to 'trainee'
USER trainee

# Launch FastAPI
CMD ["uvicorn", "python.main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
