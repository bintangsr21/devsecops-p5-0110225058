import os
import tempfile
import unittest

from taskmanager.manager import TaskManager
from taskmanager.storage import JsonStorage


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.path)
        self.manager = TaskManager(JsonStorage(self.path))

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add_task(self):
        t = self.manager.add("Belajar DevSecOps", "high")
        self.assertEqual(t.id, 1)
        self.assertEqual(len(self.manager.list()), 1)

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add("   ")

    def test_invalid_priority_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add("Tugas", "urgent")

    def test_complete_task(self):
        t = self.manager.add("Tugas A")
        self.manager.complete(t.id)
        self.assertEqual(self.manager.list(only_pending=True), [])

    def test_remove_task(self):
        t = self.manager.add("Tugas B")
        self.manager.remove(t.id)
        self.assertEqual(len(self.manager.list()), 0)

    def test_remove_unknown_id(self):
        with self.assertRaises(KeyError):
            self.manager.remove(99)


if __name__ == "__main__":
    unittest.main()