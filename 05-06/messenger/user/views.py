from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import User
import json
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(['GET'])
def user_info(request):
    data = json.loads(request.body)
    if ("user_id" not in data.keys()):
        return JsonResponse({'Error': "not user_id in the passed arguments"}, status=400)
    if (not str(data["user_id"]).isdigit()):
        return JsonResponse({'Error': "user_id must be digit"}, status=400)
    user = get_object_or_404(User, id=data["user_id"])
    result_user = {"username":user.username,"photo":user.photo, "birthday":user.birthday}
    return JsonResponse({"User":result_user}, status=201)
