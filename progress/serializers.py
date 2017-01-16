""" Django REST Framework Serializers """

from progress.models import CourseModuleCompletion
from rest_framework import serializers


class CourseModuleCompletionSerializer(serializers.ModelSerializer):
    """ Serializer for CourseModuleCompletion model interactions """
    user_id = serializers.IntegerField(source='user.id')

    class Meta(object):
        """ Serializer/field specification """
        model = CourseModuleCompletion
        fields = ('id', 'user_id', 'course_id', 'content_id', 'stage', 'created', 'modified')
        read_only = ('id', 'created')
