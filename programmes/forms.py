from django import forms
from .models import Programme


class ProgrammeForm(forms.ModelForm):

    class Meta:
        model = Programme
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
