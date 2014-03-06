from django import forms
from django.forms import extras
import datetime
from django.forms.extras.widgets import SelectDateWidget

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()


class HomePageSearch(forms.Form):
    sportName = forms.ChoiceField(label='Sport name')
    sportArea = forms.CharField(label='Area name',widget=forms.TextInput(attrs={'class': 'home_choose_area'}))
    date = forms.DateField(widget=extras.SelectDateWidget(attrs={'class' : 'home_choose_date'}),initial=datetime.date.today)
