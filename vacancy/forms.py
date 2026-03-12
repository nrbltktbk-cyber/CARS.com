from django.forms import ModelForm
from .models import ITSecialist
from captcha.fields import CaptchaField
from django.forms import ModelForm
from .models import ITSecialist

class ITForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ITSecialist
        fields = '__all__'

class ITSpecialistForm(ModelForm):
    class Meta:
        model = ITSecialist
        fields = '__all__'