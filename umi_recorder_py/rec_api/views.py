from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class RecordVodView(APIView):
    def post(self, request):
        streamer_id: str = request.data.get('streamer_id')

        # return RecService.start_recording(streamer_id)
        return Response('Hello world: ' + streamer_id)