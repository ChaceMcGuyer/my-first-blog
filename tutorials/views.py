from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Tutorials
from django import forms
from .forms_tutorial import TutorialsForm

# Create your views here.

# View for the tutorial landing page
def tutorial_landing(request):
    tutorials = Tutorials.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'tutorials/tutorial_landing.html', {'tutorials': tutorials})

# Detailed view of an individual tutorial
def tutorial_detail(request, pk):
    tutorial = get_object_or_404(Tutorials, pk=pk)
    return render(request, 'tutorials/tutorial_detail.html', {'tutorial': tutorial})

# View to create a new tutorial
def tutorial_new(request):
    if request.method == "POST":
        form = TutorialsForm(request.POST,)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.author = request.user
            tutorial.published_date = timezone.now()
            tutorial.save()
            return redirect('tutorial_detail', pk=tutorial.pk)
    else:
        form = TutorialsForm()
    return render(request, 'tutorials/tutorial_edit.html', {'form': form})

# View to edit an existing tutorial
def tutorial_edit(request, pk):
    tutorial = get_object_or_404(Tutorials, pk=pk)
    if request.method == "POST":
        form = TutorialsForm(request.POST, instance=post)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.author = request.user
            tutorial.published_date = timezone.now()
            tutorial.save()
            return redirect('tutorial_detail', pk=tutorial.pk)
    else:
        form = TutorialsForm(instance=tutorial)
    return render(request, 'tutorials/tutorial_edit.html', {'form': form})
