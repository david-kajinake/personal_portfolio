import time
local_time = time.localtime()
current_hour = local_time.tm_hour
currnt_minute = local_time.tm_min
current_second = local_time.tm_sec
def css_js_version(request):
    full_time = f"{current_hour}{currnt_minute}{current_second}"
    return{
        "css_version": full_time , 
        "js_version": full_time
    }
