from django.urls import path
from polls.views import index, detail, vote, results

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
    path('<int:id>/vote', vote, name='vote'),
    path('<int:id>/results', results, name='results'),
]
