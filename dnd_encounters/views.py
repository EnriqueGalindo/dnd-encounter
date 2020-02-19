from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import NPCTraits


def npc_list(request):
    npcs = Post.objects.all()
    return render(request, "index.html", {"npcs": npcs})


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


def hp_up_1(request, id):
    post = Post.objects.get(id=id)
    post.hit_points += 1
    post.save()
    return redirect(reverse("home"))


def hp_up_10(request, id):
    post = Post.objects.get(id=id)
    post.hit_points += 10
    post.save()
    return redirect(reverse("home"))


def hp_down_1(request, id):
    post = Post.objects.get(id=id)
    post.hit_points -= 1
    post.save()
    return redirect(reverse("home"))


def hp_down_10(request, id):
    post = Post.objects.get(id=id)
    post.hit_points -= 10
    post.save()
    return redirect(reverse("home"))
