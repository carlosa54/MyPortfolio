from rest_framework import serializers
from ..projects.models import Work, Project
from ..skills.models import Skill


class ProjectSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = Project
		fields = '__all__'

	def get_image(self, obj):
		return self.context['request'].build_absolute_uri(obj.images.first().image.url)

class ProjectDetailSerializer(serializers.ModelSerializer):
	images = serializers.StringRelatedField(many=True)
	class Meta:
		model = Project
		fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Work
		fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skill
		fields = '__all__'