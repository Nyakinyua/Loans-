from .views import *
import cronjobs

@cronjobs.register
def my_cron_job():
    interest_cal