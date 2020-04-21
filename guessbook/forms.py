from django import forms

class CommentForm(forms.Form):
	name = forms.CharField(
		widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name'}))
	comment = forms.CharField(widget = forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Comment'}))