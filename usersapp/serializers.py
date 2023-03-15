from rest_framework.serializers import HyperlinkedModelSerializer

from usersapp.models import MyCustomUser


class MyCustomUserSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = MyCustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
