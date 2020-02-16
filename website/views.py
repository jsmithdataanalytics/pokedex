from django.http import HttpResponse

from website.models import Pokemon


def index(request):
    mons = Pokemon.objects.all().order_by('number')
    lines = [f'<li><a href="{mon.number}">{mon.name.upper()}</a></li>' for mon in mons]

    return HttpResponse(f'<html><body><h1>Pok\u00e9dex</h1><ol>{"".join(lines)}</ol></body></html>')


def profile(request, number):
    mon = Pokemon.objects.get(number=number)
    d = mon.__dict__
    lines = []

    d['primary_type'] = mon.primary_type.name
    d['secondary_type'] = mon.secondary_type.name if mon.secondary_type else 'none'

    del d['primary_type_id']
    del d['secondary_type_id']
    del d['_state']
    del d['id']

    order = ['number', 'name', 'primary_type', 'secondary_type',
             'height', 'weight', 'genus', 'description', 'image',
             'hp', 'attack', 'defense', 'special', 'speed']

    for key in order:
        lines.append(f'{key}: {str(d[key])}')

    return HttpResponse(f'<html><body>{"<br />".join(lines)}</body></html>')
