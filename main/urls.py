from django.urls import path, include
from rest_framework import routers
from .views import StudentInfoView

app_name = 'student'

router = routers.DefaultRouter()
router.register('student', StudentInfoView)

urlpatterns = [
    path('', include(router.urls)),
]
