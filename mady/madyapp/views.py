from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def home(request, my_id, myname):
    if my_id == 1:
        name = "Gaurav"
    elif my_id == 2:
        name = "Rdx"
    elif my_id == 3:
        name = "aattif"
    else:
        name = "unknown"

    print(my_id)
    context = {"id": my_id, "name": name, "myname": myname}
    return render(request, 'dyapp/show.html', context)


def subhome(request, my_id, my_subid):
    print(my_id, my_subid)
    context = {"id": my_id, "subid": my_subid}
    return render(request, 'dyapp/show.html', context)


def superhome(request, my_id, my_subid, my_superid):
    print(my_id, my_subid, my_superid)
    context = {"id": my_id, "subid": my_subid, "superid": my_superid}
    return render(request, 'dyapp/show.html', context)


def show(request):
    return render(request, 'dyapp/links.html')


# Here we make our converter function

def converterpath(request, fivedigits):

    context = {"digits": fivedigits}
    return render(request, "dyapp/converter.html", context)
