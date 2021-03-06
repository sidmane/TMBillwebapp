# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bank(models.Model):
    cutomer = models.CharField(max_length=80, blank=True, null=True)
    bankname = models.CharField(max_length=80, blank=True, null=True)
    branch = models.CharField(max_length=80, blank=True, null=True)
    branchcode = models.CharField(max_length=80, blank=True, null=True)
    accountnumber = models.CharField(max_length=30, blank=True, null=True)
    accounttype = models.CharField(max_length=20, blank=True, null=True)
    ifsc = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank'


class BillKotNo(models.Model):
    bill_no = models.IntegerField(blank=True, null=True)
    kot_no = models.IntegerField(blank=True, null=True)
    purchase_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_kot_no'


class Customerbalance(models.Model):
    billno = models.ForeignKey('TmbinBill', models.DO_NOTHING, db_column='billNo')  # Field name made lowercase.
    customerid = models.ForeignKey('TmbinCustomer', models.DO_NOTHING, db_column='customerId')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    debitamount = models.DecimalField(db_column='debitAmount', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    creditamount = models.DecimalField(db_column='creditAmount', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    is_paid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customerbalance'


class Dailycash(models.Model):
    date = models.DateField(blank=True, null=True)
    totalamount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    twok = models.IntegerField(blank=True, null=True)
    fiveh = models.IntegerField(blank=True, null=True)
    twoh = models.IntegerField(blank=True, null=True)
    oneh = models.IntegerField(blank=True, null=True)
    fifty = models.IntegerField(blank=True, null=True)
    twenty = models.IntegerField(blank=True, null=True)
    ten = models.IntegerField(blank=True, null=True)
    tencoin = models.IntegerField(blank=True, null=True)
    fivecoin = models.IntegerField(blank=True, null=True)
    twocoin = models.IntegerField(blank=True, null=True)
    onecoin = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dailycash'


class Demoactivate(models.Model):
    end = models.DateField(blank=True, null=True)
    dayleft = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demoactivate'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrderType(models.Model):
    type = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_type'


class Payment(models.Model):
    order_type = models.ForeignKey(OrderType, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING, blank=True, null=True)
    refer = models.CharField(max_length=30, blank=True, null=True)
    is_split = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentSplit(models.Model):
    payment = models.ForeignKey(Payment, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_split'


class PaymentType(models.Model):
    type = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_type'


class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField(unique=True)
    purchase_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    supplier = models.ForeignKey('TmbinVendor', models.DO_NOTHING, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase'


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, models.DO_NOTHING)
    item = models.ForeignKey('Rawmaterial', models.DO_NOTHING, blank=True, null=True)
    expiry = models.DateField(blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    net_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    igst = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sgst = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_item'


class RawMaterialCategory(models.Model):
    category_name = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_material_category'


class Rawmaterial(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    unit = models.ForeignKey('Unit', models.DO_NOTHING, blank=True, null=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    igst = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sgst = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_sgst = models.IntegerField()
    raw_material_category = models.ForeignKey(RawMaterialCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawmaterial'


class Recipe(models.Model):
    recipe = models.ForeignKey('TmbinItem', models.DO_NOTHING)
    rawmaterial = models.ForeignKey(Rawmaterial, models.DO_NOTHING)
    qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class TmbillExpenses(models.Model):
    category = models.ForeignKey('TmbillExpensescategory', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    is_chargable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmbill_expenses'


class TmbillExpensescategory(models.Model):
    category_name = models.CharField(unique=True, max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbill_expensescategory'


class TmbinAdmin(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    business_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    gst_no = models.CharField(db_column='GST_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_admin'


class TmbinBill(models.Model):
    bill_no = models.AutoField(primary_key=True)
    total_person = models.IntegerField(blank=True, null=True)
    bill_date = models.DateField(blank=True, null=True)
    bill_time = models.TimeField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    table_no = models.ForeignKey('TmbinTable', models.DO_NOTHING, db_column='table_no', blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    igst = models.DecimalField(db_column='IGST', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cgst = models.DecimalField(db_column='CGST', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sgst = models.DecimalField(db_column='SGST', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    order_type = models.CharField(max_length=15, blank=True, null=True)
    tax_amount = models.IntegerField(blank=True, null=True)
    discount = models.ForeignKey('TmbinDiscount', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('TmbinCustomer', models.DO_NOTHING, blank=True, null=True)
    delivery_boy = models.ForeignKey('TmbinDeliveryBoy', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey(Payment, models.DO_NOTHING, blank=True, null=True)
    employeeid = models.ForeignKey('TmbinEmployee', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_bill'


class TmbinBillItem(models.Model):
    bill_no = models.ForeignKey(TmbinBill, models.DO_NOTHING, db_column='bill_no', blank=True, null=True)
    item = models.ForeignKey('TmbinItem', models.DO_NOTHING, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_bill_item'


class TmbinCategory(models.Model):
    name = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_category'


class TmbinCustomer(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    business_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    gst_no = models.CharField(db_column='GST_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_customer'


class TmbinDeliveryBoy(models.Model):
    boy_id = models.AutoField(primary_key=True)
    boy_name = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    date_of_jion = models.DateField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    shift = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_delivery_boy'


class TmbinDiscount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    discount_name = models.CharField(max_length=20, blank=True, null=True)
    discount_type = models.CharField(max_length=20, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_amount = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_discount'


class TmbinEmployee(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    date_of_join = models.DateField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    shift = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_employee'


class TmbinHotel(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    gst_no = models.CharField(db_column='GST_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    sellerid = models.CharField(max_length=60, blank=True, null=True)
    merchantid = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_hotel'


class TmbinItem(models.Model):
    code = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=40, blank=True, null=True)
    short_name = models.CharField(unique=True, max_length=20, blank=True, null=True)
    category = models.ForeignKey(TmbinCategory, models.DO_NOTHING, db_column='category', blank=True, null=True)
    sub_category = models.ForeignKey('TmbinSubCategory', models.DO_NOTHING, db_column='sub_category', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_item'


class TmbinKot(models.Model):
    kot_no = models.AutoField(primary_key=True)
    kot_time = models.TimeField(blank=True, null=True)
    kot_date = models.DateField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField()
    item = models.ForeignKey(TmbinItem, models.DO_NOTHING, blank=True, null=True)
    table_no = models.ForeignKey('TmbinTable', models.DO_NOTHING, db_column='table_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_kot'


class TmbinKotItem(models.Model):
    kot_no = models.ForeignKey(TmbinKot, models.DO_NOTHING, db_column='kot_no', blank=True, null=True)
    item = models.ForeignKey(TmbinItem, models.DO_NOTHING, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_kot_item'


class TmbinLogin(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=128)
    access = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tmbin_login'


class TmbinPrinter(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_printer'


class TmbinSubCategory(models.Model):
    category = models.ForeignKey(TmbinCategory, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_sub_category'


class TmbinTable(models.Model):
    table_no = models.IntegerField(primary_key=True)
    is_available = models.IntegerField()
    table_name = models.CharField(db_column='TABLE_NAME', unique=True, max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmbin_table'


class TmbinTax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_name = models.CharField(unique=True, max_length=20, blank=True, null=True)
    tex_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_tax'


class TmbinVendor(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    business_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    gst_no = models.CharField(db_column='GST_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmbin_vendor'


class Transfer(models.Model):
    date = models.DateField(blank=True, null=True)
    totalamount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    twok = models.IntegerField(blank=True, null=True)
    fiveh = models.IntegerField(blank=True, null=True)
    twoh = models.IntegerField(blank=True, null=True)
    oneh = models.IntegerField(blank=True, null=True)
    fifty = models.IntegerField(blank=True, null=True)
    twenty = models.IntegerField(blank=True, null=True)
    ten = models.IntegerField(blank=True, null=True)
    tencoin = models.IntegerField(blank=True, null=True)
    fivecoin = models.IntegerField(blank=True, null=True)
    twocoin = models.IntegerField(blank=True, null=True)
    onecoin = models.IntegerField(blank=True, null=True)
    bankid = models.ForeignKey(Bank, models.DO_NOTHING, db_column='bankid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfer'


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit = models.CharField(unique=True, max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit'
