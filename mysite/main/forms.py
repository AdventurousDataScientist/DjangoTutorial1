from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)

class AddItem(forms.Form):
    name = forms.CharField(label="Item", max_length=500)
    complete = forms.BooleanField(label="Complete", required=False)
