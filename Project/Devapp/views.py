from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from .serializers import Detail_Serializers, Mark_Serializers
from rest_framework.response import Response
from .models import Detail, Mark
from rest_framework.views import APIView

# Create your views here.
#task-1:-
class Detail_ListCreateView(generics.ListCreateAPIView):
    """
        url : /api/student,
        Method : GET, POST
    """
    queryset = Detail.objects.all()
    serializer_class = Detail_Serializers

#task-2:
class Mark_ListCreateView(generics.ListCreateAPIView):
    """
        url : /api/student/add-mark,
        Method : GET, POST
    """

    queryset = Mark.objects.all()
    serializer_class = Mark_Serializers

#task-3:
class ResultOnCategory(APIView):
    def get(self, request):
        """
            url : /api/student/result
            Method : GET
        """
        records = Detail.objects.all()
        total_no_of_students = len(records)

        grade_A = Mark.objects.filter(mark__range=[91, 100])
        students_with_Grade_A = len(grade_A)
        grade_B = Mark.objects.filter(mark__range=[81, 90])
        students_with_Grade_B = len(grade_B)
        grade_C = Mark.objects.filter(mark__range=[71, 80])
        students_with_Grade_C = len(grade_C)
        grade_D = Mark.objects.filter(mark__range=[61, 70])
        students_with_Grade_D = len(grade_D)
        grade_E = Mark.objects.filter(mark__range=[55, 61])
        students_with_Grade_E = len(grade_E)
        grade_F = Mark.objects.filter(mark__range=[0, 54])
        students_with_Grade_F = len(grade_F)

        distinction = round((students_with_Grade_A / total_no_of_students), 3)

        firstClass = round(((students_with_Grade_B + students_with_Grade_C) / total_no_of_students), 3)

        passClass = (total_no_of_students - students_with_Grade_F) / total_no_of_students

        response = {
            'total_no_of_students' : total_no_of_students,
            'total_no_of_students_with_Grade-A' :students_with_Grade_A,
            'total_no_of_students_with_Grade-B' :students_with_Grade_B,
            'total_no_of_students_with_Grade-C' :students_with_Grade_C,
            'total_no_of_students_with_Grade-D' :students_with_Grade_D,
            'total_no_of_students_with_Grade-E' :students_with_Grade_E,
            'total_no_of_students_with_Grade-F' :students_with_Grade_F,

            'distinction %' : distinction,
            'first Class %' : firstClass,
            'pass Class %'  : passClass
        }

        return Response(response, status=status.HTTP_200_OK)
