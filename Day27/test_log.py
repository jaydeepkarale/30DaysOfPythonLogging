import unittest
import example


class MyTestCase(unittest.TestCase):
    def test_logging(self):
        with self.assertLogs('demo_logger', level='DEBUG') as lc:
            example.check_status('Open')
            self.assertEqual(['DEBUG:demo_logger:Good status'], lc.output)
            example.check_status('Bad')
            self.assertEqual(['DEBUG:demo_logger:Good status','ERROR:demo_logger:Unknown status: Bad'], lc.output)


if __name__ == '__main__':
    unittest.main()
