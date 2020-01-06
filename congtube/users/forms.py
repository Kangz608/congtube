from django import forms
from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):
    agree_terms = forms.BooleanField(label='서비스 이용약관 및 개인정보방침 동의', required=True)
    agree_marketing = forms.BooleanField(label='마케팅 이용 동의', required=False)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.agree_terms = self.cleaned_data['agree_terms']
        user.agree_marketing = self.cleaned_data['agree_marketing']
        user.save()
        return user
