from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from .views import ProjectListAPIView, ProjectRetrieveAPIView, WorkListAPIView, WorkRetrieveAPIView, SkillListAPIView, SkillRetrieveAPIView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
	url(r'^projects/$', ProjectListAPIView.as_view() , name='projects_api'),
	url(r'^projects/(?P<pk>\d+)/$', ProjectRetrieveAPIView.as_view() , name='projects_detail_api'),
	url(r'^works/$', WorkListAPIView.as_view() , name='works_api'),
	url(r'^works/(?P<pk>\d+)/$', WorkRetrieveAPIView.as_view() , name='works_detail_api'),
	url(r'^skills/$', SkillListAPIView.as_view() , name='skills_api'),
	url(r'^skills/(?P<pk>\d+)/$', SkillRetrieveAPIView.as_view() , name='skills_detail_api'),
]
