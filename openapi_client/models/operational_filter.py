# coding: utf-8

"""
    MSK-MIND REST API

    MSK-MIND REST API  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class OperationalFilter(object):
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
        'dmp_ids': 'list[str]',
        'file_type': 'str',
        'create_time': 'date'
    }

    attribute_map = {
        'dmp_ids': 'dmpIds',
        'file_type': 'fileType',
        'create_time': 'createTime'
    }

    def __init__(self, dmp_ids=None, file_type=None, create_time=None, local_vars_configuration=None):  # noqa: E501
        """OperationalFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dmp_ids = None
        self._file_type = None
        self._create_time = None
        self.discriminator = None

        if dmp_ids is not None:
            self.dmp_ids = dmp_ids
        if file_type is not None:
            self.file_type = file_type
        if create_time is not None:
            self.create_time = create_time

    @property
    def dmp_ids(self):
        """Gets the dmp_ids of this OperationalFilter.  # noqa: E501


        :return: The dmp_ids of this OperationalFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._dmp_ids

    @dmp_ids.setter
    def dmp_ids(self, dmp_ids):
        """Sets the dmp_ids of this OperationalFilter.


        :param dmp_ids: The dmp_ids of this OperationalFilter.  # noqa: E501
        :type: list[str]
        """

        self._dmp_ids = dmp_ids

    @property
    def file_type(self):
        """Gets the file_type of this OperationalFilter.  # noqa: E501


        :return: The file_type of this OperationalFilter.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this OperationalFilter.


        :param file_type: The file_type of this OperationalFilter.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def create_time(self):
        """Gets the create_time of this OperationalFilter.  # noqa: E501


        :return: The create_time of this OperationalFilter.  # noqa: E501
        :rtype: date
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this OperationalFilter.


        :param create_time: The create_time of this OperationalFilter.  # noqa: E501
        :type: date
        """

        self._create_time = create_time

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
        if not isinstance(other, OperationalFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperationalFilter):
            return True

        return self.to_dict() != other.to_dict()
