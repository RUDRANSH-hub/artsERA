from django.shortcuts import render
from KNIT_app.models import Form
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
def music(request):
    return render(request, 'music.html')
def content(request):
    return render(request, 'content.html')
def photography(request):
    return render(request, 'photography.html')


def form(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        img = request.POST.get('img')
        catagory=request.POST.get('catagory')
        form = Form(name= name, email=email, phone=phone, desc=desc, img=img, catagory=catagory)
        form.save()

    return render(request, 'form.html')
    