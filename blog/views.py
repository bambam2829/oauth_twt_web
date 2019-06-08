from django.shortcuts import render
from .models import Test
# Create your views here.
def post_list(request):
    test = Test(100,100)
    result = test.calc
    array = {'result' : result}
    return render(request, 'blog/post_list.html',array)
