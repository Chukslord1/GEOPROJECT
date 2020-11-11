from django.shortcuts import render
from  APP.models import UserProfile
from django.contrib.gis.measure import D
from django.db.models import Q



# Create your views here.
def index(request):
    school = UserProfile.objects.first()
    #Assume first object is required School


    close_by=UserProfile.objects.filter(geo_location__distance_lte=(school.geo_location, D(m=100)))
    #query for school 10 metres from

    mid_distance=UserProfile.objects.filter(geo_location__distance_lte=(school.geo_location, D(mi=10)))
    #query for school 10 miles  from you

    far=UserProfile.objects.filter(geo_location__distance_lte=(school.geo_location, D(km=10)))
    #query for school 10 kilmetres from you

    within_range=UserProfile.objects.filter(Q(geo_location__distance_gte=(school.geo_location, D(km=5)))
        & Q(geo_location__distance_lte=(school.geo_location, D(km=10))))
    #query for school within a distance of 5km to 10km

    context={"close_by":close_by,"mid_distance":mid_distance,"far":far,"within_range":within_range}
    return render(request,"index.html",context)
