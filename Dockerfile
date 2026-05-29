FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install pandas
RUN pip install scikit-learn
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install joblib
RUN pip install prometheus-fastapi-instrumentator

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
