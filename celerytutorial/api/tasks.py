from celery import shared_task
import time
from .serializers import ItemSerializer


@shared_task
def insertIntoDB(data):
    time.sleep(10)
    serializer = ItemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

    return data
