from CPBet.models import english_premier_league_result, bookmaker, unique_token_key

__author__ = 'tippytip'
from django.contrib import admin


admin.site.register(english_premier_league_result)
admin.site.register(bookmaker)
admin.site.register(unique_token_key)

# from django.contrib import admin
# from polls.models import Choice, Poll
#
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
#
# class PollAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
# admin.site.register(Poll, PollAdmin)