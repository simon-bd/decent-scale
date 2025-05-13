from homeassistant.components.sensor import SensorEntity
from homeassistant.const import MASS_GRAMS
from homeassistant.helpers.entity import Entity

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([DecentScaleSensor()])

class DecentScaleSensor(SensorEntity):
    _attr_name = "Decent Scale Weight"
    _attr_native_unit_of_measurement = MASS_GRAMS
    _attr_state_class = "measurement"
    _attr_device_class = "weight"

    def __init__(self):
        self._attr_native_value = None

    def update(self):
        # Placeholder for now — integrate with pydecentscale later
        self._attr_native_value = 0.0
