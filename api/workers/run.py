from time import sleep

from celery import Celery
from celery.utils.log import get_task_logger

from api.workers.config import CeleryConfig

celery_app = Celery(__name__)
celery_app.config_from_object(CeleryConfig)


logger = get_task_logger(__name__)


@celery_app.task(name="wait_for")
def wait_for(seconds: int, fail: bool = False) -> str:
    if fail:
        logger.error(f"Deliberately failed to wait for {seconds} seconds.")
        raise RuntimeError
    logger.info("Going to sleep...")
    sleep(seconds)
    logger.info("Waking up!")
    return f"Waited for {seconds} seconds."
