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
from openapi_client.models.backup_job_summary import BackupJobSummary  # noqa: E501
from openapi_client.rest import ApiException

class TestBackupJobSummary(unittest.TestCase):
    """BackupJobSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BackupJobSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.backup_job_summary.BackupJobSummary()  # noqa: E501
        if include_optional :
            return BackupJobSummary(
                key = '0', 
                start_timestamp = 56, 
                status = 'IN_PROGRESS'
            )
        else :
            return BackupJobSummary(
        )

    def testBackupJobSummary(self):
        """Test BackupJobSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
