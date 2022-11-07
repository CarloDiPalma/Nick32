from django.contrib import admin
from .models import Room, Topic, Message, RoomCount


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'topic', 'name', 'description')
    list_display_links = ('id', 'host', 'topic', 'name', 'description')
    search_fields = ('id', 'name', 'description')


admin.site.register(Room, RoomAdmin)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(RoomCount)
