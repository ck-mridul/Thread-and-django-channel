from django.shortcuts import render
from django.http import JsonResponse
from .tread import CreateStudentsThread
from channels.layers import get_channel_layer

# Create your views here.


async def home(request):
   
    return render(request, 'home.html')


def generate_student_data(request):
    total = request.GET.get('total')
    CreateStudentsThread(total).start()    
    return JsonResponse({"status":200})