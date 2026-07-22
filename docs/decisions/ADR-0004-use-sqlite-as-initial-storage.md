# ADR-0004 – Use SQLite as Initial Storage Backend

**Status:** Accepted

**Date:** 2026-07-22

---

# Context

Nordschleifen Coach requires persistent storage for telemetry-related data, extracted features, analysis results, and user progress.

During the initial development phase, the project will be used primarily by a single developer on a local machine.

The storage solution should:

* require no server installation,
* be easy to set up,
* support ACID transactions,
* integrate well with Python,
* allow future migration to a different database system.

---

# Decision

SQLite is selected as the initial storage backend.

Database access will occur exclusively through repository interfaces defined by the application layer.

The rest of the system shall remain independent of SQLite.

---

# Rationale

SQLite provides several advantages for the first development stages:

* Zero configuration
* Single database file
* Reliable and mature implementation
* Excellent Python support
* Fast enough for local telemetry analysis
* Easy backup and portability

SQLite is sufficient for expected data volumes during early development.

---

# Constraints

The following limitations are accepted:

* Single-writer architecture
* Limited scalability for concurrent users
* Not intended for distributed deployments

These limitations are acceptable because they do not conflict with the current project scope.

---

# Migration Strategy

The storage implementation must remain replaceable.

Possible future backends include:

* PostgreSQL
* DuckDB
* Cloud-hosted SQL databases

Migration should require only replacing repository implementations in the infrastructure layer.

No business logic should require modification.

---

# Alternatives Considered

## PostgreSQL

Rejected for the initial phase because it requires additional infrastructure and administration.

## DuckDB

Rejected because transactional application data is a higher priority than analytical performance during early development.

DuckDB may be introduced later for advanced telemetry analytics.

## JSON Files

Rejected because they do not provide transactional consistency or efficient querying.

---

# Consequences

## Advantages

* Simple development setup
* No external dependencies
* Reliable persistence
* Easy distribution
* Straightforward migration path

## Trade-offs

* Limited concurrency
* Less suitable for multi-user deployments
* Database file management becomes necessary

These trade-offs are acceptable for the initial project phase.

---

# Decision Outcome

SQLite is adopted as the initial persistence technology.

The application remains storage-independent through repository interfaces.

SQLite is considered an implementation detail of the infrastructure layer.
