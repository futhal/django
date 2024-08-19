from django.shortcuts import render

def meshcentral_view(request):
    return render(request, 'meshcentral.html')
