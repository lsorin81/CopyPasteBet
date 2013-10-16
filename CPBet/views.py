from django.http import HttpResponse
from django.template import loader, RequestContext


ARG_EVENT_DESCRIPTION = "EventDescription"
ARG_EVENT_DATE = "EventDate"
ARG_EVENT_RESULT = "EventResult"
ARG_BET_DESCRIPTION = "BetDescription"
ARG_BET_CODE = "BetCode"
ARG_BET_BOOKMAKER = "BetBookmaker"
ARG_BET_ODDS = "BetOdds"
ARG_BET_AMOUNT = "BetAmount"
ARG_BET_DATE = "BetDate"
ARG_BET_TYPE = "BetType"
ARG_BET_RESULT = "BetResult"
ARG_DICTIONARY = "Dictionary"
ARG_BOOKMAKER_PICTURE = "BookmakerPicture"


def login_template(request):
    template = loader.get_template('CPBet/index.html')
    context = RequestContext(request, )
    return HttpResponse(template.render(context))


def register_template(request):
    template = loader.get_template('CPBet/register.html')
    context = RequestContext(request, )
    return HttpResponse(template.render(context))


