from django.db import models


class TmbinTable(models.Model):
    table_no = models.IntegerField(primary_key=True)
    is_available = models.IntegerField()
    table_name = models.CharField(db_column='TABLE_NAME', unique=True, max_length=25, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.table_name
    class Meta:
        managed = False
        db_table = 'tmbin_table'

class TmbinCustomer(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    business_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    gst_no = models.CharField(db_column='GST_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tmbin_customer'
