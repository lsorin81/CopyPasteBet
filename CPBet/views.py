from django.http import HttpResponse
from django.template import loader, RequestContext


def login_template(request):
    template = loader.get_template('CPBet/index.html')
    context = RequestContext(request, )
    return HttpResponse(template.render(context))


def register_template(request):
    template = loader.get_template('CPBet/register.html')
    context = RequestContext(request, )
    return HttpResponse(template.render(context))