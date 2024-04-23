# Create your views here.
from django.shortcuts import render, redirect
from .forms import MoveStudentsForm, DeleteStudentsForm
from apps.students.models import Student

def move_students(request):
    if request.method == 'POST':
        form = MoveStudentsForm(request.POST)
        if form.is_valid():
            from_class_id = form.cleaned_data['from_class'].id
            to_class_id = form.cleaned_data['to_class'].id
            # Move students from one class to another
            Student.objects.filter(current_class_id=from_class_id).update(current_class_id=to_class_id)
            return redirect('move_students_success')
    else:
        form = MoveStudentsForm()
    return render(request, 'move_students.html', {'form': form})

def delete_students(request):
    if request.method == 'POST':
        form = DeleteStudentsForm(request.POST)
        if form.is_valid():
            class_id = form.cleaned_data['class_to_delete'].id
            # Delete students from the given class
            Student.objects.filter(current_class_id=class_id).delete()
            return redirect('delete_students_success')
    else:
        form = DeleteStudentsForm()
    return render(request, 'delete_students.html', {'form': form})

def move_students_success(request):
    return render(request, 'move_students_success.html')

def delete_students_success(request):
    return render(request, 'delete_students_success.html')
