import unittest

from materials import read_feed


class InputsTest(unittest.TestCase):
    def test_interacting_work_and_shared_cells(self):
        cells = {r["device"]: r for r in read_feed("cells")}
        events = list(read_feed("timeline"))
        jobs = {r["job"]: r for r in read_feed("jobs")}
        for work in jobs.values():
            self.assertLess(work["earliest"], work["latest"])
            self.assertTrue(set(work["all_devices"]) <= cells.keys())
        grant = next(r for r in events if r["kind"] == "lease_expired")
        start = next(r for r in events if r["job"] == grant["job"] and r["kind"] == "work_started")
        self.assertEqual(start["permit"], grant["permit"])
        self.assertGreater(start["received"], grant["received"])
        moved = next(r for r in events if r["job"] == "m21" and r["kind"] == "route_active")
        self.assertIn(moved["device"], jobs["m22"]["all_devices"])
        self.assertGreater(len(cells[moved["device"]]["services"]), 1)

