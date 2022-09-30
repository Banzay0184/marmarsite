from django.http import HttpResponseRedirect
from django.views.generic import *
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.


class ProjectsListView(ListView):
    model = Projects
    template_name = 'projects_list.html'

    def get_queryset(self):
        return Projects.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PeojectsDetailView(DetailView):
    model = Projects
    context_object_name = 'project'
    slug_url_kwarg = 'project_slug'
    template_name = 'projects_detail.html'


def home(request):
    return render(request, 'base.html')


def index(request):
    projects = Projects.objects.all()
    employees = Employees.objects.all()
    reviews = Reviews.objects.all()
    partners = PartnersModel.objects.all()
    form = ConatactForms
    if request.method == 'POST':
        form = ConatactForms(request.POST)
        if form.is_valid():
            ContactModel.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        pass

    formtw = ReviewsForms
    if request.method == 'POST':
        formtw = ReviewsForms(request.POST)
        if formtw.is_valid():
            Reviews.objects.create(**formtw.cleaned_data)
            return redirect('index')
    else:
        pass

    return render(request, 'index.html', {"projects": projects,
                                          "form": form,
                                          "employees": employees,
                                          "formtw": formtw,
                                          "reviews": reviews,
                                          "partners": partners,
                                          })
