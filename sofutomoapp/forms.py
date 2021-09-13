from django import forms
from .models import GuestModel

sex={
    ('男性','男性'),
    ('女性','女性')
}
ch = (
    ("大阪市", "大阪市"),
    ("堺市", "堺市"),
    ("能勢町", "能勢町"),
    ("", "フランス"),
    ("de", "ドイツ"),
)

class RegisterForm(forms.Form):

    email = forms.EmailField(
        label='メールアドレス', 
        required=True    
    )

    gender = forms.ChoiceField(
        label='性別',
        widget=forms.RadioSelect,
        choices=sex, 
        required=True
        )
    age = forms.IntegerField(
        label='年齢',
        required=True
    )
    #image = forms.ImageField()


class HostForm(forms.Form):

    event_date = forms.SplitDateTimeField(
        label='開催日時',
        widget=forms.SplitDateTimeWidget(date_attrs={"type":"date"}, time_attrs={"type":"time"}),
        required=True
        )
    member = forms.IntegerField(
        label='人数',
        required=True
    )
    location = forms.ChoiceField(
        label='location',
        choices=ch,
        required=True
    )
"""
class RegisterForm(forms.ModelForm):
    class Meta:
        model = GuestModel
        fields = ['gender','image','age','email']
"""

class ImageForm(forms.Form):
    image = forms.ImageField()