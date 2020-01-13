from django.http import HttpResponse


# Create your views here.
def get(request):
  data = request.GET['data']
  print(data)
  return HttpResponse("hello world %s." % data)

def post(request):
  data = request.body
  print(data)
  return HttpResponse(data)