from django.urls import path, re_path
from django.views.generic import DetailView,ListView
from linkler.models import link
from .views import linklerim

urlpatterns = [
    path('', ListView.as_view(queryset=link.objects.all().order_by("-tarih"),
                              template_name='linkler/linkler.html')),
    path('linklerim/', linklerim),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=link,
                                                 template_name='linkler/link.html'),name='link_detail'),
    ]
