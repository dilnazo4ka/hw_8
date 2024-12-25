FROM python:3.9-slim

WORKDIR /app

COPY req.txt req.txt

RUN pip install --no-cache-dir -r req.txt

COPY hw_8.py hw_8.py

# Set the default command
CMD ["python3", "hw_8.py"]
