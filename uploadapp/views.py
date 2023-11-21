from django.shortcuts import render, redirect
from uploadapp.forms import UploadForm, UploadFileForm
from django.urls import reverse

from uploadapp.models import UploadFile


# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            saved_object=form.instance
            return render(request, 'uploadapp/add_image.html', {'form': form,'saved_obj':saved_object})
    else:
        form=UploadForm()
    return render(request,'uploadapp/add_image.html',{'form':form})
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object=form.instance
            return render(request, 'uploadapp/add_file.html', {'form': form,'saved_obj':saved_object})
    else:
        form=UploadFileForm()
    return render(request,'uploadapp/add_file.html',{'form':form})
def thank_page(request):
    context={}
    return render(request, 'uploadapp/thank.html',context)