# 07 – Development Principles

**Status:** Draft

**Version:** 1.0

**Last Updated:** 2026-07-22

---

# Purpose

This document defines the development principles for the Nordschleifen Coach.

Its purpose is to ensure consistent implementation, maintainability, and code quality throughout the lifetime of the project.

These principles apply to all source code, tests, and documentation.

---

# General Principles

The project follows these core principles:

* Architecture before implementation
* Deterministic analysis before AI
* Documentation before major features
* Simplicity over unnecessary complexity
* Readability over cleverness
* Small, incremental improvements

---

# Clean Code

Code should be:

* Easy to read
* Easy to understand
* Easy to test
* Easy to modify

Developers should optimize for clarity rather than minimizing the number of lines.

---

# Single Responsibility Principle

Every:

* class,
* function,
* module,

should have one clearly defined responsibility.

Large functions should be decomposed into smaller units.

---

# Dependency Management

Dependencies must follow the rules defined in:

* ADR-0001
* ADR-0002
* ADR-0003

Business logic must never depend directly on:

* databases,
* AI providers,
* file systems,
* user interfaces.

---

# Naming Conventions

Names should be descriptive.

Examples:

Classes

* Session
* Lap
* Feature
* SkillEvaluation

Services

* FeatureExtractionService
* SkillEvaluationService
* TrainingPlanningService

Use Cases

* ImportTelemetryUseCase
* AnalyzeSessionUseCase

Repositories

* SessionRepository
* FeatureRepository

Avoid abbreviations unless they are well established.

---

# Python Style

The project follows:

* PEP 8
* Ruff formatting and linting
* Type hints for public interfaces
* Meaningful docstrings where appropriate

Magic numbers should be replaced with named constants.

---

# Error Handling

Errors should:

* be detected early,
* provide meaningful messages,
* never fail silently.

Recoverable and unrecoverable errors should be clearly distinguished.

---

# Testing

Testing is a first-class development activity.

The project includes:

* Unit tests
* Integration tests
* Regression tests

Business logic should be testable without external dependencies.

Infrastructure components may use test doubles or mocks where appropriate.

---

# Git Workflow

Each commit should represent one logical change.

Recommended workflow:

1. Implement
2. Test
3. Update documentation if required
4. Review changes
5. Commit

Commit messages should be written in English using the imperative mood.

Examples:

* Add telemetry parser
* Implement feature extraction
* Refactor session detection

---

# Documentation

Architecture documentation is maintained alongside the implementation.

Significant architectural decisions require an ADR.

Documentation should be updated when implementation changes affect system behavior.

---

# Performance

Optimize only after correctness.

Priority order:

1. Correctness
2. Readability
3. Maintainability
4. Performance

Performance optimizations should be supported by measurements whenever possible.

---

# AI Usage

Artificial Intelligence is used for:

* explaining results,
* generating natural language feedback,
* assisting user interaction.

Artificial Intelligence is not used for:

* computing features,
* evaluating skills,
* replacing deterministic algorithms.

---

# Continuous Improvement

The architecture is expected to evolve.

Improvements should:

* preserve existing design principles,
* reduce complexity,
* improve maintainability,
* avoid unnecessary breaking changes.

---

# Summary

The Nordschleifen Coach prioritizes clarity, modularity, and long-term maintainability over short-term implementation speed.

Every contribution should reinforce these principles and support the project's architectural goals.
