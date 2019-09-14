from django.shortcuts import render

# Create your views here.
def student_data(request):
    return render(request, 'student/student_data.html')