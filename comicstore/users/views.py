from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def land(request):
    return render(request,'users/land.html')

def landon(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(username,password,remember)
    context = {
        'next_url':'/users/land'
    }
    return JsonResponse({"res":1},context)