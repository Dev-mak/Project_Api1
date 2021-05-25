from django.urls import path
from .views import *

urlpatterns = [
    path('api/student/', Detail_ListCreateView.as_view()),
    path('api/student/add-mark', Mark_ListCreateView.as_view()),
    path('api/student/result', ResultOnCategory.as_view())

]