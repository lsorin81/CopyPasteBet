import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.views.generic import View
from CPBet.models import bookmakers

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
STANDARD_MARATHON_NO = 16


class BetHelp(View):
    template_name = "confirm.html"

    def get_context_data(self, **kwargs):
        context = super(BetHelp, self).get_context_data(**kwargs)
        return context

    def stripUrl(self, urlString):
        urlArray = urlString.split("/")
        return urlArray[len(urlArray)-1]


class MarathonClass(BetHelp):

    def marathon(self, request, stringArray):
        marathonArray = stringArray[0].split(" ")
        if len(marathonArray) == STANDARD_MARATHON_NO:
            betFields = {
                ARG_BOOKMAKER_PICTURE: super(MarathonClass, self).
                stripUrl(bookmakers.objects.get(pk=4).image.url),
                ARG_EVENT_DESCRIPTION: "Fulham -vs- Stoke City",
                ARG_EVENT_DATE: "10/5/2013 7:00",
                ARG_EVENT_RESULT: "FT 1:0",
                ARG_BET_DESCRIPTION: "Fulham",
                ARG_BET_CODE: "327237505",
                ARG_BET_ODDS: 2.640,
                ARG_BET_AMOUNT: 10.00,
                ARG_BET_DATE: "10/5/2013 6:48",
                ARG_BET_TYPE: "Game - 1X2",
                ARG_BET_RESULT: 5
            }
            return betFields

        else:
            return None


def login_template(request):
    template = loader.get_template('CPBet/index.html')
    context = RequestContext(request, )
    return HttpResponse(template.render(context))


def register_template(request):
    template = loader.get_template('CPBet/register.html')
    context = RequestContext(request, )
    return HttpResponse(template.render(context))


