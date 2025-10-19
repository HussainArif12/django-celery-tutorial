from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Item
from .serializers import ItemSerializer
from rest_framework.parsers import JSONParser
from .tasks import insertIntoDB
from django_celery_results.models import TaskResult


# Create your views here.
@api_view(["GET", "POST"])
def index(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        insertIntoDB.delay(data)
        return JsonResponse(
            {"message": "Item creation task has been added to the queue"}
        )
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def view_tasks(request):
    tasks = TaskResult.objects.all()
    return JsonResponse({"tasks": list(tasks.values())})
