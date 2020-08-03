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
from openapi_client.models.external_analysis_import_infos import ExternalAnalysisImportInfos  # noqa: E501
from openapi_client.rest import ApiException

class TestExternalAnalysisImportInfos(unittest.TestCase):
    """ExternalAnalysisImportInfos unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExternalAnalysisImportInfos
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.external_analysis_import_infos.ExternalAnalysisImportInfos()  # noqa: E501
        if include_optional :
            return ExternalAnalysisImportInfos(
                infos = [
                    openapi_client.models.external_analysis_import_info_object.ExternalAnalysisImportInfoObject(
                        uniform_path = '0', 
                        partition = '0', 
                        report_uniform_path = '0', 
                        type = '0', )
                    ]
            )
        else :
            return ExternalAnalysisImportInfos(
        )

    def testExternalAnalysisImportInfos(self):
        """Test ExternalAnalysisImportInfos"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
