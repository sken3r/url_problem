from ..models import TraceOperation


def create_or_update_trace_operation_for_path(path: str) -> TraceOperation:
    trace_operation, created = TraceOperation.objects.get_or_create(view_path=path)

    if not created:
        trace_operation.hit_count += 1
        trace_operation.save()

    return trace_operation
