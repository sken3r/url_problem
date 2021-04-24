from django.test import TestCase

from ....backend import create_or_update_trace_operation_for_path
from ....models import TraceOperation


class ViewsTestCase(TestCase):
    def setUp(self):
        self.path = "http://wwww.example.com"
        TraceOperation(view_path=self.path).save()

    def test_shorten_url(self):
        create_or_update_trace_operation_for_path(self.path)

        trace_operations = TraceOperation.objects.all()
        assert len(trace_operations) == 1
        assert trace_operations[0].hit_count == 2
        assert trace_operations[0].view_path == "http://wwww.example.com"
