from datetime import datetime, date
from pytz import timezone

from apscheduler.schedulers.background import BackgroundScheduler

from assessment.models import Assessment, Question, Answer, Result_set
from account.models import User


def check_for_new_assesments():
    print("scheduler working")
    d = datetime.now(timezone('US/Eastern'))
    fmt = '%Y-%m-%d'
    d = d.strftime(fmt)
    assessment_list = Assessment.objects.all()
    for i in assessment_list:
        print(i.name, i.start_date, d, str(i.start_date) == d )
        if str(i.start_date) == d:
            print("Email  will be sent")
        else:
            print("no assignment")



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_for_new_assesments, 'interval', seconds=1)
    scheduler.start()
