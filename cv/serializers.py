from rest_framework import serializers
from cv.models import CV, CVInfo, Contact
from users.models import CustomUser


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"

    def to_representation(self, instance):
        user = self.context.get('request').user
        data = super().to_representation(instance)

        request = self.context.get('request')
        if request and request.method == "GET" and hasattr(user,"hr_role") and not user.hr_role and not user.is_staff:
            raise serializers.ValidationError("You do not have a HR role.")
        else:
            return data
        
    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user if request else None

        if request and request.method == "POST":
            if hasattr(user,"premium_role") and not user.premium_role:
                cv_count = CV.objects.filter(user_id=user.id).count()
                if cv_count >= 1:
                    raise serializers.ValidationError("You reach the limit for free account.")
        return attrs
        
        



class CVInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVInfo
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
