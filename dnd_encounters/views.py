from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import NPCTraits


def npc_traits(request):
    html = "genericForm.html"
    if request.method == "POST":
        form = NPCTraits(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                name=data["name"],
                hit_points=data["hit_points"],
                armor_class=data["armor_class"],
                resistances=data["resistances"],
                immunities=data["immunities"],
                speed=data["speed"]
            )
            return redirect(reverse("home"))

    form = NPCTraits()
    return render(request, html, {'form': form})


def npc_list(request, id):
    npcs = NPCTraits.objects.get(id=id)
    return render(request, "index.html", {"npcs": npcs})