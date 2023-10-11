from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult

# Create your views here.

def index(request):
  print("Results: ")
  result = add.delay(10, 20)
  print("Result 1: ", result)
  print("Ready: ", result.ready())
  print("Successful: ", result.successful())
  print("Failed: ", result.failed())
  # result2 = sub.delay(10, 20)
  # print("Result 1: ", result2)
  return render(request, "myapp/home.html", {'result': result})

# def index(request):
#   print("Results: ")
#   result = add.apply_async(args=[10, 20])
#   print("Result 1: ", result)
#   # result2 = sub.apply_async(args=[10, 20])
#   # print("Result 2: ", result2)
#   return render(request, "myapp/home.html", {'result': result})

def check_result(request, task_id):
  result = AsyncResult(task_id)
  print("Ready 1: ", result.ready())
  print("Successful 1: ", result.successful())
  print("Failed 1: ", result.failed())  
  print("Id: ", result.id)
  print("Task Id: ", result.task_id)
  print("State: ", result.state)
  return render(request, "myapp/result.html", {'result': result})

def contact(request):
  return render(request, "myapp/contact.html")

def about(request):
  return render(request, "myapp/about.html")