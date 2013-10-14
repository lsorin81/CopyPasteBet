__author__ = 'tippytip'
from django.contrib import admin
from .models import english_premier_league_results

admin.site.register(english_premier_league_results)

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