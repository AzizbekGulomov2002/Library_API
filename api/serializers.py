from pyexpat import model
from rest_framework import serializers
from library.models import Kitob

class KitobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitob
        fields = ('nomi','kitob_haqida','muallif','janr','isbn','narx')