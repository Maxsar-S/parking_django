from django.contrib import admin
from .models import Reservation, Space, User


admin.site.register(Reservation)
admin.site.register(Space)
admin.site.register(User)
