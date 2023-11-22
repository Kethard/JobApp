from django.contrib import admin
from subscribe.models import Subscribe
from uploadapp.models import Uploads, UploadFile
# Register your models here.
admin.site.register(Subscribe)
admin.site.register(Uploads)
admin.site.register(UploadFile)