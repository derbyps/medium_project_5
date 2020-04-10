from django.contrib import admin
from .models import Users, Kategori, Artikel, Respon, Like
# Register your models here.
admin.site.register(Users)
admin.site.register(Kategori)
admin.site.register(Artikel)
admin.site.register(Respon)
admin.site.register(Like)
