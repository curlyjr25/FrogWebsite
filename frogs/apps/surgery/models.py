from django.db import models

class Surgery(models.Model):
    surgery_number = models.IntegerField()
    date = models.DateField()
    frog = models.CharField(max_length=200)
    tank_number = models.IntegerField()
    collagenase = models.IntegerField()
    collagenase_amount = models.IntegerField()
    activity = models.IntegerField()
    solution_volume = models.IntegerField()
    g_b_oocytes = models.CharField(max_length=1)
    volume_of_oocytes = models.IntegerField()
    previous_surgery = models.ForeignKey('Surgery', null=True, blank=True)
    company = models.CharField(max_length=200)
    number_oocytes_ordered = models.IntegerField()
    complaints = models.BooleanField()
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.surgery_number)
