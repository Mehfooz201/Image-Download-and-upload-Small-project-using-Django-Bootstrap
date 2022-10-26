from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Image
from django.db.models import Q
from .forms import ImageAdmin

# Create your views here.

def index(request):
    obj = Image.objects.all()
    return render(request, 'myapp/index.html', {'obj':obj})


def details_img(request, id):
    obj = Image.objects.get(pk=id)
    return render(request, 'myapp/details.html', {'obj':obj})


def add_image(request):
    if request.method=='POST':
        form = ImageAdmin(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('index')
    else:        
        form = ImageAdmin()

    return render(request, 'myapp/addimage.html', {'form':form})


def search(request):
    query = None
    result = []
    if request.method == 'GET':
        query = request.GET.get('search')
        result = Image.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))
    return render(request, 'myapp/search.html', {'query':query, 'result':result})
