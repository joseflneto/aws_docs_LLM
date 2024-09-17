FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY utils.py utils.py
COPY variables.py variables.py
COPY faiss_index.bin faiss_index.bin
COPY metadata.pkl metadata.pkl

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
