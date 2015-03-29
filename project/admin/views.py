# -*- coding: utf-8 -*-
"""
admin.views
"""
from kay.utils import render_to_response

# Create your views here.


def index(request):
    return render_to_response('admin/index.html', {'message': 'Hello'})
