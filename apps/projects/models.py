# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.text import slugify

from django.db import models

# Create your models here.
class Work(models.Model):
	name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	from_date = models.DateField(null=False)
	to_date = models.DateField(null=True, blank=True)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

	def __unicode__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	url = models.URLField(blank=True, null=True)
	work = models.OneToOneField(Work, on_delete=models.CASCADE, primary_key=True,)
	personal = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title


def image_upload_to(instance, filename):
	''' This function formats the filename of the images of ProjectImage '''
	title = instance.project.title
	slug = slugify(title)
	# Takes the second element of the list returned by the split function
	file_extension = filename.split(".")[1] 
	new_filename = "%s.%s" %(instance.id, file_extension)
	return "projects/%s/%s" %(slug, new_filename)

class ProjectImage(models.Model):
	project = models.ForeignKey(Project)
	image = models.ImageField(upload_to=image_upload_to)

	def __unicode__(self):
		return self.project.title