/*
 * Author: Klusjesman, modified bij supersjimmie for Arduino/ESP8266
 * Refactored as ESPHome external component
 */

#pragma once

#include <stdio.h>
#ifdef ESP8266
#include <Arduino.h>
#endif

namespace esphome::ithoc1101 {

#define CC1101_BUFFER_LEN        64
#define CC1101_DATA_LEN          CC1101_BUFFER_LEN - 3


class CC1101Packet
{
	public:
		uint8_t length;
		uint8_t data[72];
};

}  // namespace esphome::ithoc1101

