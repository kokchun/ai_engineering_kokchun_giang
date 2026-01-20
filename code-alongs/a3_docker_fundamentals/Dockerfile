# python will be preinstalled in our container
FROM python:3.11-slim

# specify where you want your working directory to be
WORKDIR /app

# copies everything in this folder in host into my working directory in container
COPY . .

RUN pip install -r requirements.txt 

# python dashboard.py
CMD [ "python", "dashboard.py" ]
