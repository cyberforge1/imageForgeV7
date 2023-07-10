from django.shortcuts import render
from .models import Prompt, Image
from django.contrib.auth.decorators import login_required
from django.http import Http404


def prompt(request):
    '''Show all prompts'''
    prompt = Prompt.objects.all()
    context = {'prompt': prompt}
    return render(request, 'imageGeneration/prompt.html', context)

@login_required
def image(request):
    '''Show all images'''
    image = Image.objects.filter(owner=request.user).order_by('datetime_field')

    image = list(reversed(image))
    context = {
        'image': image,
    }
    return render(request, 'imageGeneration/image.html', context)


def gallery(request):
    '''Show the gallery'''
    gallery = Image.objects.all().order_by('datetime_field')
    gallery = list(reversed(gallery))
    context = {
        'gallery': gallery,
    }
    return render(request, 'imageGeneration/gallery.html', context)