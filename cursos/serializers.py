from rest_framework import serializers

from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship (melhores casos 1 para 1)
    # Um curso pode ter muitas avaliacoes
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)#Apenas leitura
    
    # HyperLinked Related Field(Melhor caso 1 para muitos)
    # avaliacao-detail igual ao nome da model + detail
    avaliacoes = serializers.HyperlinkedRelatedField(
       many=True,
        read_only=True, 
        view_name='avaliacao-detail'
    )

    # Primary Key Related Field
    # Retorna apenas os ID das avaliacoes
    #avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )

    
