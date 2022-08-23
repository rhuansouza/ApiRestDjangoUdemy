from asyncio import mixins

from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Avaliacao, Curso
from .permissions import EhSuperUser
from .serializers import AvaliacaoSerializer, CursoSerializer

"""
API V2 
"""
class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,)
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @api_view(['GET'])
    def listarmultiplos(request):
        curso = Curso.objects.all()
        avaliacao = Avaliacao.objects.all()
        print('Entrou aqui')
        serializerCurso = CursoSerializer(curso, many=True)
        serializerAvaliacao = AvaliacaoSerializer(avaliacao, many=True)
        resultModel = serializerCurso.data + serializerAvaliacao.data
        #print(serializerCurso.data[0])
        #print(serializerCurso.data[0]['titulo'])
        #serializerCurso.data[0]['titulo'] = 'teste'
        #print(serializerCurso.data[0].get('titulo'))
        listaSaida = [
            
        ]
        novasaida = {
            
        }            
        
        for item in serializerCurso.data:
            print('entrou',item.get('titulo'))
            novasaida = item.get('titulo')
            print('dicionario ',novasaida)
            listaSaida.append(novasaida)
            
        
        print(novasaida)
        saida = {
            'curso' : listaSaida,
            'avaliacoes': serializerCurso.data[0].get('titulo')
        }
        return Response(saida)
        


    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        print(pk)
        # Paginando rota
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""
class AvaliacaoViewSet(mixins.ListModelMixin,
mixins.CreateModelMixin,
mixins.RetrieveModelMixin,
mixins.UpdateModelMixin,
mixins.DestroyModelMixin,
viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
   

"""
API V1 
"""
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                curso_id=self.kwargs.get('curso_pk'),
                pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(),
                                 pk=self.kwargs.get('avaliacao_pk'))




    
