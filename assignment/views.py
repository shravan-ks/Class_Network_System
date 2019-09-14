from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from assignment.forms import assignsol
from assignment.models import assignment, AssignmentAns

@login_required
def assignQ(request):
    assign = assignment.objects.all()
    return render(request, 'assignment/assign.html', {'assign':assign})

@login_required
def assignview(request, id):
    assignview = assignment.objects.filter(id=id)
    return render(request, 'assignment/assignview.html', {'assignview':assignview})
@login_required
def compose(request):
    form = assignsol(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('assignQ')
    return render(request, 'assignment/compose.html', {'form': form})
@login_required
def sent(request):
    assignsent = AssignmentAns.objects.all()
    return render(request, 'assignment/sent.html', {'assignsent':assignsent})
@login_required
def sentview(request, id):
    sentView = AssignmentAns.objects.filter(id=id)
    return render(request, 'assignment/sentview.html', {'sentView':sentView})