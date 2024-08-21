from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods


def articles(request):
    pass

def article_detail(request, pk):
    pass


@login_required
@require_http_methods(['POST', 'GET'])
def create(request):
    pass


@login_required
@require_http_methods(['POST', 'GET'])
def update(request):
    pass


@login_required
@require_POST
def delete(request, pk):
    pass


@require_POST
def comment_create(request, pk):
    pass


@require_POST
def comment_delete(request, pk, comment_pk):
    pass


@require_POST
def like(request, pk):
    pass