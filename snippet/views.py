from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import SnippetForm, DecryptForm
from django.urls import reverse


def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            return redirect('snippet:snippet_detail', pk=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, 'snippet/create_snippet.html', {'form': form})


def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)

    decrypted_content = None
    key_error = False

    if request.method == 'POST':
        decrypt_form = DecryptForm(request.POST)
        if decrypt_form.is_valid():
            key = decrypt_form.cleaned_data['key']

            if key == snippet.key:
                decrypted_content = snippet.original_content
            else:
                key_error = True
    else:
        decrypt_form = DecryptForm()

    return render(request, 'snippet/snippet_detail.html', {
        'snippet': snippet,
        'decrypted_content': decrypted_content,
        'key_error': key_error,
        'decrypt_form': decrypt_form,
    })