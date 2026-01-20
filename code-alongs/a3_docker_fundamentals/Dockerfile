# python will be preinstalled in our container
FROM python:3.11-slim

# specify where you want your working directory to be
WORKDIR /app

# copies everything in this folder in host into my working directory in container
COPY . .

RUN pip install -r requirements.txt 

EXPOSE 8501

CMD [ "streamlit", "run", "dashboard.py" ]

# docker run --name dashboard1 cool_dashboard