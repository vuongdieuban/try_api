from django.urls import path
from .views import PostRudView

app_name = 'post_api'

urlpatterns = [
    path('<slug>/', PostRudView.as_view(), name='post-rud'),
]