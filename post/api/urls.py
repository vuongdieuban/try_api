from django.urls import path
from .views import PostRudView, PostAPIView

app_name = 'post_api'

urlpatterns = [
    path('', PostAPIView.as_view(), name='post-create'),
    path('<slug>/', PostRudView.as_view(), name='post-rud'),

]