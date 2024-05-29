from django.shortcuts import render
from .models import Student
# Create your views here.
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

def home(request):
    student_objs = Student.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(student_objs,2)
    try:
        student_objs = paginator.page(page)
    except PageNotAnInteger:
        student_objs = paginator.page(1)
    except EmptyPage:
        student_objs = paginator.page(paginator.num_pages)
    context = {
        'student_objs':student_objs
    }
    return render(request,'home.html',context)
