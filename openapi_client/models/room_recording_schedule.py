# coding: utf-8

"""
    vc_webapi

    Web API for the Virtual Classroom project  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: 237294@via.dk
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RoomRecordingSchedule(object):
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
        'valid_from': 'datetime',
        'valid_to': 'datetime',
        'scheduled_sessions': 'list[ScheduledSession]'
    }

    attribute_map = {
        'valid_from': 'validFrom',
        'valid_to': 'validTo',
        'scheduled_sessions': 'scheduledSessions'
    }

    def __init__(self, valid_from=None, valid_to=None, scheduled_sessions=None):  # noqa: E501
        """RoomRecordingSchedule - a model defined in OpenAPI"""  # noqa: E501

        self._valid_from = None
        self._valid_to = None
        self._scheduled_sessions = None
        self.discriminator = None

        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to
        self.scheduled_sessions = scheduled_sessions

    @property
    def valid_from(self):
        """Gets the valid_from of this RoomRecordingSchedule.  # noqa: E501


        :return: The valid_from of this RoomRecordingSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this RoomRecordingSchedule.


        :param valid_from: The valid_from of this RoomRecordingSchedule.  # noqa: E501
        :type: datetime
        """

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this RoomRecordingSchedule.  # noqa: E501


        :return: The valid_to of this RoomRecordingSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this RoomRecordingSchedule.


        :param valid_to: The valid_to of this RoomRecordingSchedule.  # noqa: E501
        :type: datetime
        """

        self._valid_to = valid_to

    @property
    def scheduled_sessions(self):
        """Gets the scheduled_sessions of this RoomRecordingSchedule.  # noqa: E501


        :return: The scheduled_sessions of this RoomRecordingSchedule.  # noqa: E501
        :rtype: list[ScheduledSession]
        """
        return self._scheduled_sessions

    @scheduled_sessions.setter
    def scheduled_sessions(self, scheduled_sessions):
        """Sets the scheduled_sessions of this RoomRecordingSchedule.


        :param scheduled_sessions: The scheduled_sessions of this RoomRecordingSchedule.  # noqa: E501
        :type: list[ScheduledSession]
        """

        self._scheduled_sessions = scheduled_sessions

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
        if not isinstance(other, RoomRecordingSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
