from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View


# логика при помощи класса View
class FeedBackView(View):
    def get(self, request):  # методы называются именно таким образом
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


# логика при помощи функций
# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             feed.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})

# логика при помощи класса View
class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')


# логика при помощи функций
#  def update_feedback(request, id_feedback):
#      feed = Feedback.objects.get(id=id_feedback)
#      if request.method == 'POST':
#          form = FeedbackForm(request.POST, instance=feed)
#          if form.is_valid():
#              form.save()
#              return HttpResponseRedirect('/done')
#      else:
#          form = FeedbackForm(instance=feed)
#      return render(request, 'feedback/feedback.html', context={'form': form})

# логика при помощи класса View
class DoneView(View):
    def get(self, request):
        return render(request, 'feedback/done.html')

# логика при помощи функций
# def done(request):
    # return render(request, 'feedback/done.html')
