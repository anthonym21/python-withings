"""Asynchronous Python client for Withings."""

from .exceptions import (
    WithingsAuthenticationFailedError,
    WithingsBadStateError,
    WithingsConnectionError,
    WithingsError,
    WithingsErrorOccurredError,
    WithingsInvalidParamsError,
    WithingsTooManyRequestsError,
    WithingsUnauthorizedError,
    WithingsUnknownStatusError,
)
from .helpers import aggregate_measurements
from .models import (
    Device,
    DeviceBattery,
    DeviceModel,
    DeviceType,
    Goals,
    Measurement,
    MeasurementGroup,
    MeasurementGroupAttribution,
    MeasurementGroupCategory,
    MeasurementType,
    NotificationCategory,
    Services,
    WebhookCall,
    get_measurement_type_from_notification_category,
)
from .withings import WithingsClient

__all__ = [
    "DeviceBattery",
    "Device",
    "DeviceType",
    "DeviceModel",
    "WithingsError",
    "WithingsConnectionError",
    "WithingsAuthenticationFailedError",
    "WithingsInvalidParamsError",
    "WithingsUnauthorizedError",
    "WithingsErrorOccurredError",
    "WithingsBadStateError",
    "WithingsTooManyRequestsError",
    "WithingsUnknownStatusError",
    "WithingsClient",
    "Goals",
    "MeasurementGroupAttribution",
    "MeasurementGroupCategory",
    "MeasurementGroup",
    "MeasurementType",
    "Measurement",
    "get_measurement_type_from_notification_category",
    "aggregate_measurements",
    "NotificationCategory",
    "Services",
    "WebhookCall",
]
