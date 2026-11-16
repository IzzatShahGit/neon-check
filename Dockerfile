FROM python:3.12-slim
WORKDIR /app
COPY check.py .
EXPOSE 8080
CMD ["python", "check.py"]
