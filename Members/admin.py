from django.contrib import admin
from .models import Member
from django.utils.html import format_html

class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name', 'picture_display', 'phone', 'gender']

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = 'Name'

    def picture_display(self, obj):
        if obj.picture:
            return format_html('<img src="{}" style="width:100px" />'.format(obj.picture.url))
        else:
            return 'No picture'

    picture_display.short_description = 'Picture'

admin.site.register(Member, MemberAdmin)




