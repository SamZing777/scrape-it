from django.urls import path

from .views import (
	ImageUploadView,
	# ImageConversionView
	)


urlpatterns = [
	path('', ImageUploadView.as_view(), name='index')
]
