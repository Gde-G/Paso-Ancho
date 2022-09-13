from django.forms import ModelForm, CharField, Textarea, EmailField, DateField, IntegerField

from .models import Consulta


class ConsultaForm(ModelForm):
    required_css_class = 'required-field'
    use_required_attribute: bool = True

    name = CharField(required=True, max_length=120)
    description = CharField(required=True)
    email = EmailField(required=True, max_length=2000)
    date_from = DateField(required=True,input_formats=['%d/%m/%Y %H:%M'])
    date_to = DateField(required=True, input_formats=['%d/%m/%Y %H:%M'])
    amount_adults = IntegerField(required=True)
    amount_kids = IntegerField(required=True)

    class Meta:
        model = Consulta
        fields = '__all__'
