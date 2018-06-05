# from django import forms
# from .models import BasicUserInfo
#
#
# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = BasicUserInfo
#         fields = ('email',)
#
#     def save(self, commit=True):
#         print("there1")
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
