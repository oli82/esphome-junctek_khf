#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"

using namespace esphome;

class JuncTekKHF
  : public esphome::Component
  , public uart::UARTDevice
{
public:
  JuncTekKHF(unsigned address = 1, bool invert_current=false);

  void set_voltage_sensor(sensor::Sensor *voltage_sensor) { voltage_sensor_ = voltage_sensor; }
  void set_current_sensor(sensor::Sensor *current_sensor) { current_sensor_ = current_sensor; }
  void set_temperature_sensor(sensor::Sensor *temperature) { temperature_ = temperature; }
  void set_ah_battery_level_sensor(sensor::Sensor *ah_battery_level_sensor) { ah_battery_level_sensor_ = ah_battery_level_sensor; }
  void set_wh_battery_discharge_sensor(sensor::Sensor *wh_battery_discharge_sensor) { wh_battery_discharge_sensor_ = wh_battery_discharge_sensor; }
  void set_wh_battery_level_sensor(sensor::Sensor *wh_battery_level_sensor) { wh_battery_level_sensor_ = wh_battery_level_sensor; }
  void set_running_time_sensor(sensor::Sensor *running_time_sensor) { running_time_sensor_ = running_time_sensor; }
  void set_battery_life_sensor(sensor::Sensor *battery_life_sensor) { battery_life_sensor_ = battery_life_sensor; }
  void set_power_sensor(sensor::Sensor *power_sensor) { power_sensor_ = power_sensor; }
  void set_battery_level_sensor(sensor::Sensor *battery_level_sensor) { battery_level_sensor_ = battery_level_sensor; }
  void set_relay_status_sensor(sensor::Sensor *relay_status_sensor) { relay_status_sensor_ = relay_status_sensor; }
  void set_direction_sensor(sensor::Sensor *direction_sensor) { direction_sensor_ = direction_sensor; }
  void set_over_voltage_set_sensor(sensor::Sensor *over_voltage_set_sensor) { over_voltage_set_sensor_ = over_voltage_set_sensor; }
  void set_under_voltage_set_sensor(sensor::Sensor *under_voltage_set_sensor) { under_voltage_set_sensor_ = under_voltage_set_sensor; }
  void set_positive_overcurrent_set_sensor(sensor::Sensor *positive_overcurrent_set_sensor) { positive_overcurrent_set_sensor_ = positive_overcurrent_set_sensor; }
  void set_negative_overcurrent_set_sensor(sensor::Sensor *negative_overcurrent_set_sensor) { negative_overcurrent_set_sensor_ = negative_overcurrent_set_sensor; }
  void set_over_power_protection_set_sensor(sensor::Sensor *over_power_protection_set_sensor) { over_power_protection_set_sensor_ = over_power_protection_set_sensor; }
  void set_over_temperature_set_sensor(sensor::Sensor *over_temperature_set_sensor) { over_temperature_set_sensor_ = over_temperature_set_sensor; }
  void set_protection_recovery_seconds_set_sensor(sensor::Sensor *protection_recovery_seconds_set_sensor) { protection_recovery_seconds_set_sensor_ = protection_recovery_seconds_set_sensor; }
  void set_delay_time_set_sensor(sensor::Sensor *delay_time_set_sensor) { delay_time_set_sensor_ = delay_time_set_sensor; }
  void set_battery_amphour_capacity_set_sensor(sensor::Sensor *battery_amphour_capacity_set_sensor) { battery_amphour_capacity_set_sensor_ = battery_amphour_capacity_set_sensor; }
  void set_voltage_calibration_set_sensor(sensor::Sensor *voltage_calibration_set_sensor) { voltage_calibration_set_sensor_ = voltage_calibration_set_sensor; }
  void set_current_calibration_set_sensor(sensor::Sensor *current_calibration_set_sensor) { current_calibration_set_sensor_ = current_calibration_set_sensor; }
  void set_temperature_calibration_set_sensor(sensor::Sensor *temperature_calibration_set_sensor) { temperature_calibration_set_sensor_ = temperature_calibration_set_sensor; }
  void set_reserved_set_sensor(sensor::Sensor *reserved_set_sensor) { reserved_set_sensor_ = reserved_set_sensor; }
  void set_relay_normally_open_sensor(sensor::Sensor *relay_normally_open_sensor) { relay_normally_open_sensor_ = relay_normally_open_sensor; }
  void set_current_ratio_set_sensor(sensor::Sensor *current_ratio_set_sensor) { current_ratio_set_sensor_ = current_ratio_set_sensor; }
  void set_xx_sensor(sensor::Sensor *xx_sensor) { xx_sensor_ = xx_sensor; }


  void dump_config() override;
  void loop() override;

  float get_setup_priority() const;// override;

protected:
  bool readline();
  void handle_line();
  void handle_status(const char* buffer);
  void handle_settings(const char* buffer);
  void request_data(uint8_t data_id);
  void decode_data(std::vector<uint8_t> data);
  bool verify_checksum(int checksum, const char* buffer);

  const unsigned address_;

  sensor::Sensor* voltage_sensor_{nullptr};
  sensor::Sensor* current_sensor_{nullptr};
  sensor::Sensor* battery_level_sensor_{nullptr};
  sensor::Sensor* temperature_{nullptr};
  sensor::Sensor* power_sensor_{nullptr};
  sensor::Sensor* ah_battery_level_sensor_{nullptr};
  sensor::Sensor* wh_battery_discharge_sensor_{nullptr};
  sensor::Sensor* wh_battery_level_sensor_{nullptr};
  sensor::Sensor* running_time_sensor_{nullptr};
  sensor::Sensor* battery_life_sensor_{nullptr};
  sensor::Sensor* relay_status_sensor_{nullptr};
  sensor::Sensor* direction_sensor_{nullptr};
  sensor::Sensor* over_voltage_set_sensor_{nullptr};
  sensor::Sensor* under_voltage_set_sensor_{nullptr};
  sensor::Sensor* positive_overcurrent_set_sensor_{nullptr};
  sensor::Sensor* negative_overcurrent_set_sensor_{nullptr};
  sensor::Sensor* over_power_protection_set_sensor_{nullptr};
  sensor::Sensor* over_temperature_set_sensor_{nullptr};

  sensor::Sensor* protection_recovery_seconds_set_sensor_{nullptr};

  sensor::Sensor* delay_time_set_sensor_{nullptr};
  sensor::Sensor* battery_amphour_capacity_set_sensor_{nullptr};
  sensor::Sensor* voltage_calibration_set_sensor_{nullptr};
  sensor::Sensor* current_calibration_set_sensor_{nullptr};
  sensor::Sensor* temperature_calibration_set_sensor_{nullptr};
  sensor::Sensor* reserved_set_sensor_{nullptr};
  sensor::Sensor* relay_normally_open_sensor_{nullptr};
  sensor::Sensor* current_ratio_set_sensor_{nullptr};
  sensor::Sensor* xx_sensor_{nullptr};


  static constexpr int MAX_LINE_LEN = 120;
  std::array<char, MAX_LINE_LEN> line_buffer_;
  size_t line_pos_ = 0;

  optional<float> battery_capacity_;
  optional<unsigned long> last_settings_;
  optional<unsigned long> last_stats_;
  bool invert_current_;
};
