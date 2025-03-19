from django.urls import path
from . import views
urlpatterns = [
    path('',views.StudentCources.as_view(), name='cource'),
    # path('student-auth/',views.StudentAuth.as_view(), name='student')
]
