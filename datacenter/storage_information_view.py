from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)

    for visit in non_closed_visits:
        duration = Visit.get_duration(visit)
        
        visit.duration = Visit.format_duration(visit, duration)
        visit.is_strange = Visit.is_visit_long(visit, duration) 

    context = {
        "non_closed_visits": non_closed_visits,   # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
