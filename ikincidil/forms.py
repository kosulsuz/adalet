from django import forms
from .models import ContactInfo

from crispy_forms.helper import FormHelper


class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactInfo
		fields = ('name', 'email', 'topic', 'content',)
		
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder']= "Your Name"
		self.fields['name'].widget.attrs['class']= "form-control-sm"
		self.fields['email'].widget.attrs['placeholder']= "Email"
		self.fields['email'].widget.attrs['class']= "form-control-sm"
		self.fields['topic'].widget.attrs['class']= "form-control-sm"
		self.fields['topic'].widget.attrs['placeholder']= "Topic"
		self.fields['content'].widget.attrs['class']= "form-control-sm"
		self.fields['content'].widget.attrs['placeholder']= "Message"
		self.helper = FormHelper()
		self.helper.form_show_labels = False 