from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import ShortURL
from .forms import ShortURLForm
import random
import string

from django.http import HttpResponse

def hello_world(request):
    return render(request, 'shortSnip/index.html')

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def create_short_url(request):
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']

            # Check if the URL already exists
            existing_url = ShortURL.objects.filter(original_url=original_url).first()

            if existing_url:
                # Handle the case where the URL already exists (e.g., redirect to existing short URL)
                return render(request, 'shortSnip/result.html', {'short_url': existing_url})

            short_code = generate_short_code()
            short_url = ShortURL(original_url=original_url, short_code=short_code)
            short_url.save()
            return render(request, 'shortSnip/result.html', {'short_url': short_url})
    else:
        form = ShortURLForm()
    return render(request, 'shortSnip/create.html', {'form': form})


def redirect_to_original(request, short_code):
    try:
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return redirect(short_url.original_url)
    except Exception:
        raise Http404("Short URL does not exist")
