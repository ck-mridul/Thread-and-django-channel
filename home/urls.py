from django.urls import path
from .views import home,generate_student_data

urlpatterns = [
    path('', home),
    path('student/',generate_student_data)
]