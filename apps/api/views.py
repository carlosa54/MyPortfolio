# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics, filters
from ..projects.models import Project, Work
from ..skills.models import Skill
from .serializers import ProjectSerializer, ProjectDetailSerializer, WorkSerializer, SkillSerializer

# Create your views here.
class ProjectListAPIView(generics.ListAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	ordering_fields = ["title", "pk"]

class ProjectRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectDetailSerializer

class WorkListAPIView(generics.ListAPIView):
	queryset = Work.objects.all()
	serializer_class = WorkSerializer
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	ordering_fields = ["name", "pk"]

class WorkRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Work.objects.all()
	serializer_class = WorkSerializer

class SkillListAPIView(generics.ListAPIView):
	queryset = Skill.objects.all()
	serializer_class = SkillSerializer
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	ordering_fields = ["name", "pk"]

class SkillRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Skill.objects.all()
	serializer_class = SkillSerializer