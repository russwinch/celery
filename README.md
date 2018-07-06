Celery
------

Trying out Celery.

`no-celery` does some requests in the synchronous way
`celery_blog` implements celery to do the requests asyncronously
`celery_schedule` implements beat to schedule tasks


All use Redis as the message broker.

    docker run redis -p 6379:6379

The schedule is dockerised and can be launched with:

    docker-compose -f docker/docker-compose.yml up --build

(To run it outside docker the broker will need to be changed to point to localhost)
