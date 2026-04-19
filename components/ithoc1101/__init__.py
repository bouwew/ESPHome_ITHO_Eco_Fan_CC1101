"""ESPHome external component for ITHO CC1101 fan control."""

import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID

# Define constants for configuration keys
CONF_COUNTER = "counter"
CONF_SEND_TRIES = "send_tries"

# Create namespace for this component
ithoc1101_ns = cg.esphome_ns.namespace("ithoc1101")

# Define the main component class
IthoCC1101 = ithoc1101_ns.class_("IthoCC1101", cg.Component)

# Define the command enum
IthoCommand = ithoc1101_ns.enum("IthoCommand")
ITHO_COMMANDS = {
    "unknown": IthoCommand.IthoUnknown,
    "join": IthoCommand.IthoJoin,
    "leave": IthoCommand.IthoLeave,
    "standby": IthoCommand.IthoStandby,
    "low": IthoCommand.IthoLow,
    "medium": IthoCommand.IthoMedium,
    "high": IthoCommand.IthoHigh,
    "full": IthoCommand.IthoFull,
    "timer1": IthoCommand.IthoTimer1,
    "timer2": IthoCommand.IthoTimer2,
    "timer3": IthoCommand.IthoTimer3,
    "duco_standby": IthoCommand.DucoStandby,
    "duco_low": IthoCommand.DucoLow,
    "duco_medium": IthoCommand.DucoMedium,
    "duco_high": IthoCommand.DucoHigh,
}

# Define configuration schema for YAML validation
CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(IthoCC1101),
        cv.Optional(CONF_COUNTER, default=0): cv.int_range(0, 255),
        cv.Optional(CONF_SEND_TRIES, default=3): cv.int_range(1, 10),
    }
)


async def to_code(config):
    """Generate C++ code for this component."""
    # Create new IthoCC1101 instance with configuration parameters
    var = cg.new_Pvariable(
        config[CONF_ID], config[CONF_COUNTER], config[CONF_SEND_TRIES]
    )

    # Register the component so setup/loop methods are called
    await cg.register_component(var, config)
