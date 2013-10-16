from CPBet.bet_checkers.helpers import stripUrl
from CPBet.models import bookmaker


__author__ = 'tippytip'
#StdLib imports
import json
import re
# Core Django imports
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
# Third-party app imports

# Constants by convention

POST_BET = "Bet"
POST_TOKEN = "Token"
ID_BET365 = 0
ID_MARATHON_BET = 1
ID_PINNACLE_SPORTS = 2
ID_WILLIAM_HILL = 3
REGEX_PINNACLE_ODDS_SURROUND = re.compile(r".+\d+\.\d\d\d\s[ADF].+")
REGEX_PINNACLE_ODDS = re.compile(r"\d+\.\d\d\d\s[ADF]")
SECRET = "CopyPasteBet"
STATUS_TOKEN_PARSING_ERROR = 460
ERR_PARSE_TOKEN = "Error parsing the token"
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
# when we copy the date from other websites the dates come from other world regions
# pending and settled


def confirm(request):
    unprocessedString = request.POST.get(POST_BET)
    # token = request.POST.get(POST_TOKEN)
    # try:
    #     if type(token) == unicode:
    #     # encode() without parameters transforms it to String
    #         token = token.encode()
    #     secret = unique_token_key.objects.get(pk=1).key
    #     data = tokenlib.parse_token(token, secret=secret)
    #     key = unicode("userid")
    # except:
    #     return HttpResponse(json.dumps({"Status": STATUS_TOKEN_PARSING_ERROR,
    #                                     "Error": ERR_PARSE_TOKEN}, sort_keys=True))
    if len(identifyPinnacle(unprocessedString)) > 0:
    # PinnacleSports
        PinnacleArray = printTabbedArrays(unprocessedString)
        if len(PinnacleArray) == 7:
            print bookmaker.objects.get(pk=1).image.url
            betFields = {
                ARG_BOOKMAKER_PICTURE: bookmaker.objects.get(pk=1).image.url,
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
            return render_to_response('CPBet/confirm.html', betFields, context_instance=RequestContext(request))
        else:
            return HttpResponse(json.dumps({"Status": 400,
                                            "Error": "Not a 7 part PinnacleSports Bet!"},
                                           sort_keys=True))
    tabArray = printTabbedArrays(unprocessedString)
    if len(tabArray) == 1:
    # instantiate betHelp class
        marathonArray = tabArray[0].split(" ")
        if len(marathonArray) == STANDARD_MARATHON_NO:
        # then parse the string into fields
            betFields = {
                ARG_BOOKMAKER_PICTURE: bookmaker.objects.get(pk=4).image.url,
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
            return render_to_response('CPBet/confirm.html', betFields,
                                      context_instance=RequestContext(request))
        else:
            return HttpResponse(json.dumps({"Status": 400,
                                            "Error": "Not a full part Marathon Bet!"},
                                           sort_keys=True))



def identifyPinnacle(unprocessedString):
    foundString = REGEX_PINNACLE_ODDS.findall(unprocessedString)
    return foundString


# Helpers functions -----------------------------------


def printTabbedArrays(d):
# print split parts!!
    splitArray = d.split("\t")
    for s in splitArray:
        print s
    return splitArray


def printDateArrays(dummy):
    for d in dummy:
        dArray = d.split("\t")
        for array in dArray:
            if hasDate(array):
                print array + " contains a date!"


def hasDate(string):
    if re.match(r".+\d:\d\d.+", string):
        return True
    return False





# check if it has Pinnacle odds style
# pinnacleOdds = identifyPinnacle(d)
#     if len(pinnacleOdds) == 0:
#         print ">>>> None"
#     else:
#         for p in pinnacleOdds:
#             print p.encode()



    # if re.match(r".+\d\d:\d\d:\d\d.+", array):
    #             print "We found this date: "+array+"\n inside this Bet: "+d
    #         elif re.match(r".+\d:\d\d:\d\d.+", array):
    #             print "We found this date: "+array+"\n inside this Bet: "+d
    #         elif re.match(r".+\d\d:\d\d.+", array):
    #             print "We found this date: "+array+"\n inside this Bet: "+d
    #         elif re.match(r".+\d:\d\d.+", array):
    #             print "We found this date: "+array+"\n inside this Bet: "+d

# def makeDictionary(request):
#     try:
#         dictionary = {
#             ADDRESS: request.POST.get(ADDRESS),
#             CONTACT: request.POST.get(CONTACT),
#             EMAIL: request.POST.get(EMAIL),
#             HOURS: request.POST.get(HOURS),
#             LATITUDE: request.POST.get(LATITUDE),
#             LONGITUDE: request.POST.get(LONGITUDE),
#             PASSWORD: request.POST.get(PASSWORD),
#             PICTURE: request.POST.get(PICTURE),
#             REGISTRATION_ID: request.POST.get(REGISTRATION_ID),
#             RESTAURANT_NAME: request.POST.get(RESTAURANT_NAME),
#             USERNAME: request.POST.get(USERNAME),
#         }
#         return dictionary
#     except Exception, e:
#         return HttpResponse(json.dumps({"Status": 400, "Error": e.args[0]},
#                             sort_keys=True))