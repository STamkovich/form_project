from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView  # в случае если нужно вывести только шаблон
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView


# логика при помощи класса CreateView
class FeedBackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'


# логика при помощи класса FormView
# class FeedBackView(FormView):
#     form_class = FeedbackForm
#     template_name = 'feedback/feedback.html'
#     success_url = '/done'
#
#     def form_valid(self, form):
#         form.save()
#         return super(FeedBackView, self).form_valid(form)


# логика при помощи класса View
# class FeedBackView(View):
#     def get(self, request):  # методы называются именно таким образом
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})


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


class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedback'

    def get_queryset(self):  # при помощи этого метода можно как-то отфильтровать наши данные
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__gt=2)
        return filter_qs


# логика при помощи класса DetailView
class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    context_object_name = 'feedback'


# логика при помощи класса UpdateView
class FeedBackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'


# логика при помощи класса View
# class FeedBackUpdateView(View):
#     def get(self, request, id_feedback):
#         feed = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(instance=feed)
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request, id_feedback):
#         feed = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')


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

# логика при помощи класса TemplateView
class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    # что бы передать данные можно воспользоваться специальными методами этого шаблона
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I.I.'
        context['date'] = '22.07.2022'
        return context
# логика при помощи функций
# def done(request):
#   return render(request, 'feedback/done.html')
