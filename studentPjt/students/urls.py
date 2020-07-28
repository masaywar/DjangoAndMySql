from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('reg/', views.register_student, name='reg'),
    path('regCon/', views.register_confirm, name='regCon'),
    path('all/', views.read_all_students, name='stuAll'),
    path('<str:name>/detail/', views.show_student_detail, name='det'),
    # path('mod/', views.read_student, name='mod'),
]
