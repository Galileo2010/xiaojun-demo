from django.http import HttpResponse


# Create your views here.
def hello(request):
  return HttpResponse("Hello, this is Regional IT Team.")
def get(request):
  name = request.GET['name']
  print(name)
  return HttpResponse("hello world %s." % name)

def post(request):
  data = request.body
  print(data)
  return HttpResponse(data)