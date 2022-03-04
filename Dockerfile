FROM python:3.10.2-alpine

EXPOSE 8000

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --no-cache-dir

WORKDIR /app
COPY . .

CMD ["uvicorn", "cafe.app:app"]
