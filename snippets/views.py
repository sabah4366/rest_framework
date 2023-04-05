from django.shortcuts import render
from rest_framework.views import APIView
from .models import Snippet
from .serializers import SnippetSerialiser,UserSerialiser
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    this viewsets automatically provides list and retrieve actions
    """
    queryset=User.objects.all()
    serializer_class=UserSerialiser




class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)