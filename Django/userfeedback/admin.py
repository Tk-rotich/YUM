from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from userfeedback.models import userComments

admin.site.site_header = "Django Test"
# Register your models here.

class userCommentsAdmin(ImportExportActionModelAdmin):
	list_display = ("id",'name', "phone_number","neighbourhood","rating","comment")
	search_fields = ('id','name','phone_number','neighbourhood')
	list_filter = ('name','phone_number','neighbourhood','rating','comment')

admin.site.register(userComments, userCommentsAdmin)