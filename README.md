# Nordschleifen Coach

An open-source AI-assisted racing coach for **Assetto Corsa Competizione**, focused on the **BMW M4 GT4** and the **Nürburgring 24h** layout.

---

## Vision

Nordschleifen Coach helps drivers improve through objective telemetry analysis rather than lap-time comparisons alone.

The project collects telemetry from Assetto Corsa Competizione, extracts meaningful driving features, evaluates driver skills, tracks long-term progress, and generates personalized training recommendations.

The long-term goal is to build an intelligent coaching system that explains *why* a lap was fast or slow and provides actionable guidance tailored to the driver's individual weaknesses.

---

## Objectives

* Automatic session detection
* Telemetry collection and storage
* Track segmentation
* Feature extraction
* Driving skill evaluation
* Progress tracking
* Personalized training plans
* AI-assisted coaching
* Modern dashboard for analysis and visualization

---

## Architecture

The project follows an **architecture-first** approach.

Deterministic telemetry analysis forms the foundation of the system. AI is used to explain results and generate coaching recommendations rather than replacing the underlying analysis.

High-level processing pipeline:

```text
Assetto Corsa Competizione
        ↓
Telemetry Collector
        ↓
Raw Data Storage
        ↓
Feature Extraction
        ↓
Analysis Engine
        ↓
Progress Engine
        ↓
Training Planner
        ↓
AI Coach
        ↓
Dashboard
```

---

## Project Structure

```text
docs/
    architecture/
    decisions/
    diagrams/

src/
tests/
data/
tools/
scripts/
```

---

## Development Principles

* Architecture before implementation
* Clean and maintainable code
* Reproducible analyses
* Version-controlled documentation
* Open-source development
* Incremental improvements through small, well-defined commits

---

## Roadmap

### Phase 1 – Foundation

* Development environment
* Architecture documentation
* Repository setup

### Phase 2 – Telemetry

* Session detection
* Telemetry collection
* Data storage

### Phase 3 – Feature Engine

* Driving features
* Track segmentation
* Skill evaluation

### Phase 4 – Coaching

* Progress analysis
* Training planner
* AI-assisted feedback

### Phase 5 – Dashboard

* Interactive visualizations
* Session comparison
* Long-term performance tracking

---

## License

This project is licensed under the Apache License 2.0.

---

## Status

🚧 Early architecture and planning phase.
