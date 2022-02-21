from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Reaction


class ReactionView(ViewSet):
    """Rare reactions"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single reaction

        Returns:
            Response -- JSON serialized reaction
        """
        try:
            reaction = Reaction.objects.get(pk=pk)
            serializer = ReactionSerializer(reaction)
            return Response(serializer.data)
        except Reaction.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 


    def list(self, request):
 
        reactions = Reaction.objects.all()
        serializer = ReactionSerializer(reactions, many=True)
        return Response(serializer.data)
    
    
    def create(self, request):

        reaction = Reaction.objects.create(
            label=request.data['label'],
            image_url=request.data['image_url']
        )
        try:
            reaction.save()
            serializer = ReactionSerializer(reaction)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def destroy(self, request, pk=None):
        """Handle DELETE request for a single reaction

        Returns:
            No content, 204 status.
        """
        try:
            reaction = Reaction.objects.get(pk=pk)
            reaction.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Reaction.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        """Handle PUT request for a single reaction

        Returns:
            No content, 204 status.
        """
        try:
            reaction = Reaction.objects.get(pk=pk)
            reaction.label = request.data['label']
            reaction.image_url = request.data['image_url']
            reaction.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Reaction.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class ReactionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Reaction
        fields = ('id', 'label', 'image_url')
