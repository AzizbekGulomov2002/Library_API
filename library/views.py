from django.shortcuts import render

from django.views.generic import ListView

from .models import Kitob

class KitobListView(ListView):
    model = Kitob
    template_name = 'kitoblar/kitob_list.html'
