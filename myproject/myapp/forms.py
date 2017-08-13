from django import forms

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = Dreamreal.objects.filter(name = username)
      
      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      return username