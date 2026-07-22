# ADR-0001 – Use Clean Architecture

**Status:** Accepted

**Date:** 2026-07-22

---

# Context

Nordschleifen Coach is intended to become a long-term open-source project.

The system will process telemetry data, perform deterministic analysis, generate AI-assisted coaching, and provide visualizations through a dashboard.

Future versions are expected to support:

* Multiple racing simulators
* Additional tracks
* Additional vehicle classes
* Different AI providers
* Multiple storage backends
* Alternative user interfaces

Without a clear architectural separation, these requirements would lead to tightly coupled components that are difficult to test, maintain, and extend.

---

# Decision

The project adopts **Clean Architecture** as its primary architectural style.

The system will be organized into independent layers.

Dependencies always point inward.

Business rules must never depend on infrastructure, frameworks, databases, or user interfaces.

---

# Layer Overview

## Domain

Contains the business model.

Examples:

* Driver
* Session
* Lap
* Track
* Section
* Segment
* Feature
* Skill
* Training Goal

The domain layer contains no infrastructure code.

---

## Application

Contains use cases that orchestrate business logic.

Examples:

* Import Telemetry
* Analyze Session
* Compare Laps
* Generate Training Plan

Application coordinates work but does not perform infrastructure tasks.

---

## Infrastructure

Implements technical details.

Examples:

* ACC telemetry collector
* SQLite
* File system
* AI provider
* Logging

Infrastructure depends on the application and domain layers, never the other way around.

---

## Interfaces

Provides interaction with external users or systems.

Examples:

* Dashboard
* Command-line interface
* REST API (future)

---

## Shared

Contains reusable utilities that are independent of business logic.

Examples:

* Configuration
* Exceptions
* Constants
* Common helper functions

---

# Dependency Rule

The dependency direction is always:

```text
Interfaces
      ↓
Infrastructure
      ↓
Application
      ↓
Domain
```

The Domain layer depends on nothing.

---

# Consequences

## Advantages

* High testability
* Clear separation of responsibilities
* Replaceable infrastructure
* Easier maintenance
* Support for future simulators
* AI provider can be replaced without affecting business logic

## Trade-offs

* More initial design effort
* Additional project structure
* Slightly higher learning curve

These trade-offs are acceptable because long-term maintainability is a primary project goal.

---

# Alternatives Considered

## Layered Architecture

Rejected because business logic tends to become coupled to infrastructure.

## MVC

Rejected because the project is analysis-centric rather than UI-centric.

## Monolithic Script Structure

Rejected because it does not scale to the expected project size.

---

# Decision Outcome

Clean Architecture is adopted as the foundation of Nordschleifen Coach.

All future implementation should respect the dependency rule and preserve the independence of the Domain layer.
