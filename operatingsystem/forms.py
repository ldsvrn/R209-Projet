from django.forms import ModelForm, Form, MultipleChoiceField, CharField, DateField, NumberInput
from django.utils.translation import gettext_lazy as _
from . import models

class OSForm(ModelForm):
    class Meta:
        model = models.operatingsystem
        fields = ('name', 'developer', 'software_license')
        labels = {
            'name' : _('Nom'),
            'developer' : _('Développeur') ,
            'software_license' : _('License')
        }

class VersionForm(Form):
    operating_system = MultipleChoiceField(choices=[(c.id,c.name) for c in models.operatingsystem.objects.all()])
    name = CharField(max_length = 100)
    release_date = DateField(widget=NumberInput(attrs={'type': 'date','id':'datepick'}))
    platform = CharField(max_length = 100)