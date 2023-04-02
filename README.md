<h1 align="center">Simple Social Network API</h1>


## Description

This is a simple social network created using Django.

## Technologies used

- Python
    - Django
    - DRF
- Docker
- PostgreSQL

## Usage

Run

```shell
docker-compose up --build -d
```

Stop

```shell
docker-compose down
```

> **Note**
> To create an admin, you can use the command:
> ```shell
> docker ps # copy id api container
> docker exec -it <container-id> bash # go in container bash by id
> python manage.py createsuperuser # create superuser
> ```
> After go to `/admin/`