# 06 – Module Structure

**Status:** Draft

**Version:** 1.0

**Last Updated:** 2026-07-22

---

# Purpose

This document defines the functional modules of the Nordschleifen Coach.

Each module has a single, well-defined responsibility and communicates with other modules through clearly defined interfaces.

The module structure is independent of the underlying implementation and complements the Clean Architecture described in *05-clean-architecture.md*.

---

# Design Principles

The module structure follows these principles:

* Single Responsibility Principle
* High cohesion
* Low coupling
* Clear module boundaries
* Deterministic processing before AI
* Replaceable infrastructure

---

# Module Overview

```text
Telemetry
     │
     ▼
Session Management
     │
     ▼
Feature Engine
     │
     ▼
Skill Engine
     │
     ▼
Progress Engine
     │
     ▼
Training Engine
     │
     ▼
AI Coach
     │
     ▼
Dashboard / CLI
```

---

# Module Descriptions

## Telemetry Module

### Purpose

Collect and validate telemetry from external simulators.

### Responsibilities

* Read telemetry
* Validate incoming data
* Normalize formats
* Store raw telemetry

### Inputs

* ACC telemetry

### Outputs

* Valid telemetry sessions

---

## Session Management Module

### Purpose

Organize telemetry into meaningful racing sessions.

### Responsibilities

* Detect sessions
* Detect laps
* Detect stints
* Associate track and vehicle information

### Inputs

* Valid telemetry

### Outputs

* Session objects
* Lap objects
* Stint objects

---

## Feature Engine

### Purpose

Extract measurable driving characteristics.

### Responsibilities

* Calculate braking features
* Calculate throttle features
* Calculate steering features
* Calculate racing line metrics
* Calculate consistency metrics

### Inputs

* Sessions
* Laps

### Outputs

* Features

---

## Skill Engine

### Purpose

Evaluate driver performance using extracted features.

### Responsibilities

* Calculate skill scores
* Detect strengths
* Detect weaknesses
* Compare sessions

### Inputs

* Features

### Outputs

* Skills
* Skill evaluations

---

## Progress Engine

### Purpose

Track driver development over time.

### Responsibilities

* Aggregate historical data
* Calculate trends
* Detect improvements
* Detect regressions

### Inputs

* Skills
* Sessions

### Outputs

* Progress reports

---

## Training Engine

### Purpose

Generate personalized training recommendations.

### Responsibilities

* Prioritize weaknesses
* Define training goals
* Recommend exercises
* Build structured training plans

### Inputs

* Skills
* Progress

### Outputs

* Training plans

---

## AI Coach

### Purpose

Translate analytical results into understandable coaching.

### Responsibilities

* Explain results
* Summarize analyses
* Answer user questions
* Generate natural language feedback

### Constraints

The AI Coach does **not**:

* calculate features,
* evaluate skills,
* modify scores,
* invent facts.

---

## Dashboard / CLI

### Purpose

Provide user interaction.

### Responsibilities

* Display analyses
* Display progress
* Display training plans
* Accept user input

The interface layer contains no business logic.

---

# Module Dependencies

```text
Telemetry
        │
        ▼
Session Management
        │
        ▼
Feature Engine
        │
        ▼
Skill Engine
        │
        ▼
Progress Engine
        │
        ▼
Training Engine
        │
        ▼
AI Coach
        │
        ▼
Dashboard
```

No module may bypass another module without explicit architectural justification.

---

# Future Extensions

The architecture is designed to support additional modules, including:

* Multi-simulator support
* Setup analysis
* Weather analysis
* Team management
* Multi-driver comparison
* Predictive performance analysis

New modules should integrate through existing interfaces without modifying established module responsibilities.

---

# Summary

The Nordschleifen Coach is organized into independent functional modules.

Each module performs a specific task and provides clearly defined outputs for the next stage of the analysis pipeline.

This modular design improves maintainability, testability, and future extensibility while preserving deterministic analysis as the foundation of the system.
