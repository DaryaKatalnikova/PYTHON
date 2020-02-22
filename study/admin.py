from django.contrib import admin
from .models import Test
from .models import Quest
from .models import Answer
from .models import Schools
from .models import Useranswer, User


admin.site.register(Test)
admin.site.register(Quest)
admin.site.register(Answer)
admin.site.register(Schools)
admin.site.register(Useranswer)
admin.site.register(User)