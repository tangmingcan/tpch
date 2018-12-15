# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Customer(models.Model):
    c_custkey = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=25, blank=True, null=True)
    c_address = models.CharField(max_length=40, blank=True, null=True)
    c_nationkey = models.BigIntegerField()
    c_phone = models.CharField(max_length=15, blank=True, null=True)
    c_acctbal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c_mktsegment = models.CharField(max_length=10, blank=True, null=True)
    c_comment = models.CharField(max_length=117, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Lineitem(models.Model):
    l_orderkey = models.BigIntegerField()
    l_partkey = models.BigIntegerField()
    l_suppkey = models.BigIntegerField()
    l_linenumber = models.IntegerField()
    l_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    l_extendedprice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    l_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    l_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    l_returnflag = models.CharField(max_length=1, blank=True, null=True)
    l_linestatus = models.CharField(max_length=1, blank=True, null=True)
    l_shipdate = models.DateField(blank=True, null=True)
    l_commitdate = models.DateField(blank=True, null=True)
    l_receiptdate = models.DateField(blank=True, null=True)
    l_shipinstruct = models.CharField(max_length=25, blank=True, null=True)
    l_shipmode = models.CharField(max_length=10, blank=True, null=True)
    l_comment = models.CharField(max_length=44, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineitem'
        unique_together = (('l_orderkey', 'l_linenumber'),)


class Nation(models.Model):
    n_nationkey = models.AutoField(primary_key=True)
    n_name = models.CharField(max_length=25, blank=True, null=True)
    n_regionkey = models.BigIntegerField()
    n_comment = models.CharField(max_length=152, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nation'


class Orders(models.Model):
    o_orderkey = models.AutoField(primary_key=True)
    o_custkey = models.BigIntegerField()
    o_orderstatus = models.CharField(max_length=1, blank=True, null=True)
    o_totalprice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    o_orderdate = models.DateField(blank=True, null=True)
    o_orderpriority = models.CharField(max_length=15, blank=True, null=True)
    o_clerk = models.CharField(max_length=15, blank=True, null=True)
    o_shippriority = models.IntegerField(blank=True, null=True)
    o_comment = models.CharField(max_length=79, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Part(models.Model):
    p_partkey = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=55, blank=True, null=True)
    p_mfgr = models.CharField(max_length=25, blank=True, null=True)
    p_brand = models.CharField(max_length=10, blank=True, null=True)
    p_type = models.CharField(max_length=25, blank=True, null=True)
    p_size = models.IntegerField(blank=True, null=True)
    p_container = models.CharField(max_length=10, blank=True, null=True)
    p_retailprice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_comment = models.CharField(max_length=23, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'


class Partsupp(models.Model):
    ps_partkey = models.BigIntegerField()
    ps_suppkey = models.BigIntegerField()
    ps_availqty = models.IntegerField(blank=True, null=True)
    ps_supplycost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ps_comment = models.CharField(max_length=199, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partsupp'
        unique_together = (('ps_partkey', 'ps_suppkey'),)


class Region(models.Model):
    r_regionkey = models.AutoField(primary_key=True)
    r_name = models.CharField(max_length=25, blank=True, null=True)
    r_comment = models.CharField(max_length=152, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class Supplier(models.Model):
    s_suppkey = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=25, blank=True, null=True)
    s_address = models.CharField(max_length=40, blank=True, null=True)
    s_nationkey = models.BigIntegerField()
    s_phone = models.CharField(max_length=15, blank=True, null=True)
    s_acctbal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    s_comment = models.CharField(max_length=101, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'
