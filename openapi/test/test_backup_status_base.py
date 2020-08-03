# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.backup_status_base import BackupStatusBase  # noqa: E501
from openapi_client.rest import ApiException

class TestBackupStatusBase(unittest.TestCase):
    """BackupStatusBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BackupStatusBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.backup_status_base.BackupStatusBase()  # noqa: E501
        if include_optional :
            return BackupStatusBase(
                status = 'IN_PROGRESS', 
                status_message = '0', 
                logs = [
                    openapi_client.models.logging_event_transport.LoggingEventTransport(
                        message = '0', 
                        level = 'ALL', 
                        time = 56, )
                    ], 
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return BackupStatusBase(
        )

    def testBackupStatusBase(self):
        """Test BackupStatusBase"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
