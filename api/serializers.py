from rest_framework.serializers import ModelSerializer

from wiki.models import Page

class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

# class ChoiceSerializer(ModelSerializer):
#     class Meta:
#         model = Choice
#         fields = '__all__'
