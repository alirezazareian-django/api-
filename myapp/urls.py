from django.urls import path
from .views import student_List, student_Details, student_Save, student_Update,student_Delete

urlpatterns=[
    path('student_List/',student_List),
    path('student_details/<pk>/',student_Details),
    path('student_save/', student_Save),
    path('student_update/<pk>/', student_Update),
    path('student_delete/<pk>/', student_Delete),

]