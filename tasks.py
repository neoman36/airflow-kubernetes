from time import sleep

from celery import Celery

app = Celery(
    main='tasks',
    broker='amqp://localhost',
    backend='db+postgresql://celery:celery@localhost:5432/celery',
)
app.conf.database_engine_options = {'echo': True}


@app.task
def add(x, y):
    sleep(10)
    return x + y
