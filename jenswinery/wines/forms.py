from django.forms import ModelForm
from wines.models import Wine, User

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ('name', 'description',)