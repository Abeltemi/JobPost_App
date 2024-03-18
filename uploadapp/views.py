from django.shortcuts import render
from .forms import UploadForm
# Create your views here.


def upload_image(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_object = form.instance
            return render(request, 'uploadapp/add_image.html', {'form': form, 'image_object':image_object})

    else:
        form = UploadForm()

    return render(request, 'uploadapp/add_image.html', {'form': form})