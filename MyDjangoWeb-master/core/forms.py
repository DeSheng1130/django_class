from django.forms import ModelForm


class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '請輸入{}'.format(self.fields[field].label)
            })
