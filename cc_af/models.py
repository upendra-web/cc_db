from __future__ import unicode_literals

from django.db import models


class Compound(models.Model):
    name = models.CharField(max_length=500)
    formula = models.CharField(max_length=500)
    cas_no = models.CharField(max_length=50)
    mol_wt = models.CharField(max_length=50)
    tc = models.CharField(max_length=50)
    pc = models.CharField(max_length=50)
    vc = models.CharField(max_length=50)
    zc = models.CharField(max_length=50)
    af = models.CharField(max_length=50)

    def __str__(self):
        return self.name + '-' + self.formula


