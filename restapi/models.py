from django.db import models

# Create your models here.
class Bank(models.Model):
    class Meta:
        db_table = 'banks'

    id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=49, db_column='name')

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class Branch(models.Model):
    class Meta:
        db_table = 'branches'

    ifsc = models.CharField(primary_key=True, max_length=11, db_column='ifsc')
    bank_id = models.IntegerField(primary_key=True, db_column='bank_id')
    branch = models.CharField(primary_key=True, max_length=74, db_column='branch')
    address = models.CharField(primary_key=True, max_length=195, db_column='address')
    city = models.CharField(primary_key=True, max_length=50, db_column='city')
    district = models.CharField(primary_key=True, max_length=50, db_column='district')
    state = models.CharField(primary_key=True, max_length=26, db_column='state')

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.ifsc, self.bank_id, self.branch, self.address, self.city, self.district, self.state)


class BankBranch(models.Model):
    class Meta:
        db_table = 'bank_branches'

    ifsc = models.CharField(primary_key=True, max_length=11, db_column='ifsc')
    bank_id = models.IntegerField(primary_key=True, db_column='bank_id')
    branch = models.CharField(primary_key=True, max_length=74, db_column='branch')
    address = models.CharField(primary_key=True, max_length=195, db_column='address')
    city = models.CharField(primary_key=True, max_length=50, db_column='city')
    district = models.CharField(primary_key=True, max_length=50, db_column='district')
    state = models.CharField(primary_key=True, max_length=26, db_column='state')
    bank_name = models.CharField(max_length=49, db_column='bank_name')

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.ifsc, self.bank_id, self.bank_name, self.branch, self.address, self.city, self.district, self.state)
