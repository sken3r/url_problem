from functools import wraps

from .. import backend


def trace_view_operation(func):
    """Creates a span for decorated functions for Views"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        backend.create_or_update_trace_operation_for_path(args[0].path)
        return func(*args, **kwargs)

    return wrapper
