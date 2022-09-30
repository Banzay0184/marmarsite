from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models


class ProjectImageInline(admin.StackedInline):
    model = models.ProjectImage


@admin.register(models.Projects)
class ProjectsAmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'id']
    inlines = [ProjectImageInline]
    save_as = True
    save_on_top = True


@admin.register(models.ContactModel)
class ContactModeladmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'numbers', 'create_at']
    list_display_links = ("name",)


admin.site.register(models.CategoryProjects, MPTTModelAdmin)
admin.site.register(models.Reviews)
admin.site.register(models.ProjectImage)
admin.site.register(models.Employees)
admin.site.register(models.PartnersModel)