from django.shortcuts import render, redirect
from MainApp.models import JobPost
from django.http import HttpResponseNotFound
# Create your views here.

def job_post(request):
    jobs = JobPost.objects.all()
    contexts = {'jobs': jobs}
    return render(request, 'mainapp/index.html', contexts)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('home'))
        job = JobPost.objects.get(id=id)
        print(job)
        contexts = {
            'job': job
        }
        return render(request, 'mainapp/job_detail.html', contexts)
    except:
        return HttpResponseNotFound('Not Found!')           