__author__ = 'tippytip'
#StdLib imports
import re

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext

# Third-party app imports

# Constants by convention
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
POST_BET_365 = "Bet365"
POST_MARATHON_BET = "MarathonBet"
POST_PINNACLE_SPORTS = "PinnacleSports"
POST_WILLIAM_HILL = "WilliamHill"
ID_BET365 = 0
ID_MARATHON_BET = 1
ID_PINNACLE_SPORTS = 2
ID_WILLIAM_HILL = 3
REGEX_PINNACLE_ODDS_SURROUND = re.compile(r".+\d+\.\d\d\d\s[ADF].+")
REGEX_PINNACLE_ODDS = re.compile(r"\d+\.\d\d\d\s[ADF]")


# when we copy the date from other websites the dates come from other world regions
# pending and settled
DUMMY_BET = {
    ARG_EVENT_DESCRIPTION: "Fulham -vs- Stoke City",
    ARG_EVENT_DATE: "10/5/2013 7:00",
    ARG_EVENT_RESULT: "FT 1:0",
    ARG_BET_DESCRIPTION: "Fulham",
    ARG_BET_CODE: "327237505",
    ARG_BET_BOOKMAKER: "PinnacleSports",
    ARG_BET_ODDS: 2.640,
    ARG_BET_AMOUNT: 10.00,
    ARG_BET_DATE: "10/5/2013 6:48",
    ARG_BET_TYPE: "Game - 1X2",
    ARG_BET_RESULT: 5
}


def confirm(request):
    dummies = list()
    dummies.append(request.POST.get(POST_BET_365))
    dummies.append(request.POST.get(POST_MARATHON_BET))
    dummies.append(request.POST.get(POST_PINNACLE_SPORTS))
    dummies.append(request.POST.get(POST_WILLIAM_HILL))
    printTabbedArrays(dummies)
    # printDateArrays(dummies)
# process the Bet
    return render_to_response('CPBet/confirm.html', DUMMY_BET, context_instance=RequestContext(request))


def identifyPinnacle(unprocessedString):
    return REGEX_PINNACLE_ODDS.findall(unprocessedString,)


# Helpers functions -----------------------------------
def printTabbedArrays(dummies):
    for d in dummies:
    # check if it has Pinnacle odds style
        pinnacleOdds = identifyPinnacle(d)
        if len(pinnacleOdds) == 0:
            print ">>>> None"
        else:
            for p in pinnacleOdds:
                print p.encode()
    # print split parts!!
        splitArray = d.split("\t")
        for s in splitArray:
            print s


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