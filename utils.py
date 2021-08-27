from datetime import datetime


def get_screenshot_name(request):
    date_time_str = str(datetime.now()).replace(":", "_").replace(".", "_")
    screenshot_name = request.node.name + date_time_str
    return screenshot_name
