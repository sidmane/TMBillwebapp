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