from django.shortcuts import render
from .models import Compound
from django.db.models import Q

def start_screen(request):
    return render(request, 'start.html')


def search(request):
    query = request.GET.get('q')
    compounds = Compound.objects.all()

    if query=="":
        return render(request, 'invalid.html')

    elif  query:
        compounds = compounds.filter(
            Q(formula__icontains=query)  |
            Q(name__icontains=query)
                                     ).distinct()
        compounds = {
            'compounds': compounds
        }
        return render(request, 'list.html', compounds)


def compound_details(request, compound_id):
    compound = Compound.objects.get(id=compound_id)
    compound = {
        'compound':compound
    }
    return render(request,'details.html', compound)

