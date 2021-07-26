from django.urls import path

from profileapp.views import ProFileCreateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProFileCreateView.as_view(), name='create')
]