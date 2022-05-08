from django.views import generic
from django.urls import	reverse_lazy

from .models import Image
from .forms import ImageUploadForm


class ImageUploadView(generic.CreateView):
	form_class = ImageUploadForm
	success_url = reverse_lazy('index')
	template_name = 'main/image_upload.html'

	def form_valid(self, form):
		return super().form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(ImageUploadView, self).get_context_data(*args, **kwargs)
		context['file_uploaded'] = Image.objects.all()
		# context['file_uploaded'] = Image.objects.get(id=0)
		return context

"""
class ImageConversionView(generic.ListView):
	model = Image
	context_object_name = 'upload_file'
	template_name = 'main/convert.html'
"""
