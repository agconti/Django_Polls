from django.contrib import admin
from polls.models import Poll, Choice
class ChoiceInline(admin.TabularInline):
	"""for representing choices with polls"""
	model = Choice
	extra = 3 
		

class PollAdmin(admin.ModelAdmin):
	""" admin rep of poll model"""
	# changes dispaly 'mode' to a list of these items
	list_display = ('question', 'pub_date', 'was_published_recently')
	# adds a filter by publication date
	list_filter = ['pub_date']
	#incorperates date hierarchy so we can drill down my month year ect
	date_hierarchy = 'pub_date'
	# as a field to search by question
	search_fields = ['question']


	fieldsets = [
				(None,               {'fields': ['question']}),
				('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
				]
	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)