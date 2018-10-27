from .models import userdata, maidata, review, message
from django import forms
from .uid import _generate_maid_id
class Orderform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Orderform, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = True
    class Meta:
        worktype = (
            ("Replacement", "REPLACEMENT"),
            ("New Subscription", "NEW SUBSCRIPTION")
            )
        Language = (
        ("HINDI", "Hindi"),
        ("MARATHI", "MARATHI")
        )
        workt = forms.CharField(max_length=16,
                widget=forms.Select(choices=worktype))
        language = forms.CharField(max_length=8,
                widget=forms.Select(choices=Language))
        model = userdata
        fields = ['name', 'email', 'phone_number', 'worktype', 'language', 'address', 'city', 'zipcode']
        labels = {'name':'Name :', 'email':'Email', 'address':'Please enter a valid Address', 'phone_number':'Phone Number', 'city':'City', 'zipcode':'ZIP-CODE'}
        widgets = {'address': forms.Textarea(attrs={'cols': 80})}

class Maidform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['maidid'].initial = _generate_maid_id
    class Meta:
        model = maidata
        fields = ['name', 'phone_number', 'address', 'maidid','age','language']
        labels = {'name':'Name', 'address':'Please enter a valid Address', 'language':'Language', 'age':'Age', 'phone_number':'Phone Number', 'maidid':'Unique Maid ID'}
        widgets = {'address': forms.Textarea(attrs={'cols': 80})}

class Reviewform(forms.ModelForm):
    class Meta:
        model = review
        fields = ['name','code','email','review']
        labels = {'name':'Name','email':'Email','code':'Maid ID',}
        widgets = {'review': forms.Textarea(attrs={'cols': 80})}

class Messageform(forms.ModelForm):
    class Meta:
        model = message
        fields = ['name', 'email', 'message']
        labels = {'name':'Name','email':'Email','message':'Message'}
        widgets = {'review': forms.Textarea(attrs={'cols': 80})}
