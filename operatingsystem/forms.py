from django.forms import ModelForm
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