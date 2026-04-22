from django.contrib import admin
from .models import (
	Ability,
	CareNote,
	Diagnosis,
	Employee,
	Invoice,
	LineItem,
	Observation,
	Owner,
	Patient,
	PatientAbility,
	Payment,
	ProcedureDefinition,
	Universe,
	Visit,
	VisitDiagnosis,
	VisitProcedure,
)

admin.site.register(Ability)
admin.site.register(Diagnosis)
admin.site.register(Employee)
admin.site.register(Invoice)
admin.site.register(LineItem)
admin.site.register(Observation)
admin.site.register(Owner)
admin.site.register(Patient)
admin.site.register(PatientAbility)
admin.site.register(Payment)
admin.site.register(ProcedureDefinition)
admin.site.register(Universe)
admin.site.register(Visit)
admin.site.register(VisitDiagnosis)
admin.site.register(VisitProcedure)
admin.site.register(CareNote)
