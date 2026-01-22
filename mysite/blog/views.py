from django.shortcuts import render, get_object_or_404
from .models import Horse

# Create your views here.
def horse_list(request):
    horses  = Horse.objects.all()
    return render (
        request,
        'blog/horse/list.html',
        {'horses' : horses}
         
    )
def horse_detail(request, id):
    horse = get_object_or_404(Horse, id=id)
    return render (
        request,
        'blog/horse/detail.html',
        {'horse': horse}
    )