from django.forms import ModelForm, CharField, Textarea, EmailField

from .models import Consulta


class ConsultaForm(ModelForm):
    required_css_class = 'required-field'
    use_required_attribute: bool = True

    name = CharField(required=True, max_length=120)
    description = CharField(required=True)
    email = EmailField(required=True, max_length=2000)

    class Meta:
        model = Consulta
        fields = '__all__'
