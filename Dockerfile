FROM python:alpine

# Install gunicorn
RUN pip install gunicorn

# Install flask
RUN pip install flask

# Add demo app
COPY ./flask-app /app
WORKDIR /app

EXPOSE 3499

CMD ["gunicorn", "-b", "0.0.0.0:3499", "main:app"]