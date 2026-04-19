# ESPHome ITHO CC1101 External Component

This is an ESPHome external component for controlling ITHO Eco Fan devices via the CC1101 radio module.

## Component Architecture

This project follows the [ESPHome Component Architecture](https://developers.esphome.io/architecture/components/) guidelines for external components.

### Directory Structure

```
components/
└── ithoc1101/
    ├── __init__.py           # Python configuration layer
    ├── IthoCC1101.h          # Main component header
    ├── IthoCC1101.cpp        # Main component implementation
    ├── CC1101.h              # CC1101 radio driver header
    ├── CC1101.cpp            # CC1101 radio driver implementation
    ├── CC1101Packet.h        # Radio packet structures
    ├── IthoPacket.h          # ITHO protocol structures
    └── README.md             # Component documentation
```

### C++ Namespace

All C++ code is properly namespaced under `esphome::ithoc1101` to follow ESPHome conventions and prevent naming conflicts.

### Python Integration

The `__init__.py` file provides:
- **CONFIG_SCHEMA**: Defines configuration options available in YAML
  - `counter` (0-255): Initial counter value for the remote
  - `send_tries` (1-10): Number of retries when sending commands
- **to_code()**: Generates C++ code from the YAML configuration
- **Enums**: Maps human-readable command names to C++ enum values

### C++ Component Lifecycle

The main `IthoCC1101` class inherits from `esphome::Component` and implements:
- **setup()**: Initializes the CC1101 radio and receives mode
- **loop()**: Checks for incoming packets from ITHO devices
- **dump_config()**: Logs configuration during startup

## Usage

### 1. Add to your ESPHome configuration

Create or edit your `configuration.yaml`:

```yaml
external_components:
  - source: github://supersjimmie/ESPHome_ITHO_Eco_Fan_CC1101
    components: [ithoc1101]

ithoc1101:
  counter: 0
  send_tries: 3
```

### 2. Hardware Requirements

- ESP8266 or ESP32 microcontroller
- CC1101 radio module connected via SPI
- Proper GPIO pin configuration for SPI (MISO, MOSI, CLK, CS)

### 3. Build and Flash

```bash
esphome run configuration.yaml
```

## Component Methods

### Public Methods

- `setup()` - Initialize component (called once at startup)
- `loop()` - Check for incoming packets (called continuously)
- `dump_config()` - Log configuration values
- `checkForNewPacket()` - Check if new packet received
- `getLastPacket()` - Get the last received packet
- `getLastCommand()` - Get the last received command
- `sendCommand(IthoCommand cmd)` - Send a command
- `ReadRSSI()` - Read signal strength

### Supported Commands

The component supports all ITHO Eco Fan commands:
- `standby`
- `low`
- `medium`
- `high`
- `full`
- `timer1`, `timer2`, `timer3`
- `join`, `leave`

Plus DUCO remote commands:
- `duco_standby`
- `duco_low`
- `duco_medium`
- `duco_high`

## ESPHome Standards Compliance

This component follows ESPHome best practices:

✅ Proper C++ namespace organization  
✅ Component lifecycle methods (setup, loop, dump_config)  
✅ Configuration validation via CONFIG_SCHEMA  
✅ Logging with appropriate tags and levels  
✅ Non-blocking code in loop()  
✅ Python codegen integration  

## Contributing

When modifying this component, please maintain compliance with ESPHome architecture:

1. Keep C++ code in the `esphome::ithoc1101` namespace
2. Implement all required lifecycle methods
3. Use ESPHome logging (ESP_LOGI, ESP_LOGCONFIG, ESP_LOGE)
4. Update both C++ headers and Python integration
5. Test with `esphome run` before submitting changes

## References

- [ESPHome Component Architecture](https://developers.esphome.io/architecture/components/)
- [ESPHome Codegen Documentation](https://developers.esphome.io/architecture/components/)
- [ITHO Eco Fan Protocol Documentation](components/ithoc1101/README.md)
