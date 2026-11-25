import unittest

from materials import list_feeds, read_feed

FIELDS = {
    'cells': ('device', 'fault_domain', 'capacity', 'warm_min', 'services'),
    'coverage': ('service', 'peak_min', 'load', 'min_domains'),
    'jobs': ('job', 'crew', 'all_devices', 'earliest', 'latest', 'duration_min', 'rank'),
    'timeline': ('received', 'occurred', 'kind', 'job', 'device', 'permit', 'value'),
}


class MaterialTest(unittest.TestCase):
    def test_feed_fields(self):
        self.assertEqual(list_feeds(), sorted(FIELDS))
        for name, fields in FIELDS.items():
            with self.subTest(feed=name):
                records = list(read_feed(name))
                self.assertTrue(records)
                self.assertTrue(all(set(row) == set(fields) for row in records))
