from django.shortcuts import render
from MyBlogs.models import userData,FAQs,polls,pollsData
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


def index(request):
    faqs = FAQs.objects.all()
    pol = polls.objects.all()
   
    return  render(request , 'index.html',{'faqs':faqs , 'pol':pol})

@csrf_exempt
def Submit(requset):
    if requset.method=='GET':
        name = requset.GET.get('name')
        email = requset.GET.get('email')
        discription = requset.GET.get('discription')
        data = userData(name=name, email=email,discription=discription)
        data.save()
    return  redirect('/')


def addPoll(reqest):
    
    if reqest.method=='GET':
        
        op = str(reqest.GET['flexRadioDefault'])
        polll = pollsData(selected_op = op)
        polll.save()
    return  redirect('/')


def search(request):
    if request.method == 'GET':
        faqsData = FAQs.objects.all()
        return render(request,'Faqs.html' , {'faqsData':faqsData})
        