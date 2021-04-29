
from rest_framework import viewsets
from rest_framework.response import Response

from tutorials.serializers import TutorialSerializer
from tutorials.models import Tutorial

class TutorialViewSet(viewsets.ModelViewSet):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.all()

    def list(self, request, *args, **kwargs):
        title = request.GET.get('title', None)
        published = request.GET.get('published', None)
        if title and published:
            queryset = Tutorial.objects.filter(title__icontains=title, published=published)
        elif title:
            queryset = Tutorial.objects.filter(title__icontains=title)
        elif published:
            queryset = Tutorial.objects.filter(published=published)
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)