import json

from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View

from server.models import Server
from utils.validators import validate_dict

REQUIREMENTS = {'name', 'address', 'state', 'user_id'}


class ServerView(View):
    """Server view handles GET, POST, PUT, DELETE requests."""

    def get(self, request, server_id=None):
        """Handles GET request.

        If server_id is None, return all servers in response,
        otherwise server with given id.
        If server with specified id was not found return error.

        :param server_id: int - server id
        :return: JsonResponse:
                {
                    response: <list of servers>/<servers>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        if server_id:
            # Get server with specified id
            server = Server.get_by_id(server_id)

            if server:
                json_response['response'] = server.to_dict()
                return JsonResponse(json_response, status=200)

            json_response['error'] = 'Server with specified id was not found.'
            return JsonResponse(json_response, status=404)

        # Get all servers
        json_response['response'] = [server.to_dict() for server in Server.get()]

        return JsonResponse(json_response, status=200)

    def post(self, request):
        """Handles POST request.

        Get server data from POST request and create one in database.
        In response return created server or error if server was not created.

        Require JSON with fields:
            {
                'name': <server name>,
                'address': <server address>,
                'state': <server state>,
                'user_id': <user_id>
            }

        :return: JsonResponse:
                {
                    response: <server>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        server_dict = json.loads(request.body.decode('utf-8'))

        if not validate_dict(server_dict, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        server = Server.create(**server_dict)

        if server:
            json_response['response'] = server.to_dict()
            return JsonResponse(json_response, status=201)

        json_response['error'] = 'Server was not created.'
        return JsonResponse(json_response, status=400)

    def put(self, request, server_id):
        """Handles PUT request.

        Get server data from PUT request and update server with given id in database.
        In response return updated server or error if server was not updated.

        :param server_id: server id
        :return: JsonResponse:
                {
                    response: <server>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        server_dict = json.loads(request.body.decode('utf-8'))

        if not validate_dict(server_dict, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        server_dict['id'] = server_id
        server = Server.update(**server_dict)

        if server:
            json_response['response'] = server.to_dict()
            return JsonResponse(json_response, status=200)

        json_response['error'] = 'Server was not updated.'
        return JsonResponse(json_response, status=400)

    def delete(self, request, server_id):
        """Handles DELETE request.

        Delete server with given id from database.

        :param server_id: int - server id
        :return: HttpResponse: Status 200 for success, 400 otherwise.
        """

        deleted = Server.remove(server_id)

        if deleted:
            return HttpResponse(status=200)

        return HttpResponse(status=400)
