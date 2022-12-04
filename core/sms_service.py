import requests

from apps.main.models import Settings


def sms_to_phone(phone='', message=''):
    s = Settings.objects.first()
    if phone == '':
        phone = s.admin_phone
    # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgzMSwicm9sZSI6InVzZXIiLCJkYXRhIjp7ImlkIjo4MzEsIm5hbWUiOiJcdTA0MWVcdTA0MWVcdTA0MWUgWFRSRU1FLVRFQ0giLCJlbWFpbCI6ImN1c3RvbXBjZ2FtaW5nMUBnbWFpbC5jb20iLCJyb2xlIjoidXNlciIsImFwaV90b2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUp6ZFdJaU9qZ3pNU3dpY205c1pTSTZJblZ6WlhJaUxDSmtZWFJoSWpwN0ltbGtJam80TXpFc0ltNWhiV1VpT2lKY2RUQTBNV1ZjZFRBME1XVmNkVEEwTVdVZ1dGUlNSVTFGTFZSRlEwZ2lMQ0psYldGcGJDSTZJbU4xYzNSdmJYQmpaMkZ0YVc1bk1VQm5iV0ZwYkM1amIyMGlMQ0p5YjJ4bElqb2lkWE5sY2lJc0ltRndhVjkwYjJ0bGJpSTZJbVY1U2pCbFdFRnBUMmxLUzFZeFVXbE1RMCIsInN0YXR1cyI6ImFjdGl2ZSIsInNtc19hcGlfbG9naW4iOiJlc2tpejIiLCJzbXNfYXBpX3Bhc3N3b3JkIjoiZSQkayF6IiwidXpfcHJpY2UiOjUwLCJ1Y2VsbF9wcmljZSI6MTE1LCJiYWxhbmNlIjoyMTE0MDUsImlzX3ZpcCI6MCwiaG9zdCI6InNlcnZlcjEiLCJjcmVhdGVkX2F0IjoiMjAyMi0wNC0yOVQxNjowMDozNS4wMDAwMDBaIiwidXBkYXRlZF9hdCI6IjIwMjItMTAtMjZUMTc6MTM6NDkuMDAwMDAwWiJ9LCJpYXQiOjE2NjY4MDQ1NDMsImV4cCI6MTY2OTM5NjU0M30.H6RHfyt2u16gDH-1ZmEU8T4lKzzrCR-HCWXQZ_hMfvQ"
    url = "http://notify.eskiz.uz/api/message/sms/send"
    payload = {'mobile_phone': str(phone),
               'message': f'{message}',
               'from': '4546'}
    headers = {'Authorization': f'Bearer {s.token}'}

    requests.request("POST", url, headers=headers, data=payload, files={})
