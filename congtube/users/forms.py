from django import forms
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm


class CustomSignupForm(SignupForm):
    agree_terms = forms.BooleanField(label='서비스 이용약관 및 개인정보방침 동의', required=True)
    agree_marketing = forms.BooleanField(label='마케팅 이용 동의', required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.agree_terms = self.cleaned_data['agree_terms']
        user.agree_marketing = self.cleaned_data['agree_marketing']
        user.save()
        return user


class SocialSignupForm(SocialSignupForm):
    password1 = forms.CharField(max_length=30, label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, label="Password(again)", widget=forms.PasswordInput)
    agree_terms = forms.BooleanField(label='서비스 이용약관 및 개인정보방침 동의', required=True)
    agree_marketing = forms.BooleanField(label='마케팅 이용 동의', required=False)

    def save(self, request):
        user = super(SocialSignupForm, self).save(request)
        user.password1 = self.cleaned_data['password1']
        user.password1 = self.cleaned_data['password2']
        user.agree_terms = self.cleaned_data['agree_terms']
        user.agree_marketing = self.cleaned_data['agree_marketing']
        user.save()
        return user