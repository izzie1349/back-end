from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from basic_app import models

# # Create your views here.
# def index(request):
#     return render(request, 'index.html')


# # class based view
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("class based views are cool!")


# template view
class IndexView(TemplateView):
    template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION'
#         return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # school_view

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School
