FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./my_model.h5 ./my_model.h5
COPY ./label_encoder.pkl ./label_encoder.pkl
COPY ./templates ./templates
COPY ./static ./static
COPY ./app.py ./app.py

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]