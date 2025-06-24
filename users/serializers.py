from rest_framework import serializers
from users.models import CustomUser, HR, Premium


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "name", "surname", "password")

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            name=validated_data["name"],
            surname=validated_data["surname"],
        )

        return user


class HRRegisterSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )

    class Meta:
        model = HR
        fields = (
            "user",
            "company_name",
            "company_nip",
            "telephone",
            "country",
            "city",
            "street",
            "number_street",
            "postcode",
        )

        def create(self, validated_data):

            user = validated_data.pop("user")
            if user:
                hr = HR.objects.create(
                    user=user,
                    company_name=validated_data["company_name"],
                    company_nip=validated_data["company_nip"],
                    telephone=validated_data["telephone"],
                    country=validated_data.get("country"),
                    city=validated_data["city"],
                    street=validated_data["street"],
                    number_street=validated_data["number_street"],
                    postcode=validated_data["postcode"],
                )
                user.hr_role = True
                user.save()
                return hr
            else:
                raise serializers.ValidationError(
                    "User with this email does not exist."
                )
