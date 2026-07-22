# 08 – Domain Design

**Status:** Draft

**Version:** 1.0

**Last Updated:** 2026-07-22

---

# Purpose

This document defines the core domain objects of the Nordschleifen Coach.

It specifies their responsibilities, relationships, and invariants. The document serves as the blueprint for the implementation of the domain layer.

---

# Domain Overview

```text
Driver
   │
   ▼
Session
   │
   ▼
Lap
   │
   ▼
Feature
   │
   ▼
Skill
   │
   ▼
Training Goal
```

---

# Driver

## Purpose

Represents a user of the system.

## Responsibilities

* Own sessions
* Track progress
* Receive coaching

## Relationships

Driver

* owns many Sessions

---

# Session

## Purpose

Represents one complete driving session.

## Responsibilities

* Store session metadata
* Own laps
* Reference track
* Reference vehicle

## Relationships

Session

* belongs to one Driver
* contains many Laps
* references one Track

---

# Lap

## Purpose

Represents one completed lap.

## Responsibilities

* Store lap time
* Store telemetry reference
* Own extracted features

## Relationships

Lap

* belongs to one Session
* contains many Features

---

# Track

## Purpose

Represents a racing circuit.

## Responsibilities

* Store metadata
* Define sectors
* Define segments

Track

* referenced by many Sessions

---

# Feature

## Purpose

Represents a measurable driving characteristic.

Examples

* Brake Point
* Minimum Speed
* Steering Smoothness
* Throttle Trace

Features are deterministic.

---

# Skill

## Purpose

Represents an evaluated driving capability.

Examples

* Braking
* Corner Entry
* Apex
* Exit
* Consistency

Skills are calculated from Features.

---

# Progress

## Purpose

Represents long-term driver development.

Progress aggregates historical skill evaluations.

---

# Training Goal

## Purpose

Represents one measurable learning objective.

Examples

* Brake later
* Improve throttle modulation
* Reduce steering corrections

Training goals originate from deterministic analysis.

---

# Domain Invariants

The following rules always apply:

* A Session belongs to exactly one Driver.
* A Lap belongs to exactly one Session.
* A Session references exactly one Track.
* Features are calculated from telemetry.
* Skills are calculated from features.
* Progress is calculated from skills.
* AI never modifies domain objects.

---

# Design Principles

Domain objects should:

* model business concepts,
* avoid infrastructure dependencies,
* encapsulate business rules,
* expose meaningful behavior,
* remain immutable where appropriate.

---

# Summary

The domain layer models the language and concepts of racing analysis.

It forms the foundation of the entire Nordschleifen Coach architecture.

All higher layers depend on this model, while the domain itself remains independent of external technologies.
