import json
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotAllowed

__author__ = 'tippytip'

# Constants by convention
ARG_BET = "Bet"
STATUS_OK = 200


# def home(request):
#     if request.method != "POST":
#         return HttpResponseNotAllowed(permitted_methods=['POST'])
#     unprocessedString = request.POST.get(ARG_BET)
#
#     try:
#     # we create the User object
#         new_user = User.objects.create_user(
#             username=dictionary[USERNAME],
#             email=dictionary[EMAIL],
#             password=dictionary[PASSWORD],
#         )
#         new_user.save()
#     except:
#         return HttpResponse(json.dumps({"Status": STATUS_DUPLICATE,
#                                         "Error": "User could not be created. Duplicate username or email"},
#                             sort_keys=True))
#     return HttpResponse(json.dumps({"Status": STATUS_OK, ARG_BET: unprocessedString},
#                                        sort_keys=True))