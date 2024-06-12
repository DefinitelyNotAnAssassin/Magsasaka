from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, When, Case, Value, CharField
from UserAuthentication.models import Account
import json



def barangay_data(request):
    data = {}

    # Get the top 10 barangays with the most registered users
    barangays = Account.objects.values('barangay').annotate(count=Count('barangay')).order_by('-count')[:10]

    for barangay in barangays:
        # Ensure the key is a string
        key = str(barangay['barangay'])
        data[key] = barangay['count']

    print(data)
    return JsonResponse(json.dumps(data), safe=False)



def age_data(request):
    data = {}

    # Define age groups using conditional expressions
    age_groups = Case(
        When(age__lt=18, then=Value('Under 18')),
        When(age__range=(18, 24), then=Value('18-24')),
        When(age__range=(25, 34), then=Value('25-34')),
        When(age__range=(35, 44), then=Value('35-44')),
        When(age__range=(45, 54), then=Value('45-54')),
        When(age__range=(55, 64), then=Value('55-64')),
        When(age__gte=65, then=Value('65 and over')),
        output_field=CharField(),
    )

    # Get the age distribution of registered users
    ages = Account.objects.annotate(age_group=age_groups).values('age_group').annotate(count=Count('age_group')).order_by('age_group')

    for age in ages:
        # Ensure the key is a string
        key = str(age['age_group'])
        if key == "None":
            continue
        data[key] = age['count']
    print(data)
    return JsonResponse(json.dumps(data), safe=False)



def family_voters_data(request):
    data = {}

    # Define voter groups using conditional expressions
    voter_groups = Case(
        When(family_voters_count=1, then=Value('1')),
        When(family_voters_count__range=(2, 5), then=Value('2-5')),
        When(family_voters_count__gte=5, then=Value('5 or more')),
        output_field=CharField(),
    )

    # Get the distribution of family voters
    voters = Account.objects.annotate(voter_group=voter_groups).values('voter_group').annotate(count=Count('voter_group')).order_by('voter_group')

    for voter in voters:
        # Ensure the key is a string
        key = str(voter['voter_group'])
        if key == "None":
            continue
        data[key] = voter['count']

    return JsonResponse(json.dumps(data), safe=False)


def get_locations(request): 
    # get the longitude and latitude of each user 

    data = []
    locations = Account.objects.values('longitude', 'latitude')

    for location in locations:
        if location['longitude'] is not None and location['latitude'] is not None:
            data.append(location)

    return JsonResponse(data, safe=False)