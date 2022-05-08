from django.db import models
from cloudinary.models import CloudinaryField


class Image(models.Model):
	short_title = models.CharField(max_length=20)
	file = CloudinaryField('image',
	         default="https://cdn.pixabay.com/photo/2016/06/16/03/49/befall-the-earth-quote-1460570_960_720.jpg")
	timeStamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.short_title
