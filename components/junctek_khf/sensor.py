import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import (
    CONF_RAW,
    CONF_ID,
    CONF_ADDRESS,
    CONF_INPUT,
    CONF_NUMBER,
    CONF_HARDWARE_UART,
    CONF_TEMPERATURE,
    CONF_VOLTAGE,
    CONF_CURRENT,
    CONF_BATTERY_LEVEL,
    CONF_POWER, 

   
    DEVICE_CLASS_VOLTAGE,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_NONE,
    UNIT_VOLT,
    UNIT_CELSIUS,
    UNIT_AMPERE,
    UNIT_WATT,
    UNIT_WATT_HOURS,
    UNIT_MINUTE,
    UNIT_PERCENT,
    UNIT_SECOND,
    ICON_EMPTY,
    ICON_THERMOMETER,
    ICON_FLASH,
    ICON_PERCENT,
    ICON_BATTERY,
    ICON_EMPTY,
    ICON_POWER,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_POWER,
)

CONF_AH_BATTERY_LEVEL="ah_battery_level"
CONF_WH_BATTERY_DISCHAGE="wh_discharge"
CONF_WH_BATTERY_LEVEL="wh_battery_level"
CONF_RUNNING_TIME="running_time"
CONF_BATTERY_LIFE="battery_life"
CONF_RELAY_STATUS="relay_status"
CONF_DIRECTION="direction"
CONF_TIME_ADJ="time_adjustment"
CONF_OVERVOLTAGE_SET="over_voltage_set"
CONF_UNDERVOLTAGE_SET="under_voltage_set"
CONF_POSITIVE_OVERCURENT_SET="positive_overcurrent_set"
CONF_NEGATIVE_OVERCURENT_SET="negative_overcurrent_set"
CONF_OVER_POWER_PROTECTION_SET="over_power_protection_set"
CONF_OVER_TEMPERATURE_PROTECTION_SET="over_temperature_set"
CONF_PROTECTION_RECOVERY_SECOND_SET="protection_recovery_seconds_set"
CONF_DELAY_TIME_SET="delay_time_set"
CONF_BATTERY_AMPHOUR_CAPACITY_SET="battery_amphour_capacity_set"
CONF_VOLTAGE_CALIBRATION_SET="voltage_calibration_set"
CONF_CURRENT_CALIBRATION_SET="current_calibration_set"
CONF_TEMPERATURE_CALIBRATION_SET="temperature_calibration_set"
CONF_RESERVED_SET="reserved_set"
CONF_RELAY_NORMALY_OPEN="relay_normally_open"
CONF_CURRENT_RATIO_SET="current_ratio_set"

UNIT_AMPERE_HEURE="AH"
UNIT_WATT_HEURE="WH"


DEPENDENCIES = ["uart"]

AUTO_LOAD = ["sensor"]

TYPES = [
    CONF_VOLTAGE,
    CONF_CURRENT,
    CONF_BATTERY_LEVEL,
    CONF_TEMPERATURE,
    CONF_POWER, 
    CONF_AH_BATTERY_LEVEL,
    CONF_WH_BATTERY_DISCHAGE,
    CONF_WH_BATTERY_LEVEL,
    CONF_RUNNING_TIME,
    CONF_TIME_ADJ,
    CONF_BATTERY_LIFE,
    CONF_RELAY_STATUS,
    CONF_DIRECTION,
    CONF_OVERVOLTAGE_SET,
    CONF_UNDERVOLTAGE_SET,
    CONF_POSITIVE_OVERCURENT_SET,
    CONF_NEGATIVE_OVERCURENT_SET,
    CONF_OVER_POWER_PROTECTION_SET,
    CONF_OVER_TEMPERATURE_PROTECTION_SET,
    CONF_PROTECTION_RECOVERY_SECOND_SET,
    CONF_DELAY_TIME_SET,
    CONF_BATTERY_AMPHOUR_CAPACITY_SET,
    CONF_VOLTAGE_CALIBRATION_SET,
    CONF_CURRENT_CALIBRATION_SET,
    CONF_TEMPERATURE_CALIBRATION_SET,
    CONF_RESERVED_SET,
    CONF_RELAY_NORMALY_OPEN,
    CONF_CURRENT_RATIO_SET,
]

CONF_INVERT_CURRENT="invert_current"

JuncTekKGF = cg.global_ns.class_(
    "JuncTekKHF", cg.Component, uart.UARTDevice
)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(JuncTekKGF),
            cv.Optional(CONF_ADDRESS, default=1): cv.int_range(1, 255),
            cv.Optional(CONF_VOLTAGE): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                icon=ICON_FLASH,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                icon="mdi:current-dc",
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_BATTERY_LEVEL): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                icon=ICON_PERCENT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_POWER): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                icon=ICON_POWER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_AH_BATTERY_LEVEL): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE_HEURE,
                icon=ICON_BATTERY,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_WH_BATTERY_DISCHAGE): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HEURE,
                icon=ICON_BATTERY,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_WH_BATTERY_LEVEL): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HEURE,
                icon=ICON_BATTERY,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_RUNNING_TIME): sensor.sensor_schema(
                unit_of_measurement=UNIT_SECOND,
                icon=ICON_BATTERY,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_BATTERY_LIFE): sensor.sensor_schema(
                unit_of_measurement=UNIT_MINUTE,
                icon=ICON_BATTERY,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_RELAY_STATUS): sensor.sensor_schema(
                icon=ICON_EMPTY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_NONE,
            ),
             cv.Optional(CONF_DIRECTION): sensor.sensor_schema(
                icon=ICON_EMPTY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_NONE,
            ),
             cv.Optional(CONF_OVERVOLTAGE_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_UNDERVOLTAGE_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_POSITIVE_OVERCURENT_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                icon=ICON_EMPTY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_NEGATIVE_OVERCURENT_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                icon=ICON_EMPTY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_OVER_POWER_PROTECTION_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                icon=ICON_FLASH,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_OVER_TEMPERATURE_PROTECTION_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_PROTECTION_RECOVERY_SECOND_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                icon=ICON_BATTERY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_DELAY_TIME_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                icon=ICON_EMPTY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_BATTERY_AMPHOUR_CAPACITY_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE_HEURE,
                icon=ICON_BATTERY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_VOLTAGE_CALIBRATION_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                icon=ICON_BATTERY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_CURRENT_CALIBRATION_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                icon=ICON_BATTERY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_TEMPERATURE_CALIBRATION_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_EMPTY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_RESERVED_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                icon=ICON_THERMOMETER,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_RELAY_NORMALY_OPEN): sensor.sensor_schema(
                icon=ICON_EMPTY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_CURRENT_RATIO_SET): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                icon=ICON_BATTERY,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_TIME_ADJ): sensor.sensor_schema(
                icon=CLOCK,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_INVERT_CURRENT, default=False): cv.boolean, 
        }
    ).extend(uart.UART_DEVICE_SCHEMA)
    )

async def setup_conf(config, key, hub):
    if key in config:
        conf = config[key]
        sens = await sensor.new_sensor(conf)
        cg.add(getattr(hub, f"set_{key}_sensor")(sens))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_ADDRESS], config[CONF_INVERT_CURRENT])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
    for key in TYPES:
        await setup_conf(config, key, var)
