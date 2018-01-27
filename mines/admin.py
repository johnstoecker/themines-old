from django.contrib import admin

from .models import Activity
from .models import Task
from .models import DailyActivity

admin.site.register(Activity)
admin.site.register(Task)
admin.site.register(DailyActivity)
