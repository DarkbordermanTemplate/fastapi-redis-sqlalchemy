FROM python:3.7.7-slim
RUN pip install pipenv

WORKDIR /api/
COPY Pipfile /api/Pipfile
COPY Pipfile.lock /api/Pipfile.lock
RUN pipenv install
COPY ./api/ /api/

CMD ["pipenv", "run", "uvicorn", "--port", "8000", "--host", "0.0.0.0","--log-level", "error", "app:APP"]
