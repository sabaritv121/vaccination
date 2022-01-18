from django.contrib import admin

from vaccination_app import models

admin.site.register(models.Login)
admin.site.register(models.Nurse)
admin.site.register(models.Hospital)
admin.site.register(models.User)
admin.site.register(models.Vaccine)
admin.site.register(models.VaccinationSchedule)
admin.site.register(models.Complaint)
admin.site.register(models.Appointment)
admin.site.register(models.ReportCard)







