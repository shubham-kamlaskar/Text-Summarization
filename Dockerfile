FROM python:3.12.2-slim-bookworm

COPY . /app

WORKDIR  /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV NAME WorldOne

EXPOSE 8080
CMD ["streamlit","run","kick.py"]