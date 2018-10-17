# -*- coding: utf-8 -*-
# Auto-generated by Stone, do not modify.
# @generated
# flake8: noqa
# pylint: skip-file
try:
    from . import stone_validators as bv
    from . import stone_base as bb
except (ImportError, SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import stone_validators as bv
    import stone_base as bb

try:
    from . import (
        common,
    )
except (ImportError, SystemError, ValueError):
    import common

class GroupManagementType(bb.Union):
    """
    The group type determines how a group is managed.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar user_managed: A group which is managed by selected users.
    :ivar company_managed: A group which is managed by team admins only.
    :ivar system_managed: A group which is managed automatically by Dropbox.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    user_managed = None
    # Attribute is overwritten below the class definition
    company_managed = None
    # Attribute is overwritten below the class definition
    system_managed = None
    # Attribute is overwritten below the class definition
    other = None

    def is_user_managed(self):
        """
        Check if the union tag is ``user_managed``.

        :rtype: bool
        """
        return self._tag == 'user_managed'

    def is_company_managed(self):
        """
        Check if the union tag is ``company_managed``.

        :rtype: bool
        """
        return self._tag == 'company_managed'

    def is_system_managed(self):
        """
        Check if the union tag is ``system_managed``.

        :rtype: bool
        """
        return self._tag == 'system_managed'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def _process_custom_annotations(self, annotation_type, processor):
        super(GroupManagementType, self)._process_custom_annotations(annotation_type, processor)

    def __repr__(self):
        return 'GroupManagementType(%r, %r)' % (self._tag, self._value)

GroupManagementType_validator = bv.Union(GroupManagementType)

class GroupSummary(bb.Struct):
    """
    Information about a group.

    :ivar group_external_id: External ID of group. This is an arbitrary ID that
        an admin can attach to a group.
    :ivar member_count: The number of members in the group.
    :ivar group_management_type: Who is allowed to manage the group.
    """

    __slots__ = [
        '_group_name_value',
        '_group_name_present',
        '_group_id_value',
        '_group_id_present',
        '_group_external_id_value',
        '_group_external_id_present',
        '_member_count_value',
        '_member_count_present',
        '_group_management_type_value',
        '_group_management_type_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 group_name=None,
                 group_id=None,
                 group_management_type=None,
                 group_external_id=None,
                 member_count=None):
        self._group_name_value = None
        self._group_name_present = False
        self._group_id_value = None
        self._group_id_present = False
        self._group_external_id_value = None
        self._group_external_id_present = False
        self._member_count_value = None
        self._member_count_present = False
        self._group_management_type_value = None
        self._group_management_type_present = False
        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if group_external_id is not None:
            self.group_external_id = group_external_id
        if member_count is not None:
            self.member_count = member_count
        if group_management_type is not None:
            self.group_management_type = group_management_type

    @property
    def group_name(self):
        """
        :rtype: str
        """
        if self._group_name_present:
            return self._group_name_value
        else:
            raise AttributeError("missing required field 'group_name'")

    @group_name.setter
    def group_name(self, val):
        val = self._group_name_validator.validate(val)
        self._group_name_value = val
        self._group_name_present = True

    @group_name.deleter
    def group_name(self):
        self._group_name_value = None
        self._group_name_present = False

    @property
    def group_id(self):
        """
        :rtype: str
        """
        if self._group_id_present:
            return self._group_id_value
        else:
            raise AttributeError("missing required field 'group_id'")

    @group_id.setter
    def group_id(self, val):
        val = self._group_id_validator.validate(val)
        self._group_id_value = val
        self._group_id_present = True

    @group_id.deleter
    def group_id(self):
        self._group_id_value = None
        self._group_id_present = False

    @property
    def group_external_id(self):
        """
        External ID of group. This is an arbitrary ID that an admin can attach
        to a group.

        :rtype: str
        """
        if self._group_external_id_present:
            return self._group_external_id_value
        else:
            return None

    @group_external_id.setter
    def group_external_id(self, val):
        if val is None:
            del self.group_external_id
            return
        val = self._group_external_id_validator.validate(val)
        self._group_external_id_value = val
        self._group_external_id_present = True

    @group_external_id.deleter
    def group_external_id(self):
        self._group_external_id_value = None
        self._group_external_id_present = False

    @property
    def member_count(self):
        """
        The number of members in the group.

        :rtype: long
        """
        if self._member_count_present:
            return self._member_count_value
        else:
            return None

    @member_count.setter
    def member_count(self, val):
        if val is None:
            del self.member_count
            return
        val = self._member_count_validator.validate(val)
        self._member_count_value = val
        self._member_count_present = True

    @member_count.deleter
    def member_count(self):
        self._member_count_value = None
        self._member_count_present = False

    @property
    def group_management_type(self):
        """
        Who is allowed to manage the group.

        :rtype: GroupManagementType
        """
        if self._group_management_type_present:
            return self._group_management_type_value
        else:
            raise AttributeError("missing required field 'group_management_type'")

    @group_management_type.setter
    def group_management_type(self, val):
        self._group_management_type_validator.validate_type_only(val)
        self._group_management_type_value = val
        self._group_management_type_present = True

    @group_management_type.deleter
    def group_management_type(self):
        self._group_management_type_value = None
        self._group_management_type_present = False

    def _process_custom_annotations(self, annotation_type, processor):
        super(GroupSummary, self)._process_custom_annotations(annotation_type, processor)

    def __repr__(self):
        return 'GroupSummary(group_name={!r}, group_id={!r}, group_management_type={!r}, group_external_id={!r}, member_count={!r})'.format(
            self._group_name_value,
            self._group_id_value,
            self._group_management_type_value,
            self._group_external_id_value,
            self._member_count_value,
        )

GroupSummary_validator = bv.Struct(GroupSummary)

class GroupType(bb.Union):
    """
    The group type determines how a group is created and managed.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar team: A group to which team members are automatically added.
        Applicable to `team folders <https://www.dropbox.com/help/986>`_ only.
    :ivar user_managed: A group is created and managed by a user.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    team = None
    # Attribute is overwritten below the class definition
    user_managed = None
    # Attribute is overwritten below the class definition
    other = None

    def is_team(self):
        """
        Check if the union tag is ``team``.

        :rtype: bool
        """
        return self._tag == 'team'

    def is_user_managed(self):
        """
        Check if the union tag is ``user_managed``.

        :rtype: bool
        """
        return self._tag == 'user_managed'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def _process_custom_annotations(self, annotation_type, processor):
        super(GroupType, self)._process_custom_annotations(annotation_type, processor)

    def __repr__(self):
        return 'GroupType(%r, %r)' % (self._tag, self._value)

GroupType_validator = bv.Union(GroupType)

class MemberSpaceLimitType(bb.Union):
    """
    The type of the space limit imposed on a team member.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar off: The team member does not have imposed space limit.
    :ivar alert_only: The team member has soft imposed space limit - the limit
        is used for display and for notifications.
    :ivar stop_sync: The team member has hard imposed space limit - Dropbox file
        sync will stop after the limit is reached.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    off = None
    # Attribute is overwritten below the class definition
    alert_only = None
    # Attribute is overwritten below the class definition
    stop_sync = None
    # Attribute is overwritten below the class definition
    other = None

    def is_off(self):
        """
        Check if the union tag is ``off``.

        :rtype: bool
        """
        return self._tag == 'off'

    def is_alert_only(self):
        """
        Check if the union tag is ``alert_only``.

        :rtype: bool
        """
        return self._tag == 'alert_only'

    def is_stop_sync(self):
        """
        Check if the union tag is ``stop_sync``.

        :rtype: bool
        """
        return self._tag == 'stop_sync'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def _process_custom_annotations(self, annotation_type, processor):
        super(MemberSpaceLimitType, self)._process_custom_annotations(annotation_type, processor)

    def __repr__(self):
        return 'MemberSpaceLimitType(%r, %r)' % (self._tag, self._value)

MemberSpaceLimitType_validator = bv.Union(MemberSpaceLimitType)

class TimeRange(bb.Struct):
    """
    Time range.

    :ivar start_time: Optional starting time (inclusive).
    :ivar end_time: Optional ending time (exclusive).
    """

    __slots__ = [
        '_start_time_value',
        '_start_time_present',
        '_end_time_value',
        '_end_time_present',
    ]

    _has_required_fields = False

    def __init__(self,
                 start_time=None,
                 end_time=None):
        self._start_time_value = None
        self._start_time_present = False
        self._end_time_value = None
        self._end_time_present = False
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def start_time(self):
        """
        Optional starting time (inclusive).

        :rtype: datetime.datetime
        """
        if self._start_time_present:
            return self._start_time_value
        else:
            return None

    @start_time.setter
    def start_time(self, val):
        if val is None:
            del self.start_time
            return
        val = self._start_time_validator.validate(val)
        self._start_time_value = val
        self._start_time_present = True

    @start_time.deleter
    def start_time(self):
        self._start_time_value = None
        self._start_time_present = False

    @property
    def end_time(self):
        """
        Optional ending time (exclusive).

        :rtype: datetime.datetime
        """
        if self._end_time_present:
            return self._end_time_value
        else:
            return None

    @end_time.setter
    def end_time(self, val):
        if val is None:
            del self.end_time
            return
        val = self._end_time_validator.validate(val)
        self._end_time_value = val
        self._end_time_present = True

    @end_time.deleter
    def end_time(self):
        self._end_time_value = None
        self._end_time_present = False

    def _process_custom_annotations(self, annotation_type, processor):
        super(TimeRange, self)._process_custom_annotations(annotation_type, processor)

    def __repr__(self):
        return 'TimeRange(start_time={!r}, end_time={!r})'.format(
            self._start_time_value,
            self._end_time_value,
        )

TimeRange_validator = bv.Struct(TimeRange)

GroupExternalId_validator = bv.String()
GroupId_validator = bv.String()
MemberExternalId_validator = bv.String(max_length=64)
ResellerId_validator = bv.String()
TeamMemberId_validator = bv.String()
GroupManagementType._user_managed_validator = bv.Void()
GroupManagementType._company_managed_validator = bv.Void()
GroupManagementType._system_managed_validator = bv.Void()
GroupManagementType._other_validator = bv.Void()
GroupManagementType._tagmap = {
    'user_managed': GroupManagementType._user_managed_validator,
    'company_managed': GroupManagementType._company_managed_validator,
    'system_managed': GroupManagementType._system_managed_validator,
    'other': GroupManagementType._other_validator,
}

GroupManagementType.user_managed = GroupManagementType('user_managed')
GroupManagementType.company_managed = GroupManagementType('company_managed')
GroupManagementType.system_managed = GroupManagementType('system_managed')
GroupManagementType.other = GroupManagementType('other')

GroupSummary._group_name_validator = bv.String()
GroupSummary._group_id_validator = GroupId_validator
GroupSummary._group_external_id_validator = bv.Nullable(GroupExternalId_validator)
GroupSummary._member_count_validator = bv.Nullable(bv.UInt32())
GroupSummary._group_management_type_validator = GroupManagementType_validator
GroupSummary._all_field_names_ = set([
    'group_name',
    'group_id',
    'group_external_id',
    'member_count',
    'group_management_type',
])
GroupSummary._all_fields_ = [
    ('group_name', GroupSummary._group_name_validator),
    ('group_id', GroupSummary._group_id_validator),
    ('group_external_id', GroupSummary._group_external_id_validator),
    ('member_count', GroupSummary._member_count_validator),
    ('group_management_type', GroupSummary._group_management_type_validator),
]

GroupType._team_validator = bv.Void()
GroupType._user_managed_validator = bv.Void()
GroupType._other_validator = bv.Void()
GroupType._tagmap = {
    'team': GroupType._team_validator,
    'user_managed': GroupType._user_managed_validator,
    'other': GroupType._other_validator,
}

GroupType.team = GroupType('team')
GroupType.user_managed = GroupType('user_managed')
GroupType.other = GroupType('other')

MemberSpaceLimitType._off_validator = bv.Void()
MemberSpaceLimitType._alert_only_validator = bv.Void()
MemberSpaceLimitType._stop_sync_validator = bv.Void()
MemberSpaceLimitType._other_validator = bv.Void()
MemberSpaceLimitType._tagmap = {
    'off': MemberSpaceLimitType._off_validator,
    'alert_only': MemberSpaceLimitType._alert_only_validator,
    'stop_sync': MemberSpaceLimitType._stop_sync_validator,
    'other': MemberSpaceLimitType._other_validator,
}

MemberSpaceLimitType.off = MemberSpaceLimitType('off')
MemberSpaceLimitType.alert_only = MemberSpaceLimitType('alert_only')
MemberSpaceLimitType.stop_sync = MemberSpaceLimitType('stop_sync')
MemberSpaceLimitType.other = MemberSpaceLimitType('other')

TimeRange._start_time_validator = bv.Nullable(common.DropboxTimestamp_validator)
TimeRange._end_time_validator = bv.Nullable(common.DropboxTimestamp_validator)
TimeRange._all_field_names_ = set([
    'start_time',
    'end_time',
])
TimeRange._all_fields_ = [
    ('start_time', TimeRange._start_time_validator),
    ('end_time', TimeRange._end_time_validator),
]

ROUTES = {
}

