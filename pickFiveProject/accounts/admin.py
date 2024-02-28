from django.contrib import admin
from .models import Account, Group, GroupXAccount, Picks, Spreads, Teams, Outcomes

# Register your models here.
admin.site.register(Account)
admin.site.register(Group)
admin.site.register(GroupXAccount)
admin.site.register(Picks)
admin.site.register(Spreads)
admin.site.register(Teams)
admin.site.register(Outcomes)
