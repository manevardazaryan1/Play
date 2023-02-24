from celery import shared_task

from play_project.celery import app


@app.task
def fibon(n):
    print(n)

