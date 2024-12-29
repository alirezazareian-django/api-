from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def student_List(request):
    students=Student.objects.all()
    students_serialize=StudentSerializer(students,many=True)
    return Response(students_serialize.data)

@api_view(['GET'])
def student_Details(request,pk):
    student=Student.objects.get(id=pk) 
    student_serialize=StudentSerializer(student,many=False)
    return Response(student_serialize.data)

@api_view(['POST'])
def student_Save(request):
    student=StudentSerializer(data=request.data)

    if student.is_valid():
        student.save()

    return Response(student.data)    

@api_view(['POST'])
def student_Update(request,pk):
    instance=Student.objects.get(id=pk)
    student=StudentSerializer(instance=instance, data=request.data)

    if student.is_valid():
        student.save()

    return Response(student.data)  

@api_view(['DELETE'])  
def student_Delete(request,pk):
    instance=Student.objects.get(id=pk)
    instance.delete()

    return Response('Student Deleted!')





