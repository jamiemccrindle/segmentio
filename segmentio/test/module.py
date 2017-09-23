import unittest

import segmentio


class TestModule(unittest.TestCase):

    def failed(self):
        self.failed = True

    def setUp(self):
        self.failed = False
        segmentio.write_key = 'testsecret'
        segmentio.on_error = self.failed

    def test_no_write_key(self):
        segmentio.write_key = None
        self.assertRaises(Exception, segmentio.track)

    def test_no_host(self):
        segmentio.host = None
        self.assertRaises(Exception, segmentio.track)

    def test_track(self):
        segmentio.track('userId', 'python module event')
        segmentio.flush()

    def test_identify(self):
        segmentio.identify('userId', { 'email': 'user@email.com' })
        segmentio.flush()

    def test_group(self):
        segmentio.group('userId', 'groupId')
        segmentio.flush()

    def test_alias(self):
        segmentio.alias('previousId', 'userId')
        segmentio.flush()

    def test_page(self):
        segmentio.page('userId')
        segmentio.flush()

    def test_screen(self):
        segmentio.screen('userId')
        segmentio.flush()

    def test_flush(self):
        segmentio.flush()
