from django.shortcuts import render, get_object_or_404
from django.views import generic
from website.models import Pokemon


def index(request):
    mons = Pokemon.objects.all().order_by('number')

    return render(request, 'website/index.html', {'pokemon_list': mons})


class IndexView(generic.ListView):
    template_name = 'website/index.html'
    context_object_name = 'mon_list'

    def get_queryset(self):
        return Pokemon.objects.all().order_by('number')


class ProfileView(generic.DetailView):
    model = Pokemon
    slug_field = 'number'
    slug_url_kwarg = 'number'
    template_name = 'website/profile.html'
