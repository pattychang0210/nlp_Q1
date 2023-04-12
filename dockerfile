FROM python:3.7-slim

WORKDIR /workspace

COPY ./main.py /workspace

RUN pip install sentence_transformers

CMD ["python", "main.py"]