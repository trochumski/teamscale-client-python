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


class FormDataMultiPart(object):
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
        'content_disposition': 'ContentDisposition',
        'entity': 'object',
        'headers': 'dict(str, list[str])',
        'media_type': 'BodyPartMediaType',
        'message_body_workers': 'object',
        'parent': 'MultiPart',
        'providers': 'object',
        'body_parts': 'list[BodyPart]'
    }

    attribute_map = {
        'content_disposition': 'contentDisposition',
        'entity': 'entity',
        'headers': 'headers',
        'media_type': 'mediaType',
        'message_body_workers': 'messageBodyWorkers',
        'parent': 'parent',
        'providers': 'providers',
        'body_parts': 'bodyParts'
    }

    def __init__(self, content_disposition=None, entity=None, headers=None, media_type=None, message_body_workers=None, parent=None, providers=None, body_parts=None, local_vars_configuration=None):  # noqa: E501
        """FormDataMultiPart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content_disposition = None
        self._entity = None
        self._headers = None
        self._media_type = None
        self._message_body_workers = None
        self._parent = None
        self._providers = None
        self._body_parts = None
        self.discriminator = None

        if content_disposition is not None:
            self.content_disposition = content_disposition
        if entity is not None:
            self.entity = entity
        if headers is not None:
            self.headers = headers
        if media_type is not None:
            self.media_type = media_type
        if message_body_workers is not None:
            self.message_body_workers = message_body_workers
        if parent is not None:
            self.parent = parent
        if providers is not None:
            self.providers = providers
        if body_parts is not None:
            self.body_parts = body_parts

    @property
    def content_disposition(self):
        """Gets the content_disposition of this FormDataMultiPart.  # noqa: E501


        :return: The content_disposition of this FormDataMultiPart.  # noqa: E501
        :rtype: ContentDisposition
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition):
        """Sets the content_disposition of this FormDataMultiPart.


        :param content_disposition: The content_disposition of this FormDataMultiPart.  # noqa: E501
        :type: ContentDisposition
        """

        self._content_disposition = content_disposition

    @property
    def entity(self):
        """Gets the entity of this FormDataMultiPart.  # noqa: E501


        :return: The entity of this FormDataMultiPart.  # noqa: E501
        :rtype: object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this FormDataMultiPart.


        :param entity: The entity of this FormDataMultiPart.  # noqa: E501
        :type: object
        """

        self._entity = entity

    @property
    def headers(self):
        """Gets the headers of this FormDataMultiPart.  # noqa: E501


        :return: The headers of this FormDataMultiPart.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this FormDataMultiPart.


        :param headers: The headers of this FormDataMultiPart.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._headers = headers

    @property
    def media_type(self):
        """Gets the media_type of this FormDataMultiPart.  # noqa: E501


        :return: The media_type of this FormDataMultiPart.  # noqa: E501
        :rtype: BodyPartMediaType
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this FormDataMultiPart.


        :param media_type: The media_type of this FormDataMultiPart.  # noqa: E501
        :type: BodyPartMediaType
        """

        self._media_type = media_type

    @property
    def message_body_workers(self):
        """Gets the message_body_workers of this FormDataMultiPart.  # noqa: E501


        :return: The message_body_workers of this FormDataMultiPart.  # noqa: E501
        :rtype: object
        """
        return self._message_body_workers

    @message_body_workers.setter
    def message_body_workers(self, message_body_workers):
        """Sets the message_body_workers of this FormDataMultiPart.


        :param message_body_workers: The message_body_workers of this FormDataMultiPart.  # noqa: E501
        :type: object
        """

        self._message_body_workers = message_body_workers

    @property
    def parent(self):
        """Gets the parent of this FormDataMultiPart.  # noqa: E501


        :return: The parent of this FormDataMultiPart.  # noqa: E501
        :rtype: MultiPart
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this FormDataMultiPart.


        :param parent: The parent of this FormDataMultiPart.  # noqa: E501
        :type: MultiPart
        """

        self._parent = parent

    @property
    def providers(self):
        """Gets the providers of this FormDataMultiPart.  # noqa: E501


        :return: The providers of this FormDataMultiPart.  # noqa: E501
        :rtype: object
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """Sets the providers of this FormDataMultiPart.


        :param providers: The providers of this FormDataMultiPart.  # noqa: E501
        :type: object
        """

        self._providers = providers

    @property
    def body_parts(self):
        """Gets the body_parts of this FormDataMultiPart.  # noqa: E501


        :return: The body_parts of this FormDataMultiPart.  # noqa: E501
        :rtype: list[BodyPart]
        """
        return self._body_parts

    @body_parts.setter
    def body_parts(self, body_parts):
        """Sets the body_parts of this FormDataMultiPart.


        :param body_parts: The body_parts of this FormDataMultiPart.  # noqa: E501
        :type: list[BodyPart]
        """

        self._body_parts = body_parts

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
        if not isinstance(other, FormDataMultiPart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormDataMultiPart):
            return True

        return self.to_dict() != other.to_dict()
