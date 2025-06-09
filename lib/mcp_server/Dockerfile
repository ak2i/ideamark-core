FROM python:3.12-slim

WORKDIR /app

COPY lib/mcp_server/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire repository so the package structure under `lib` is preserved
COPY . /app

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "lib.mcp_server.main:app", "--host", "0.0.0.0", "--port", "8000"]
