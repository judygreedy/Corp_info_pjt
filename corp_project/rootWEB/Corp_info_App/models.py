from django.db import models

# Create your models here.

class corp_information(models.Model):
    CORP_CODE = models.IntegerField(db_column='corp_code', primary_key=True)  # Field name made lowercase.
    CORP_NAME = models.CharField(db_column='corp_name', max_length=50)  # Field name made lowercase.
    CORP_IND = models.CharField(db_column='corp_ind', max_length=50)  # Field name made lowerca
    CORP_SM = models.IntegerField(db_column='corp_sm')
    CORP_M = models.FloatField(db_column='corp_m')
    CORP_AUG = models.FloatField(db_column='corp_aug')
    CORP_SAL = models.IntegerField(db_column='corp_sal')
    CORP_SALES = models.BigIntegerField(db_column='corp_sales')
    CORP_OPE = models.BigIntegerField(db_column='corp_ope')
    FIN_GRO = models.FloatField(db_column='fin_gro')
    FIN_STA = models.FloatField(db_column='fin_sta')
    FIN_PRO = models.FloatField(db_column='fin_pro')
    FIN_ACT = models.FloatField(db_column='fin_act')
    CAREER = models.FloatField(db_column='career')
    WL_BALANCE = models.FloatField(db_column='wl_balance')
    WELFARE = models.FloatField(db_column='welfare')
    CULTURE = models.FloatField(db_column='culture')
    MANAGEMENT = models.FloatField(db_column='management')
    CLUSTER = models.IntegerField(db_column='cluster')