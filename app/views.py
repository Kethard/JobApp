from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from app.models import JobPost
from django.template import loader
# Create your views here.
job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]
job_description = [
    "First job desctription",
    "Second job description",
    "Third job description"
]
list = "<ul><li>Job 1</li><li>Job 2</li><li>Job 3</li></ul>"

'''def hello(request):
    job = "http://127.0.0.1:8000/job/1"
    return HttpResponse(f"<h3>Hello World</h3> <br>{list}")'''
class TempClass:
    x = 5
def job_list(request):
    job_list = JobPost.objects.all()
    context = {'jobs':job_list,}
    return render(request, 'app/job_list.html', context)
def job(request, id):
    try:
        job_list = JobPost.objects.get(id = id)
        if job_list.id == 0:
            return redirect(reverse('jobs_home'))
        #context={'jobs':job_list.title[job_list.id],'descriptions':job_list.description[job_list.id]}
        context={'job':job_list}
        return render(request,'app/job_det.html',context)
    except:
        return HttpResponseNotFound("<h2 align=center>Page Not Found</h2>")
def hello(request):
    temp = TempClass()
    is_auth = False
    lista = ['Jeden','Dwa','Trzy','Cztery','Pięć']
    context = {"name":'Django','age':'35','lista':lista,'isauth':is_auth,'tempobj':temp,'new_list':job_description[0]}

    return render(request, 'app/hello.html', context)