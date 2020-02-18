from django.shortcuts import render
from django.views import generic

from website.models import Pokemon


def home(request):
    return render(request, 'website/home.html')


class DexView(generic.ListView):
    template_name = 'website/dex.html'
    context_object_name = 'mon_list'

    def get_queryset(self):
        return Pokemon.objects.filter(name__startswith=self.request.GET.get('q', '')).order_by('number')


class ProfileView(generic.DetailView):
    model = Pokemon
    slug_field = 'number'
    slug_url_kwarg = 'number'
    template_name = 'website/profile.html'
