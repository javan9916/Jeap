from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import VideoItem

class VideoItemAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(VideoItem, VideoItemAdmin)
