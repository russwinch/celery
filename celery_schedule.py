from celery import Celery
from celery.schedules import crontab

app = Celery('celery_schedule', broker='redis://redis')
app.conf.timezone = 'Europe/London'

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # testing
    sender.add_periodic_task(5.0, test.s('test'))

    sender.add_periodic_task(
        crontab(hour=9, minute=30, day_of_week='mon-fri'),
        test.s('Good morning'),
    )

@app.task
def test(arg):
    print(arg)
