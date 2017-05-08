from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Game
from django import forms
from .forms import GameForm

# Create your views here.


#view for seeing all games
def game_list(request):
    games = Game.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'code_games/game_list.html', {'games': games})


#view for seeing/playing an individual game
def game_single(request, pk):
    games = get_object_or_404(Game, pk=pk)
    return render(request, 'code_games/game_single.html', {'games': games})

#view for adding a new game
def game_new(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('game_single', pk=post.pk)
    else:
        form = GameForm()
    return render(request, 'code_games/game_new.html', {'form': form})
