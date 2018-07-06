Celery
------

Trying out Celery.

`no-celery` does some requests in the synchronous way
`celery_blog` implements celery to do the requests asyncronously
`celery_schedule` implements beat to schedule tasks


All use redis as a message broker.

The schedule is dockerised and can be launched with:
    docker-compose -f docker/docker-compose.yml up --build
