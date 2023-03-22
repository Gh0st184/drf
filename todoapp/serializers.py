from rest_framework.serializers import HyperlinkedModelSerializer

from todoapp.models import Project, ToDo


class ProjectSerializers(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializers(HyperlinkedModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'
