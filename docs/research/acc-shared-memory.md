# ACC Shared Memory Research

## Status

- Simulator: Assetto Corsa Competizione
- Telemetry Source: ACC Shared Memory
- Python Library: pyaccsharedmemory
- Status: Successfully connected

---

# Sections

ACC Shared Memory provides three logical sections:

- Physics
- Graphics
- Static

---

# Physics

## Core Vehicle State

| Field | Type | Unit | Required | Notes |
|------|------|------|----------|------|
| speed_kmh | float | km/h | ✅ | Vehicle speed |
| rpm | int | rpm | ✅ | Engine speed |
| gear | int | - | ✅ | Current gear |
| gas | float | 0–1 | ✅ | Throttle position |
| brake | float | 0–1 | ✅ | Brake pedal |
| steer_angle | float | rad | ✅ | Steering angle |

## Vehicle Motion

| Field | Required |
|------|----------|
| heading | ✅ |
| pitch | ✅ |
| roll | ✅ |
| velocity | ✅ |
| local_velocity | ✅ |
| g_force | ✅ |

## Wheel Data

| Field | Required |
|------|----------|
| tyre_core_temp | ✅ |
| wheel_pressure | ✅ |
| slip_ratio | ✅ |
| slip_angle | ✅ |
| wheel_slip | ✅ |
| brake_temp | ✅ |

---

# Graphics

## Session

| Field | Required |
|------|----------|
| completed_lap | ✅ |
| current_time | ✅ |
| best_time | ✅ |
| is_valid_lap | ✅ |
| distance_traveled | ✅ |
| normalized_car_position | ⭐⭐⭐⭐⭐ |

---

# Static

## Track

| Field | Required |
|------|----------|
| track | ✅ |
| car_model | ✅ |
| max_rpm | ✅ |

---

# Observations

The field `normalized_car_position` is one of the most valuable telemetry values for the Nordschleifen Coach.

It allows comparing telemetry at identical positions on the track without relying on GPS coordinates.

Potential applications:

- Brake point detection
- Turn-in detection
- Apex detection
- Corner exit analysis
- Lap comparison