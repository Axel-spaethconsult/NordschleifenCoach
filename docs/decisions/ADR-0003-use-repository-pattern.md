# ADR-0003 – Use Repository Pattern

**Status:** Accepted

**Date:** 2026-07-22

---

# Context

Nordschleifen Coach manages several kinds of persistent data:

* Raw telemetry
* Sessions
* Laps
* Features
* Skill evaluations
* Progress history
* Training plans

The application requires a consistent way to read and write this data without depending on a specific storage technology.

Future versions may replace or extend the initial storage solution.

---

# Decision

The project adopts the **Repository Pattern** for all persistent domain data.

Repositories provide a collection-like interface for accessing and storing domain objects.

The application layer depends only on repository interfaces.

Concrete implementations are provided by the infrastructure layer.

---

# Repository Responsibilities

Repositories are responsible for:

* Loading domain objects
* Persisting domain objects
* Querying stored data
* Hiding storage-specific implementation details

Repositories are **not** responsible for:

* Business rules
* Feature calculation
* Skill evaluation
* Training logic
* AI interaction

---

# Initial Repository Interfaces

Examples include:

* SessionRepository
* LapRepository
* FeatureRepository
* ProgressRepository
* TrainingPlanRepository

Additional repositories may be introduced when required.

---

# Dependency Rule

Repositories are defined as interfaces in the application layer.

Infrastructure provides implementations.

```text
Application
      │
      ▼
Repository Interface
      ▲
      │
SQLite Repository
PostgreSQL Repository
Memory Repository
```

The application remains independent of the storage implementation.

---

# Consequences

## Advantages

* Storage technology can be replaced without affecting business logic.
* Easier unit testing using in-memory repositories.
* Centralized data access.
* Improved maintainability.
* Consistent persistence model across the project.

## Trade-offs

* Additional abstraction layer.
* Slightly more implementation effort.
* More interfaces to maintain.

These trade-offs are acceptable because persistence flexibility is an important long-term requirement.

---

# Alternatives Considered

## Direct SQL access

Rejected because SQL queries would spread throughout the application.

## Active Record

Rejected because it couples domain objects to persistence.

## Global database service

Rejected because it mixes persistence with business logic.

---

# Decision Outcome

All persistent data access shall be performed through repository interfaces.

The application layer remains independent of database technology.

Concrete repository implementations belong exclusively to the infrastructure layer.

