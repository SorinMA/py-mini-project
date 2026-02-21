from flask import Blueprint, request

from app.utils import SuperManager, TimeManager

main = Blueprint('main', __name__)

@main.route('/current-time')
def current_time():
    timer = TimeManager()
    return {
        "timestamp": timer.format_current_time(),
        "utility_version": timer.version
    }

@main.route('/current-time-inverted')
def current_time_inverted():
    timer = TimeManager()
    return {
        "timestamp": timer.format_current_time_inverted(),
        "utility_version": timer.version
    }

@main.route('/calculate')
def calculate():
    a = request.args.get('a', default=0, type=int)
    b = request.args.get('b', default=0, type=int)
    manager = SuperManager()
    report = manager.get_full_report(a, b)
    return report

@main.route('/reports-stats')
def reports_stats():
    manager = SuperManager()
    return manager.get_successful_reports()