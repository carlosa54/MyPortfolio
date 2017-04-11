# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, ProjectImage, Work

class ProjectImageInline(admin.TabularInline):
	model = ProjectImage
	extra = 0
	max_num = 10
	min_num = 1

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	inlines = [
		ProjectImageInline,
	]
	class Meta:
		model = Project

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Work)
