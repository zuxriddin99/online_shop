import datetime

import requests
from django_cron import CronJobBase, Schedule

# from apps.main.models import Settings
from apps.products.models import Brand


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'core.my_cron_job'  # a unique code

    def do(self):
        headers = {}
        files = {}
        url = 'https://notify.eskiz.uz/api/auth/login'
        payload = {'email': 'custompcgaming1@gmail.com',
                   'password': '5kxq5WOjtQp4PGf53IbO1QejyuQD8fUJ5LtLM1qF'}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        resp = response.json()
        # setting, _ = Settings.objects.get_or_create(id=1)
        # print(setting)
        # print(resp['data']['token'])
        # setting.token = resp['data']['token']
        # setting.save()
