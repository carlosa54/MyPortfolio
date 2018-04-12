# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from ..projects.models import Project

# Create your models here.
# Skill Type constants
SKILL_TYPE_CHOICES = (
	('TH','Technology'),
	('PL','Programming Language'),
	('OS','Operating System'),
	('ST','Software Tool'),
	('FR','Framework'),
)

def image_upload_to(instance, filename):
	''' This function formats the filename of the images of the Skill model '''
	slug = slugify(instance.pk)
	return "skills/%s/%s" %(slug, filename)

class Skill(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True,null=True)
	level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	skill_type = models.CharField(choices=SKILL_TYPE_CHOICES, max_length=2)
	image = models.ImageField(upload_to=image_upload_to,blank=True,null=True)

	def __unicode__(self):
		return self.name + ": " + self.get_skill_type_display()

