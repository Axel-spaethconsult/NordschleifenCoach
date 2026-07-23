# 09 Telemetry Model

## Purpose

Telemetry is the primary source of information for the Nordschleifen Coach.

The domain model defines *what* information is required to analyse a driver's performance without depending on any specific simulator, telemetry protocol, or data source.

The model represents the state of the vehicle, the driver's inputs, the session, and the surrounding environment at a specific point in time.

---

# Design Principles

The telemetry model follows the project's Clean Architecture principles.

- The domain is independent of telemetry providers.
- Telemetry objects represent domain concepts, not simulator structures.
- Every object has a single responsibility.
- Objects should remain small, cohesive, and easily testable.
- The model must support real-time and offline telemetry equally.

---

# Overview

The central domain object is the `TelemetryFrame`.

Each frame represents a snapshot of the vehicle at a specific timestamp.

```text
TelemetryFrame
│
├── DriverInputs
├── VehicleState
├── VehicleDynamics
├── WheelState
├── SessionState
└── EnvironmentState
```

The frame itself contains no analysis logic.

Its only responsibility is to represent the current state of the vehicle and session.

---

# TelemetryFrame

The `TelemetryFrame` aggregates all telemetry information for a single instant in time.

Responsibilities:

- represent one telemetry sample
- provide a consistent snapshot
- aggregate all telemetry sub-models
- remain immutable after creation whenever possible

Typical properties:

- timestamp
- driver_inputs
- vehicle_state
- vehicle_dynamics
- wheel_state
- session_state
- environment_state

---

# DriverInputs

The `DriverInputs` object represents commands issued by the driver.

Responsibilities:

- throttle position
- brake position
- steering angle
- clutch position
- selected gear

This object represents driver intent rather than vehicle behaviour.

---

# VehicleState

The `VehicleState` object represents the mechanical state of the vehicle.

Typical information includes:

- vehicle speed
- engine RPM
- current fuel level
- engine status
- ignition status

The object describes the vehicle itself, independent of driver inputs.

---

# VehicleDynamics

The `VehicleDynamics` object describes how the vehicle moves through space.

Typical information includes:

- heading
- pitch
- roll
- velocity
- local velocity
- acceleration
- G-forces

This object forms the basis for analysing vehicle balance and dynamic behaviour.

---

# WheelState

The `WheelState` object contains tyre and brake information.

Typical information includes:

- tyre temperatures
- tyre pressures
- brake temperatures
- brake pressures
- wheel slip
- slip angle
- slip ratio

This information is essential for analysing grip, braking performance, and vehicle stability.

---

# SessionState

The `SessionState` object contains information describing the current driving session.

Typical information includes:

- current lap
- lap validity
- lap time
- sector
- travelled distance
- normalized track position
- race position

The normalized track position is especially important because it allows telemetry samples from different laps to be compared at identical locations on the circuit.

---

# EnvironmentState

The `EnvironmentState` object represents external conditions influencing vehicle behaviour.

Typical information includes:

- air temperature
- track temperature
- track grip
- weather conditions
- wind

Environmental information changes relatively slowly but has a significant impact on vehicle performance.

---

# Relationships

```text
TelemetryFrame
│
├── DriverInputs
├── VehicleState
├── VehicleDynamics
├── WheelState
├── SessionState
└── EnvironmentState
```

Each sub-model owns a single area of responsibility.

No sub-model should duplicate information contained in another.

---

# Design Rationale

The telemetry model intentionally separates driver actions from vehicle behaviour.

For example:

- Brake pedal position belongs to `DriverInputs`.
- Vehicle deceleration belongs to `VehicleDynamics`.

Likewise:

- Steering angle belongs to `DriverInputs`.
- Vehicle yaw behaviour belongs to `VehicleDynamics`.

This separation enables analysis engines to distinguish between what the driver intended and how the vehicle responded.

---

# Future Extensions

The telemetry model is intentionally extensible.

Possible future additions include:

- SuspensionState
- AeroState
- PowertrainState
- ElectronicSystemsState
- DamageState
- AIOpponentState

New telemetry objects should be introduced only when they represent clearly identifiable domain concepts.

---

# Summary

The telemetry model defines a simulator-independent representation of vehicle telemetry.

It serves as the canonical data model used throughout the application and forms the foundation for feature extraction, driving analysis, coaching logic, and AI-generated feedback.