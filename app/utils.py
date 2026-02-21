from datetime import datetime
from flask import current_app
import functools

def add_status_tag(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = f"[SUCCESS] {func(*args, **kwargs)}"
        except Exception as e:
            result = "[FAILURE]"
            current_app.logger.exception(f"Error in {func.__name__}: {str(e)}")
        return result
    return wrapper

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class TimeManager(metaclass=SingletonMeta):
    def __init__(self):
        self.version = "1.0.0"

    @add_status_tag
    def format_current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @add_status_tag
    def format_current_time_inverted(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
class MathManager(metaclass=SingletonMeta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @add_status_tag
    def divide(self, a, b):
        return float(a) / float(b)
    
class SuperManager(TimeManager, MathManager):
    _call_successful_count = 0

    def get_full_report(self, a, b):
        result = self.divide(a, b)
        time = self.format_current_time()
        report = {
            'result': result,
            'time': time,
            'utility_version': self.version
        }
        if "SUCCESS" in result:
            SuperManager._call_successful_count += 1
        return report

    def get_successful_reports(self):
        return {'successful_reports': SuperManager._call_successful_count}
