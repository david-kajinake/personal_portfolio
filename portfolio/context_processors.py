from .models import MyEmail , MyPhoneNumber
import time
def get_time(): 
    local_time = time.localtime()
    current_hour = local_time.tm_hour
    currnt_minute = local_time.tm_min
    current_second = local_time.tm_sec
    return f"{current_hour}{currnt_minute}{current_second}"

def css_js_version(request):
    full_time = get_time()
    return{
        "css_version": full_time , 
        "js_version": full_time
    }

def contacts(request):
    primary_phone_number = MyPhoneNumber.objects.all().first()
    primary_email_address = MyEmail.objects.all().first()
    return{
        "primary_phone_number": primary_phone_number , 
        "primary_email_address": primary_email_address
    }


