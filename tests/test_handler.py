import unittest
from proxy_alarms.handler import _get_type_message


class TestProcess(unittest.TestCase):
    def test_message_is_cloud_connector(self):
        #Assume
        message: dict = {"var1": "1", "var2": "2"}
        #Action
        response = _get_type_message(message)
        #Assert
        self.assertTrue(response)
