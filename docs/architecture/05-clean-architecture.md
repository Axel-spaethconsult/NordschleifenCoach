# 05 – Clean Architecture

**Status:** Draft

**Version:** 1.0

**Last Updated:** 2026-07-22

---

# Purpose

This document defines the architectural structure of the Nordschleifen Coach.

It specifies the architectural layers, their responsibilities, dependency rules, and how data flows through the system.

The architecture follows the decisions documented in:

* ADR-0001 – Use Clean Architecture
* ADR-0002 – Use Ports and Adapters
* ADR-0003 – Use Repository Pattern
* ADR-0005 – Deterministic Analysis Before AI

---

# Architectural Principles

The system follows these principles:

* Business logic is independent of infrastructure.
* Dependencies always point inward.
* External technologies are replaceable.
* AI explains analysis but never performs it.
* Domain logic remains deterministic and testable.

---

# Layer Overview

## Domain

The domain layer contains the core business concepts and rules.

Responsibilities:

* Domain entities
* Value objects
* Domain services
* Business rules

The domain layer has no dependencies on other layers.

Examples:

* Driver
* Session
* Lap
* Track
* Feature
* Skill
* TrainingGoal

---

## Application

The application layer orchestrates business workflows.

Responsibilities:

* Use cases
* Transaction boundaries
* Coordination of domain services
* Repository interfaces
* External service interfaces

Examples:

* ImportTelemetryUseCase
* AnalyzeSessionUseCase
* CompareSessionsUseCase
* GenerateTrainingPlanUseCase

---

## Infrastructure

The infrastructure layer provides technical implementations.

Responsibilities:

* Telemetry import
* Database access
* AI provider integration
* File system access
* Logging

Examples:

* SQLite repositories
* ACC telemetry collector
* OpenAI adapter
* Local file storage

---

## Interfaces

The interface layer exposes the application.

Responsibilities:

* CLI
* Dashboard
* REST API
* Future desktop application

This layer contains no business logic.

---

# Dependency Rule

Dependencies always point toward the domain.

```text
Interfaces
      │
      ▼
Infrastructure
      │
      ▼
Application
      │
      ▼
Domain
```

The Domain layer must never reference any other layer.

---

# High-Level Data Flow

The primary workflow is:

```text
ACC
 │
 ▼
Telemetry Collector
 │
 ▼
Raw Telemetry Storage
 │
 ▼
Feature Extraction
 │
 ▼
Feature Repository
 │
 ▼
Skill Evaluation
 │
 ▼
Progress Evaluation
 │
 ▼
Training Planner
 │
 ▼
AI Coach
 │
 ▼
Dashboard / CLI
```

---

# Layer Responsibilities

| Component             | Layer          |
| --------------------- | -------------- |
| Driver                | Domain         |
| Session               | Domain         |
| Lap                   | Domain         |
| Track                 | Domain         |
| Feature               | Domain         |
| Skill                 | Domain         |
| Progress              | Domain         |
| TrainingGoal          | Domain         |
| Feature Extraction    | Domain Service |
| Skill Evaluation      | Domain Service |
| Progress Evaluation   | Domain Service |
| Training Planner      | Domain Service |
| Repository Interfaces | Application    |
| AI Interface          | Application    |
| SQLite                | Infrastructure |
| ACC Collector         | Infrastructure |
| OpenAI Adapter        | Infrastructure |
| Dashboard             | Interfaces     |
| CLI                   | Interfaces     |

---

# Dependency Constraints

Allowed:

* Interfaces → Application
* Infrastructure → Application
* Application → Domain

Forbidden:

* Domain → Application
* Domain → Infrastructure
* Domain → Interfaces
* Application → Infrastructure (direct implementation dependency)

---

# Architectural Goal

The architecture shall allow:

* Additional racing simulators
* Alternative AI providers
* Different storage technologies
* Additional analysis modules
* New user interfaces

without requiring changes to the core business logic.

---

# Summary

The Nordschleifen Coach is built around a deterministic domain model.

Infrastructure is considered replaceable.

Artificial Intelligence is treated as an optional explanation layer rather than a source of analytical truth.
