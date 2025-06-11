from rest_framework import serializers
from cv.models import CV, CVInfo


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"


class CVInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVInfo
        fields = "__all__"
