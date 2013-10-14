__author__ = 'tippytip'
import json
import tokenlib
from django.contrib.auth import authenticate, login
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed, HttpResponse

# Constants by convention
POST_USERNAME = "Username"
POST_PASSWORD = "Password"
POST_EMAIL = "Email"
STATUS_DUPLICATE = 456
STATUS_NOT_YET = 457
STATUS_WRONG_USERNAME_OR_PASSWORD = 459
SECRET = "CopyPasteBet"


def register(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=['POST'])
    # make sure u verify that the 2 passwords are the same
    try:
    # we create the User object
        new_user = User.objects.create_user(
            username=request.POST.get(POST_USERNAME),
            password=request.POST.get(POST_PASSWORD),
            email=request.POST.get(POST_EMAIL),
        )
        new_user.save()
    except:
        return HttpResponse(json.dumps({"Status": STATUS_DUPLICATE,
                                        "Error": "User could not be created. Duplicate username or email"},
                            sort_keys=True))
    # authenticate newly formed user
    # is it possible to use new_user references????
    user = authenticate(username=new_user.username, password=new_user.password)
    if user is not None:
        if user.is_active:
        # we log in and create token
            login(request, user)
            print "User has been authenticated."
            token = tokenlib.make_token({"userid": user.id}, secret=SECRET)
        template = loader.get_template('CPBet/homepage.html')
        context = RequestContext(request, token)
        return HttpResponse(template.render(context))
        # return HttpResponse(json.dumps({"Status": 0, "Token": token}, sort_keys=True))
    else:
        return HttpResponse(json.dumps({"Status": STATUS_NOT_YET,
                                        "Error": "The account has not been created yet."},
                                       sort_keys=True))


def login(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=['POST'])
    username = request.POST.get(POST_USERNAME)
    password = request.POST.get(POST_PASSWORD)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print user
            token = tokenlib.make_token({"userid": user.id}, secret=SECRET)
        return HttpResponse(json.dumps({"Status": 0, "Token": token}, sort_keys=True))
    else:
        return HttpResponse(json.dumps({"Status": STATUS_WRONG_USERNAME_OR_PASSWORD,
                                        "Error": "Username or password incorrect."},
                                       sort_keys=True))