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
from openapi_client.models.findings_filter_settings import FindingsFilterSettings  # noqa: E501
from openapi_client.rest import ApiException

class TestFindingsFilterSettings(unittest.TestCase):
    """FindingsFilterSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FindingsFilterSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.findings_filter_settings.FindingsFilterSettings()  # noqa: E501
        if include_optional :
            return FindingsFilterSettings(
                commit = 'a', 
                regex_filter = '0', 
                exclude_regex_filter = True, 
                filter_findings_added_to_tasks = True, 
                category_and_groups_filters = [
                    '0'
                    ], 
                invert_category_and_groups_filters = True, 
                assessment_filters = [
                    'RED'
                    ], 
                blacklisting_option = 'EXCLUDED', 
                baseline = '0', 
                qualified_name = '0', 
                include_changed_code_findings = True, 
                blacklist_rationale_filter = '0'
            )
        else :
            return FindingsFilterSettings(
        )

    def testFindingsFilterSettings(self):
        """Test FindingsFilterSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
