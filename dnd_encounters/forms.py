from django import forms


class NPCTraits(forms.Form):
    name = forms.CharField()
    hit_points = forms.IntegerField()
    armor_class = forms.IntegerField()
    resistances = forms.CharField()
    immunities = forms.CharField()
    speed = forms.IntegerField()
