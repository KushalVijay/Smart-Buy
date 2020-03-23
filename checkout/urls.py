from django.conf.urls import url
from .views import checkout,payment

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^payment/', payment, name='payment'),
]