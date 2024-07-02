from django.http import HttpRequest

from tracker.models import UserData


def get_user_data(request: HttpRequest) -> dict:
    http_sec = request.META['HTTP_SEC_CH_UA']
    ip_address = request.META['REMOTE_ADDR']
    browser = get_browser(http_sec)
    data = {
        "ip_address": ip_address,
        "browser": browser,
    }
    return data


def get_browser(http_sec: str) -> str:
    """Get proper name for a browser"""
    browser = http_sec.split(";")[0]
    if browser == '"Not/A)Brand"':
        browser = http_sec.split(";")[2].split(",")[1]
    return browser.strip(' "')


def enter_user_data_to_db(data: dict) -> None:
    UserData.objects.create(**data)
