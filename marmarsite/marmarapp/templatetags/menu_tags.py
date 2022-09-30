from django import template
from marmarapp.models import *

register = template.Library()


# @register.simple_tag()
# def get_categories():
#     return CategoryProjects.objects.all()

@register.inclusion_tag('include/tags/top_menu.html')
def get_categories():
    project = CategoryProjects.objects.all()
    # filter(parent__isnull=True).order_by("name")
    return {"list_project": project}
