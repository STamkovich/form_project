from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery
from django.views.generic import CreateView, TemplateView, ListView


# в случае если не использовать модель
# def storage_file(file):
#     with open('gallery_tmp/new_image.jpg', 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)


class GalleryView(CreateView):
    model = Gallery
    form_class = GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = 'done_form'


# class GalleryView(View):
#
#     def get(self, request):
#         form = GalleryUploadForm()
#         return render(request, 'gallery/load_file.html', {'form': form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # storage_file(form.cleaned_data['image'])
#             new_image = Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/load_file.html', {'form': form})

#  Gallery.objects.all().image.read() посмотреть файл в байтах через калькулятор

class ListImages(ListView):
    template_name = 'gallery/list_image.html'
    model = Gallery
    context_object_name = 'records'


class DoneFormView(TemplateView):
    template_name = 'gallery/done_form.html'
