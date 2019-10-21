from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = Visit.objects.filter(passcard=passcard)

    for visit in this_passcard_visits:
        duration = Visit.get_duration(visit)
        
        visit.duration = Visit.format_duration(visit, duration)
        visit.is_strange = Visit.is_visit_long(visit, duration)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
