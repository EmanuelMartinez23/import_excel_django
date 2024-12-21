from django.urls import path
from  .views import uploadView

urlpatterns = [
    path('', uploadView, name = 'upload')
]
