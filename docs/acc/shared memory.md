# ACC Shared Memory Reference

## Zweck

Dieses Dokument beschreibt die von `pyaccsharedmemory` bereitgestellten Shared-Memory-Daten von Assetto Corsa Competizione.

Es dient als Referenz für:

* Reader
* Parser
* DTOs
* Mapper

und soll verhindern, dass Feldnamen erneut recherchiert werden müssen.

---

# Top-Level

```text
SharedMemory
├── Physics
├── Graphics
└── Static
```

---

# Parser-Zuordnung

| Parser                 | Quelle            |
| ---------------------- | ----------------- |
| DriverInputsParser     | Physics           |
| VehicleStateParser     | Physics           |
| VehicleDynamicsParser  | Physics           |
| WheelParser            | Physics           |
| SessionStateParser     | Graphics          |
| EnvironmentStateParser | Graphics + Static |

---

# Physics

| Feld                 | Typ          | Verwendet | DTO                         |
| -------------------- | ------------ | --------- | --------------------------- |
| abs                  | float        | ❌         |                             |
| abs_vibration        | float        | ❌         |                             |
| air_temp             | float        | ❌         |                             |
| autoshifter_on       | bool         | ❌         |                             |
| brake                | float        | ✅         | DriverInputs.brake          |
| brake_bias           | float        | ❌         |                             |
| brake_pressure       | Wheels       | ❌         |                             |
| brake_temp           | Wheels       | ❌         |                             |
| car_damage           | CarDamage    | ❌         |                             |
| clutch               | float        | ✅         | DriverInputs.clutch         |
| disc_life            | Wheels       | ❌         |                             |
| final_ff             | float        | ❌         |                             |
| front_brake_compound | int          | ❌         |                             |
| fuel                 | float        | ✅         | VehicleState.fuel           |
| g_force              | Vector3f     | ❌         |                             |
| g_vibration          | float        | ❌         |                             |
| gas                  | float        | ✅         | DriverInputs.throttle       |
| gear                 | int          | ✅         | DriverInputs.gear           |
| heading              | float        | ❌         |                             |
| ignition_on          | bool         | ✅         | VehicleState.ignition_on    |
| is_ai_controlled     | bool         | ❌         |                             |
| is_engine_running    | bool         | ✅         | VehicleState.engine_running |
| kerb_vibration       | float        | ❌         |                             |
| local_angular_vel    | Vector3f     | ❌         |                             |
| local_velocity       | Vector3f     | ❌         |                             |
| packed_id            | int          | ❌         |                             |
| pad_life             | Wheels       | ❌         |                             |
| pit_limiter_on       | bool         | ❌         |                             |
| pitch                | float        | ❌         |                             |
| rear_brake_compound  | int          | ❌         |                             |
| road_temp            | float        | ❌         |                             |
| roll                 | float        | ❌         |                             |
| rpm                  | int          | ✅         | VehicleState.rpm            |
| slip_angle           | Wheels       | ❌         |                             |
| slip_ratio           | Wheels       | ❌         |                             |
| slip_vibration       | float        | ❌         |                             |
| speed_kmh            | float        | ✅         | VehicleState.speed          |
| starter_engine_on    | bool         | ❌         |                             |
| steer_angle          | float        | ✅         | DriverInputs.steering       |
| suspension_damage    | Wheels       | ❌         |                             |
| suspension_travel    | Wheels       | ❌         |                             |
| tc                   | float        | ❌         |                             |
| turbo_boost          | float        | ❌         |                             |
| tyre_contact_heading | ContactPoint | ❌         |                             |
| tyre_contact_normal  | ContactPoint | ❌         |                             |
| tyre_contact_point   | ContactPoint | ❌         |                             |
| tyre_core_temp       | Wheels       | ❌         |                             |
| velocity             | Vector3f     | ❌         |                             |
| water_temp           | float        | ❌         |                             |
| wheel_angular_s      | Wheels       | ❌         |                             |
| wheel_pressure       | Wheels       | ❌         |                             |
| wheel_slip           | Wheels       | ❌         |                             |

---

# Graphics

| Feld                         | Typ                   | Verwendet  |
| ---------------------------- | --------------------- | ---------- |
| abs_level                    | int                   | ❌          |
| active_cars                  | int                   | ❌          |
| best_time                    | int                   | ❌          |
| best_time_str                | str                   | ❌          |
| car_coordinates              | list                  | ❌          |
| car_id                       | tuple                 | ❌          |
| clock                        | float                 | ❌          |
| completed_lap                | int                   | 🟡 geplant |
| current_sector_index         | int                   | ❌          |
| current_time                 | int                   | ❌          |
| current_time_str             | str                   | ❌          |
| current_tyre_set             | int                   | ❌          |
| delta_lap_time               | int                   | ❌          |
| delta_lap_time_str           | str                   | ❌          |
| direction_light_left         | bool                  | ❌          |
| direction_light_right        | bool                  | ❌          |
| distance_traveled            | float                 | ❌          |
| driver_stint_time_left       | int                   | ❌          |
| driver_stint_total_time_left | int                   | ❌          |
| engine_map                   | int                   | ❌          |
| estimated_lap_time           | int                   | ❌          |
| estimated_lap_time_str       | str                   | ❌          |
| exhaust_temp                 | float                 | ❌          |
| flag                         | ACC_FLAG_TYPE         | ❌          |
| flashing_light               | bool                  | ❌          |
| fuel_estimated_laps          | float                 | ❌          |
| fuel_per_lap                 | float                 | ❌          |
| gap_ahead                    | int                   | ❌          |
| gap_behind                   | int                   | ❌          |
| global_chequered             | bool                  | ❌          |
| global_green                 | bool                  | ❌          |
| global_red                   | bool                  | ❌          |
| global_white                 | bool                  | ❌          |
| global_yellow                | bool                  | ❌          |
| global_yellow_s1             | bool                  | ❌          |
| global_yellow_s2             | bool                  | ❌          |
| global_yellow_s3             | bool                  | ❌          |
| ideal_line_on                | bool                  | ❌          |
| is_delta_positive            | bool                  | ❌          |
| is_in_pit                    | bool                  | ❌          |
| is_in_pit_lane               | bool                  | ❌          |
| is_setup_menu_visible        | bool                  | ❌          |
| is_valid_lap                 | bool                  | ❌          |
| last_sector_time             | int                   | ❌          |
| last_sector_time_str         | int                   | ❌          |
| last_time                    | int                   | ❌          |
| last_time_str                | str                   | ❌          |
| light_stage                  | int                   | ❌          |
| main_display_index           | int                   | ❌          |
| mandatory_pit_done           | bool                  | ❌          |
| mfd_fuel_to_add              | float                 | ❌          |
| mfd_tyre_pressure            | Wheels                | ❌          |
| mfd_tyre_set                 | int                   | ❌          |
| missing_mandatory_pits       | int                   | ❌          |
| normalized_car_position      | float                 | ❌          |
| number_of_laps               | int                   | ❌          |
| packed_id                    | int                   | ❌          |
| penalty                      | ACC_PENALTY_TYPE      | ❌          |
| penalty_time                 | float                 | ❌          |
| player_car_id                | int                   | ❌          |
| position                     | int                   | ❌          |
| rain_intensity               | ACC_RAIN_INTENSITY    | ❌          |
| rain_intensity_in_10min      | ACC_RAIN_INTENSITY    | ❌          |
| rain_intensity_in_30min      | ACC_RAIN_INTENSITY    | ❌          |
| rain_light                   | bool                  | ❌          |
| rain_tyres                   | int                   | ❌          |
| secondary_display_index      | int                   | ❌          |
| session_index                | int                   | ❌          |
| session_time_left            | float                 | ❌          |
| session_type                 | ACC_SESSION_TYPE      | ❌          |
| status                       | ACC_STATUS            | ❌          |
| strategy_tyre_set            | int                   | ❌          |
| tc_cut_level                 | int                   | ❌          |
| tc_level                     | int                   | ❌          |
| track_grip_status            | ACC_TRACK_GRIP_STATUS | ❌          |
| track_status                 | str                   | ❌          |
| tyre_compound                | str                   | ❌          |
| used_fuel                    | float                 | ❌          |
| wind_direction               | float                 | ❌          |
| wind_speed                   | float                 | ❌          |
| wiper_stage                  | int                   | ❌          |

---

# Static

| Feld                  | Typ   | Verwendet  |
| --------------------- | ----- | ---------- |
| ac_version            | str   | ❌          |
| aid_auto_clutch       | bool  | ❌          |
| aid_fuel_rate         | float | ❌          |
| aid_mechanical_damage | float | ❌          |
| aid_stability         | float | ❌          |
| aid_tyre_rate         | float | ❌          |
| car_model             | str   | 🟡 geplant |
| dry_tyres_name        | str   | ❌          |
| is_online             | bool  | ❌          |
| max_fuel              | float | ❌          |
| max_rpm               | int   | ❌          |
| num_cars              | int   | ❌          |
| number_of_session     | int   | ❌          |
| penalty_enabled       | bool  | ❌          |
| pit_window_end        | int   | ❌          |
| pit_window_start      | int   | ❌          |
| player_name           | str   | ❌          |
| player_nick           | str   | ❌          |
| player_surname        | str   | ❌          |
| sector_count          | int   | ❌          |
| sm_version            | str   | ❌          |
| track                 | str   | 🟡 geplant |
| wet_tyres_name        | str   | ❌          |

---

# Legende

| Symbol | Bedeutung                         |
| ------ | --------------------------------- |
| ✅      | Wird aktuell im Projekt verwendet |
| 🟡     | Für Parser/DTO vorgesehen         |
| ❌      | Derzeit nicht verwendet           |
