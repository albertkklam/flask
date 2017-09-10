from django.forms import ModelForm
from wines.models import Wine, User

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ('name','colour','year','grape','region','price','abv','description','mode_rating','winner',)