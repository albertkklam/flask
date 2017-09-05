from django.forms import ModelForm
from wines.models import Wine, User

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ('user','name','colour','year','grape','region_country','price','abv','description','mode_rating','winner',)