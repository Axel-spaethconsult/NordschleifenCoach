# 01 – Requirements

# Functional Requirements

## FR-001 Session Detection

The system shall automatically detect the start and end of driving sessions.

## FR-002 Telemetry Collection

The system shall collect all available telemetry from Assetto Corsa Competizione.

## FR-003 Data Storage

The system shall store raw telemetry without modification.

## FR-004 Track Recognition

The system shall identify the current track and layout.

## FR-005 Vehicle Recognition

The system shall identify the driven vehicle.

## FR-006 Track Segmentation

The system shall divide the track into predefined sections and analysis segments.

## FR-007 Feature Extraction

The system shall calculate measurable driving features from raw telemetry.

Examples include:

* Speed
* Braking
* Throttle
* Steering
* Racing Line
* Vehicle Dynamics
* Consistency

## FR-008 Skill Evaluation

The system shall evaluate driver skills based on extracted features.

Skills include:

* Braking
* Trail Braking
* Corner Entry
* Rotation
* Mid Corner
* Corner Exit
* Throttle Control
* Steering Smoothness
* Racing Line
* Consistency

## FR-009 Progress Tracking

The system shall track driver improvement over time.

## FR-010 Session Comparison

The system shall compare sessions and laps.

## FR-011 Training Recommendations

The system shall generate personalized training recommendations.

## FR-012 AI Coach

The AI Coach shall explain analysis results using natural language.

The AI Coach shall not replace deterministic analysis.

---

# Non-Functional Requirements

## Performance

* Session processing should complete within a reasonable time after the session ends.
* Analysis should scale to thousands of laps.

## Reliability

* Raw telemetry must never be modified.
* Derived data shall be reproducible.

## Maintainability

* Modular architecture
* Clear interfaces
* Independent components
* Version-controlled documentation

## Extensibility

The architecture shall support:

* additional cars
* additional tracks
* additional simulators
* additional analysis modules

## Explainability

Every recommendation should be traceable to measurable telemetry.

---

# Constraints

## Initial Scope

Simulator:

* Assetto Corsa Competizione

Vehicle:

* BMW M4 GT4

Track:

* Nürburgring 24h

Future versions may expand beyond this initial scope.

---

# Success Metrics

The system is considered successful if it can:

* identify measurable weaknesses
* explain those weaknesses
* recommend targeted practice
* demonstrate measurable driver improvement over time

---

# Out of Scope

The following are intentionally excluded from the initial versions:

* Automatic driving
* Race strategy optimization
* Vehicle setup optimization
* Multiplayer race management
* Real-time driving assistance

These topics may be reconsidered in future releases.
