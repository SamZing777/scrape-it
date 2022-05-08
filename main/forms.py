from django import forms
from cloudinary.forms import CloudinaryJsFileField

from .models import Image


class ImageUploadForm(forms.ModelForm):
	file = CloudinaryJsFileField

	class Meta:
		model = Image
		fields = ['short_title', 'file']

	def save(self, user=None):
		upload = super(ImageUploadForm, self).save(commit=False)
		upload.save()
		return upload
