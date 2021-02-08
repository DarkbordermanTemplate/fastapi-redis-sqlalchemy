# FastAPI-redis
Fastapi framework template, with basic redis operations.

![Integration](https://github.com/DarkbordermanTemplate/fastapi-redis/workflows/Integration/badge.svg)

## Development

### Prerequisitive

| Name | Version |
| --- | --- |
| Python | 3.7 |
| pipenv(Python module) | 2018.11.26 or up |

### Environment setup

0. Initialize environment variable

```
cp sample.env .env
```

1. Initialize Python environment

```
make init
```

2. Enter the environment and start developing

```
pipenv shell
```

3. Start development API service

```
cd api/
uvicorn app:APP
```
The server will run at http://127.0.0.1:8000


### Formatting

This project uses `black` and `isort` for formatting

```
make reformat
```

### Linting

This project uses `pylint` and `flake8` for linting

```
make lint
```

### Testing

This project uses `pytest` and its extension(`pytest-cov`) for testing

## Deployment

### Prerequisitive

| Name | Version |
| --- | --- |
| Docker | 19.03.6 |
| docker-compose | 1.17.1 |

### Building image

```
docker-compose build
```
This will build the image with tag `fastapi-template:latest`

### Deployment step

The service is deployed with `docker-compose`.

0. Start containers
```
docker-compose up
```

## Contribution

* Darkborderman/Divik(reastw1234@gmail.com)
