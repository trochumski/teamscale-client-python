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


class User(object):
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
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email_address': 'str',
        'authenticator': 'str',
        'gravatar_hash': 'str',
        'use_gravatar': 'bool',
        'aliases': 'list[str]',
        'group_ids': 'list[str]'
    }

    attribute_map = {
        'username': 'username',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email_address': 'emailAddress',
        'authenticator': 'authenticator',
        'gravatar_hash': 'gravatarHash',
        'use_gravatar': 'useGravatar',
        'aliases': 'aliases',
        'group_ids': 'groupIds'
    }

    def __init__(self, username=None, first_name=None, last_name=None, email_address=None, authenticator=None, gravatar_hash=None, use_gravatar=None, aliases=None, group_ids=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._authenticator = None
        self._gravatar_hash = None
        self._use_gravatar = None
        self._aliases = None
        self._group_ids = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address
        if authenticator is not None:
            self.authenticator = authenticator
        if gravatar_hash is not None:
            self.gravatar_hash = gravatar_hash
        if use_gravatar is not None:
            self.use_gravatar = use_gravatar
        if aliases is not None:
            self.aliases = aliases
        if group_ids is not None:
            self.group_ids = group_ids

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501


        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.


        :param username: The username of this User.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this User.  # noqa: E501


        :return: The email_address of this User.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this User.


        :param email_address: The email_address of this User.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def authenticator(self):
        """Gets the authenticator of this User.  # noqa: E501


        :return: The authenticator of this User.  # noqa: E501
        :rtype: str
        """
        return self._authenticator

    @authenticator.setter
    def authenticator(self, authenticator):
        """Sets the authenticator of this User.


        :param authenticator: The authenticator of this User.  # noqa: E501
        :type: str
        """

        self._authenticator = authenticator

    @property
    def gravatar_hash(self):
        """Gets the gravatar_hash of this User.  # noqa: E501


        :return: The gravatar_hash of this User.  # noqa: E501
        :rtype: str
        """
        return self._gravatar_hash

    @gravatar_hash.setter
    def gravatar_hash(self, gravatar_hash):
        """Sets the gravatar_hash of this User.


        :param gravatar_hash: The gravatar_hash of this User.  # noqa: E501
        :type: str
        """

        self._gravatar_hash = gravatar_hash

    @property
    def use_gravatar(self):
        """Gets the use_gravatar of this User.  # noqa: E501


        :return: The use_gravatar of this User.  # noqa: E501
        :rtype: bool
        """
        return self._use_gravatar

    @use_gravatar.setter
    def use_gravatar(self, use_gravatar):
        """Sets the use_gravatar of this User.


        :param use_gravatar: The use_gravatar of this User.  # noqa: E501
        :type: bool
        """

        self._use_gravatar = use_gravatar

    @property
    def aliases(self):
        """Gets the aliases of this User.  # noqa: E501


        :return: The aliases of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this User.


        :param aliases: The aliases of this User.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def group_ids(self):
        """Gets the group_ids of this User.  # noqa: E501


        :return: The group_ids of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this User.


        :param group_ids: The group_ids of this User.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
