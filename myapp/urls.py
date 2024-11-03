from django.urls import path
from .import views

urlpatterns = [
    path('',views.studentCreate,name='student_create'),
    path('git/',views.Studentget,name='student_create')
]
