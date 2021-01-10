from hsvp_server.settings.base import MEDIA_ROOT
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage


class UploadFile(APIView):
    """
    file upload
    """

    def post(self, request, *args, **kwargs):

        try:
            file_object = request.FILES['document']
            file_name = file_object.name

            if file_object.size > (4 * 1024 * 1024):
                return Response({file_name: 'Unable to upload file should be less than 4 MB.'})

            fs = FileSystemStorage()
            filename = fs.save(file_name, file_object)
            uploaded_file_url = fs.url(filename)

            return Response({'uploaded_file_url': uploaded_file_url})

        except Exception as e:
            print(str(e))
            responseData = {'message': str(e), 'status': False}
            return Response(responseData)
