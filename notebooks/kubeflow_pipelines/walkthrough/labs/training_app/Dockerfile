
FROM gcr.io/deeplearning-platform-release/base-cpu
RUN pip install -U fire cloudml-hypertune scikit-learn==0.20.4 pandas==0.24.2

COPY . /app

WORKDIR /app

ENTRYPOINT ["python3", "train.py"]
