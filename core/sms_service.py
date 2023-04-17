import requests

from apps.main.models import Settings


def sms_to_phone(phone='', message=''):
    s = Settings.objects.first()
    if phone == '':
        phone = s.admin_phone
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjQ3MCwicm9sZSI6InVzZXIiLCJkYXRhIjp7ImlkIjo0NzAsIm5hbWUiOiJPT08gXHUyMDFjQXVyYSBUcmFkZSBDb21wYW55XHUyMDFkIiwiZW1haWwiOiJzYW12ZWwxNi4wMy4xOTcxQGdtYWlsLmNvbSIsInJvbGUiOiJ1c2VyIiwiYXBpX3Rva2VuIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SnpkV0lpT2pRM01Dd2ljbTlzWlNJNkluVnpaWElpTENKa1lYUmhJanA3SW1sa0lqbzBOekFzSW01aGJXVWlPaUpQVDA4Z1hIVXlNREZqUVhWeVlTQlVjbUZrWlNCRGIyMXdZVzU1WEhVeU1ERmtJaXdpWlcxaGFXd2lPaUp6WVcxMlpXd3hOaTR3TXk0eE9UY3hRR2R0WVdsc0xtTnZiU0lzSW5KdmJHVWlPaUoxYzJWeUlpd2lZWEJwWDNSdmEyVnVJam9pWlhsS01HVllRV2xQYVVwTFZqIiwic3RhdHVzIjoiYWN0aXZlIiwic21zX2FwaV9sb2dpbiI6ImVza2l6MiIsInNtc19hcGlfcGFzc3dvcmQiOiJlJCRrIXoiLCJ1el9wcmljZSI6NTAsInVjZWxsX3ByaWNlIjoxMTUsInRlc3RfdWNlbGxfcHJpY2UiOjExNSwiYmFsYW5jZSI6Mjg0NjUwLCJpc192aXAiOjAsImhvc3QiOiJzZXJ2ZXIxIiwiY3JlYXRlZF9hdCI6IjIwMjEtMDQtMDhUMDk6MzA6NDIuMDAwMDAwWiIsInVwZGF0ZWRfYXQiOiIyMDIyLTA4LTA1VDE2OjU1OjE5LjAwMDAwMFoiLCJ3aGl0ZWxpc3QiOm51bGx9LCJpYXQiOjE2ODE3MDQyMDAsImV4cCI6MTY4NDI5NjIwMH0.WEFIR855fnmRXsKYnrG0KBBw3TRAwsVUbi9LUgzdw6E"
    url = "http://notify.eskiz.uz/api/message/sms/send"
    payload = {'mobile_phone': str(phone),
               'message': f'{message}',
               'from': '4546'}
    headers = {'Authorization': f'Bearer {token}'}

    requests.request("POST", url, headers=headers, data=payload, files={})
