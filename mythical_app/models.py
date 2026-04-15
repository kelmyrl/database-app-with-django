# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ability(models.Model):
    ability_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    ability_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ability'


class Diagnosis(models.Model):
    diagnosis_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosis'


class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    job_role = models.TextField()
    specialty = models.TextField(blank=True, null=True)
    hire_date = models.DateField()
    phone = models.TextField()
    email = models.TextField()
    schedule = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Invoice(models.Model):
    invoice_id = models.BigAutoField(primary_key=True)
    visit = models.ForeignKey('Visit', models.DO_NOTHING)
    status = models.TextField()
    due_date = models.DateField(blank=True, null=True)
    issue_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'invoice'


class LineItem(models.Model):
    line_item_id = models.BigAutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    line_item_type = models.TextField()
    visit_procedure = models.ForeignKey('VisitProcedure', models.DO_NOTHING, blank=True, null=True)
    medication_id = models.BigIntegerField(blank=True, null=True)
    vaccination_id = models.BigIntegerField(blank=True, null=True)
    boarding_stay_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'line_item'


class Observation(models.Model):
    observation_id = models.BigAutoField(primary_key=True)
    visit_procedure = models.ForeignKey('VisitProcedure', models.DO_NOTHING)
    observation_type = models.TextField(blank=True, null=True)
    observed_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observation'


class Owner(models.Model):
    owner_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    universe = models.ForeignKey('Universe', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'owner'


class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    dob = models.DateField(blank=True, null=True)
    name = models.TextField()
    color = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(Owner, models.DO_NOTHING)
    species_id = models.BigIntegerField(blank=True, null=True)
    breed_id = models.BigIntegerField(blank=True, null=True)
    universe = models.ForeignKey('Universe', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient'


class PatientAbility(models.Model):
    patient_ability_id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    ability = models.ForeignKey(Ability, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_ability'
        unique_together = (('patient', 'ability'),)


class Payment(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.TextField()

    class Meta:
        managed = False
        db_table = 'payment'


class ProcedureDefinition(models.Model):
    procedure_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    standard_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_definition'


class Universe(models.Model):
    universe_id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'universe'


class Visit(models.Model):
    visit_id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    vet = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit'


class VisitDiagnosis(models.Model):
    visit_diagnosis_id = models.BigAutoField(primary_key=True)
    visit = models.ForeignKey(Visit, models.DO_NOTHING)
    diagnosis = models.ForeignKey(Diagnosis, models.DO_NOTHING)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    recorded_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visit_diagnosis'
        unique_together = (('visit', 'diagnosis', 'recorded_at'),)


class VisitProcedure(models.Model):
    visit_procedure_id = models.BigAutoField(primary_key=True)
    visit = models.ForeignKey(Visit, models.DO_NOTHING)
    procedure = models.ForeignKey(ProcedureDefinition, models.DO_NOTHING)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    performed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visit_procedure'
        unique_together = (('visit', 'procedure', 'performed_at'),)
