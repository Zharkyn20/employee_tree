from django.urls import path

from tree.views import index

urlpatterns = [path("", index, name="index")]
