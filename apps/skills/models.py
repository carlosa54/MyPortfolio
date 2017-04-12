# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
class Skill(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True,null=True)
	level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	project = models.ManyToManyField(Project)
	skill_type = models.CharField(choices=SKILL_TYPE_CHOICES, max_length=2)

