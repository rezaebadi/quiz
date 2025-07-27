from rest_framework import serializers
from .models import *
class BookSerializer(serializers.ModelSerializer):
    author_name=serializers.SerializerMethodField()

    class Meta:
        model=Book
        fields=("title","author","author_name")

    def get_author_name(self,obj):
        return obj.author.name