from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, HR


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "name", "surname", "hr_role", "premium_role")

    company_name = forms.CharField(required=False)
    company_nip = forms.CharField(required=False)
    telephone = forms.CharField(required=False)
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)
    number_street = forms.CharField(required=False)
    postcode = forms.CharField(required=False)

    def save(self, commit=True):
        user = super().save(commit)
        if user.hr_role:
            hr_instance = HR(
                user=user,
                company_name=self.cleaned_data["company_name"],
                company_nip=self.cleaned_data["company_nip"],
                telephone=self.cleaned_data["telephone"],
                city=self.cleaned_data["city"],
                street=self.cleaned_data["street"],
                number_street=self.cleaned_data["number_street"],
                postcode=self.cleaned_data["postcode"],
            )
            if commit:
                hr_instance.save()
        return user
