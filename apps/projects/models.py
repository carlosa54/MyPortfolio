# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.text import slugify

from django.db import models

def logo_upload_to(instance, filename):
	''' This function formats the filename of the Work logos'''
	slug = slugify(instance.pk)
	return "works/%s/%s" %(slug, filename)

class Work(models.Model):
	name = models.CharField(max_length=50)
	logo = models.ImageField(upload_to=logo_upload_to,blank=True,null=True)
	position = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
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
	github_url = models.URLField(blank=True, null=True)
	work = models.ForeignKey(Work, on_delete=models.SET_NULL, null=True, blank=True)
	personal = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title


def image_upload_to(instance, filename):
	''' This function formats the filename of the images of ProjectImage '''
	slug = slugify(instance.project.pk)
	return "projects/%s/%s" %(slug, filename)

class ProjectImage(models.Model):
	project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="images")
	image = models.ImageField(upload_to=image_upload_to)

	def __unicode__(self):
		return self.image.url