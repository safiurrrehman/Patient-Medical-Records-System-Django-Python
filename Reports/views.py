from django.shortcuts import render,redirect
from .models import Patient, Doctor, Admin
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

def logIn(request):
    if request.method == 'POST':
        user = request.POST['username']
        if user:
            match = Patient.objects.filter(name=user)
            matcher = Doctor.objects.filter(name=user)
            admin = Admin.objects.filter(name=user)
            if match:
                return render(request, 'Reports/record.html',{'sr': match})
            elif matcher:
                return render(request, 'Reports/search.html')
            elif admin:
                return render(request, 'Reports/register.html')
            else:
                return HttpResponse('no record found')

        else:
            return HttpResponse('/search')
    return render(request, 'PMS/home.html')

def search(request):
    if request.method == 'POST':
        srch = request.POST['srch']
        if srch:
            match = Patient.objects.filter(id=srch)
            if match:

                return render(request, 'Reports/result.html', {'sr': match})
            else:
                return HttpResponse('no record found')
        else:
            return HttpResponse('/search')
    return render(request, 'Reports/search.html')


def patient(request):
    if request.method == 'POST':

        first_name = request.POST['pat_name']
        last_name = request.POST['l_name']
        age = request.POST['age']

        pat_gender = request.POST.get('gen', 'Female')
        address = request.POST['address']
        code = request.POST['code']
        number = request.POST['number']
        disease = request.POST['dis']
        history = request.POST['hist']
        Doctor = request.POST['doc_name']
        doc_gender = request.POST.get('gends', 'Female')
        b = Patient.objects.create(name=first_name, age=age, gender=pat_gender,address=address,phone=number, disease=disease, previousHistory=history, doctor=Doctor,
                                   email=first_name+'@gmail.com')
        b.save()
        return redirect('register')
        #return HttpResponse("submitted")




    else:
        return render(request, 'Reports/register.html')
        #return HttpResponse("hello")
