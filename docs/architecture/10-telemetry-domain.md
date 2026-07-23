# 10 ACC Integration

## Purpose

This document describes how telemetry data from Assetto Corsa Competizione (ACC) is integrated into the Nordschleifen Coach.

The integration layer translates simulator-specific telemetry into the simulator-independent domain model defined in the Telemetry Model.

Its primary responsibility is data translation, not business logic.

---

# Architectural Principles

The ACC integration follows the project's Clean Architecture principles.

- The domain layer never depends on ACC.
- ACC-specific code exists only inside the Infrastructure layer.
- The adapter reads telemetry but performs no driving analysis.
- DTOs mirror the simulator structures.
- Mappers translate simulator data into domain objects.
- Business logic never accesses Shared Memory directly.
- The domain model remains independent of any telemetry provider.

---

# Integration Overview

```text
Assetto Corsa Competizione
            │
            ▼
      Shared Memory
            │
            ▼
     Infrastructure Adapter
            │
            ▼
         ACC DTOs
            │
            ▼
          Mapper
            │
            ▼
     TelemetryFrame
            │
            ▼
        Application
            │
            ▼
      Feature Engine
            │
            ▼
       Skill Engine
            │
            ▼
         AI Coach
```

---

# Data Source

Version 1 of the Nordschleifen Coach uses the ACC Shared Memory interface as its primary telemetry source.

Characteristics:

- Live telemetry
- Read-only interface
- Low latency
- Continuous updates during driving sessions

Additional telemetry providers may be added in future versions.

---

# Shared Memory Structure

ACC exposes telemetry through three logical sections.

## Physics

Contains dynamic vehicle information.

Examples include:

- speed
- engine RPM
- steering
- throttle
- brake
- tyre data
- suspension
- wheel slip
- vehicle dynamics

---

## Graphics

Contains session-related information.

Examples include:

- lap information
- lap validity
- current time
- best lap
- sector
- normalized track position
- race position
- weather
- track grip

---

## Static

Contains information that changes rarely.

Examples include:

- track
- car model
- player
- maximum RPM
- simulator version

---

# Data Flow

Telemetry is processed using the following pipeline.

```text
ACC
        │
        ▼
Shared Memory
        │
        ▼
Read
        │
        ▼
ACC DTOs
        │
        ▼
Mapper
        │
        ▼
TelemetryFrame
        │
        ▼
Application Services
```

Each processing stage has a single responsibility.

---

# DTO Layer

The DTO layer mirrors the Shared Memory structures.

Typical DTOs include:

- AccPhysicsDto
- AccGraphicsDto
- AccStaticDto

DTOs contain raw simulator data only.

They perform no validation, calculations, or business logic.

---

# Mapping Layer

The mapper translates simulator-specific data into domain objects.

Example mappings:

| ACC Field | Domain Property |
|-----------|-----------------|
| gas | DriverInputs.throttle |
| brake | DriverInputs.brake |
| steer_angle | DriverInputs.steering |
| clutch | DriverInputs.clutch |
| gear | DriverInputs.gear |
| speed_kmh | VehicleState.speed |
| rpm | VehicleState.rpm |
| fuel | VehicleState.fuel |
| heading | VehicleDynamics.heading |
| pitch | VehicleDynamics.pitch |
| roll | VehicleDynamics.roll |
| g_force | VehicleDynamics.g_force |
| wheel_slip | WheelState.slip |
| tyre_core_temp | WheelState.tyre_temperature |
| wheel_pressure | WheelState.tyre_pressure |
| normalized_car_position | SessionState.normalized_position |
| completed_lap | SessionState.lap |
| current_time | SessionState.current_time |
| track | EnvironmentState.track |
| road_temp | EnvironmentState.track_temperature |
| air_temp | EnvironmentState.air_temperature |

The mapper is responsible only for translation.

No driving analysis is performed during mapping.

---

# Domain Translation

Simulator terminology is translated into domain terminology.

Example:

```text
ACC
gas

↓

DriverInputs.throttle
```

```text
ACC
speed_kmh

↓

VehicleState.speed
```

The domain model intentionally avoids simulator-specific names whenever a more general domain concept exists.

---

# Error Handling

The integration layer is responsible for handling telemetry acquisition errors.

Typical error scenarios include:

- ACC not running
- Shared Memory unavailable
- incomplete telemetry frames
- invalid timestamps
- corrupted data

Errors should be detected within the Infrastructure layer.

Invalid telemetry must never propagate into the domain model.

---

# Update Strategy

Telemetry is read continuously while a driving session is active.

Each successful read produces a new immutable TelemetryFrame.

Frames are processed in chronological order.

The update frequency may be configurable in future versions.

---

# Extensibility

The telemetry architecture is designed to support additional data providers.

Possible future integrations include:

- MoTeC log files
- Replay telemetry
- CSV imports
- iRacing telemetry
- Le Mans Ultimate telemetry

All telemetry providers must translate their data into the common TelemetryFrame domain model.

No application logic should depend on a specific simulator.

---

# Summary

The ACC integration provides a clean separation between simulator-specific telemetry and the domain model.

It is responsible for reading, translating, and delivering telemetry data while keeping the remainder of the application completely independent of Assetto Corsa Competizione.

This separation enables future telemetry providers to be integrated without modifying the application's business logic.