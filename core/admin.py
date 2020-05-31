from django.contrib import admin
from .models import Diagnos
from .models import Epicriz
from .models import Disease
from .models import Answer
from .models import Question
from .models import Ancket
from .models import Patient
from .models import User


# Register your models here.
admin.site.register(Diagnos)
admin.site.register(Epicriz)
admin.site.register(Disease)
admin.site.register(Answer)
admin.site.register(Ancket)
admin.site.register(Patient)
admin.site.register(User)