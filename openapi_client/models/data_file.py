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


class DataFile(object):
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
        'id': 'str',
        'path': 'str',
        'type': 'str',
        'create_time': 'date'
    }

    attribute_map = {
        'id': 'id',
        'path': 'path',
        'type': 'type',
        'create_time': 'createTime'
    }

    def __init__(self, id=None, path=None, type=None, create_time=None, local_vars_configuration=None):  # noqa: E501
        """DataFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._path = None
        self._type = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this DataFile.  # noqa: E501


        :return: The id of this DataFile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataFile.


        :param id: The id of this DataFile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this DataFile.  # noqa: E501


        :return: The path of this DataFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DataFile.


        :param path: The path of this DataFile.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def type(self):
        """Gets the type of this DataFile.  # noqa: E501


        :return: The type of this DataFile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataFile.


        :param type: The type of this DataFile.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLINICAL", "MOLECULAR", "IMAGE", "IMAGE_HNE", "IMAGE_CT", "IMAGE_MRI"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def create_time(self):
        """Gets the create_time of this DataFile.  # noqa: E501


        :return: The create_time of this DataFile.  # noqa: E501
        :rtype: date
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataFile.


        :param create_time: The create_time of this DataFile.  # noqa: E501
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
        if not isinstance(other, DataFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataFile):
            return True

        return self.to_dict() != other.to_dict()
