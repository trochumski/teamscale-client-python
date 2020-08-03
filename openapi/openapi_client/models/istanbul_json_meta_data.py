# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class IstanbulJsonMetaData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'program_version': 'str',
        'partition': 'str'
    }

    attribute_map = {
        'program_version': '__programVersion',
        'partition': '__partition'
    }

    def __init__(self, program_version=None, partition=None, local_vars_configuration=None):  # noqa: E501
        """IstanbulJsonMetaData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._program_version = None
        self._partition = None
        self.discriminator = None

        if program_version is not None:
            self.program_version = program_version
        if partition is not None:
            self.partition = partition

    @property
    def program_version(self):
        """Gets the program_version of this IstanbulJsonMetaData.  # noqa: E501


        :return: The program_version of this IstanbulJsonMetaData.  # noqa: E501
        :rtype: str
        """
        return self._program_version

    @program_version.setter
    def program_version(self, program_version):
        """Sets the program_version of this IstanbulJsonMetaData.


        :param program_version: The program_version of this IstanbulJsonMetaData.  # noqa: E501
        :type: str
        """

        self._program_version = program_version

    @property
    def partition(self):
        """Gets the partition of this IstanbulJsonMetaData.  # noqa: E501


        :return: The partition of this IstanbulJsonMetaData.  # noqa: E501
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this IstanbulJsonMetaData.


        :param partition: The partition of this IstanbulJsonMetaData.  # noqa: E501
        :type: str
        """

        self._partition = partition

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IstanbulJsonMetaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IstanbulJsonMetaData):
            return True

        return self.to_dict() != other.to_dict()
