FROM python:3-alpine as deps
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install waitress

FROM deps AS source
COPY ./ /app/

FROM source AS finished

CMD waitress-serve --socket=/run/waitress.sock app:app
