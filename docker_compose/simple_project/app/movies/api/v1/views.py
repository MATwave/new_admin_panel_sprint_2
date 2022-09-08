from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from movies.models import Filmwork
from movies.models.person_film_work import PersonFilmwork,Roles

class MoviesListApi(BaseListView):
    model = Filmwork
    http_method_names = ['get']  # Список методов, которые реализует обработчик
    paginate_by = 50
    def get_queryset(self):
        queryset = Filmwork.objects.prefetch_related('genres', 'person').values().all().\
            annotate(genres=ArrayAgg('genres__name',
                                     distinct=True),
                     actors=ArrayAgg('persons__full_name',
                                     filter=Q(personfilmwork__role__icontains=Roles.ACTOR),
                                     distinct=True),
                     directors=ArrayAgg('persons__full_name',
                                        filter=Q(personfilmwork__role__icontains=Roles.DIRECTOR),
                                        distinct=True),
                     writers=ArrayAgg('persons__full_name',
                                      filter=Q(personfilmwork__role__icontains=Roles.WRITER),
                                      distinct=True)
                     )
        
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):

        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset,self.paginate_by)
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(page.object_list)
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)