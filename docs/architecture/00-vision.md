# 00 – Project Vision

## Purpose

Nordschleifen Coach is an open-source AI-assisted racing coach for Assetto Corsa Competizione.

Its primary goal is to help drivers improve their driving through objective telemetry analysis, long-term skill tracking, and personalized coaching rather than focusing solely on lap times.

The initial development target is the BMW M4 GT4 on the Nürburgring 24h layout. The architecture, however, is designed to support additional cars and tracks in the future.

---

# Problem Statement

Many existing telemetry tools visualize data but leave the interpretation to the driver.

Nordschleifen Coach aims to bridge this gap by transforming telemetry into understandable coaching feedback.

Instead of asking:

> "What does this telemetry graph mean?"

the driver should be able to ask:

> "Why am I losing time here, and what should I practice next?"

---

# Vision

Nordschleifen Coach combines deterministic telemetry analysis with AI-generated explanations.

The system should:

* automatically detect driving sessions
* collect telemetry
* segment the track into meaningful analysis regions
* extract measurable driving features
* evaluate driving skills
* track long-term improvement
* identify weaknesses
* generate personalized training recommendations

AI is not responsible for calculating the results.

Instead, AI explains and communicates the results produced by deterministic analysis.

---

# Core Principles

## Architecture First

System architecture is designed before implementation.

## Explainable Analysis

Every coaching recommendation should be traceable to measurable telemetry.

## Data Driven

Recommendations are based on objective driving data instead of assumptions.

## Incremental Development

The project grows through small, well-defined iterations.

## Open Source

The project welcomes community contributions while maintaining high quality standards.

---

# Project Scope

## Included

* Assetto Corsa Competizione telemetry
* Nürburgring 24h support
* Telemetry collection
* Feature extraction
* Track segmentation
* Skill evaluation
* Progress tracking
* AI-assisted coaching
* Dashboard and visualization

## Not Included

* Automatic driving
* Cheat systems
* Real-time vehicle control
* Unrealistic "perfect lap" generators
* Esports race strategy
* Vehicle setup optimization (initial versions)

---

# Long-Term Goal

The long-term objective is to create an intelligent coaching platform that helps drivers continuously improve through measurable progress.

The software should answer three questions after every session:

1. What happened?
2. Why did it happen?
3. What should I practice next?

---

# Success Criteria

The project is successful if a driver can improve through the coaching recommendations without requiring expert telemetry knowledge.

Improvement should be measurable, explainable, and repeatable.

---

# Guiding Principle

Measure first.

Understand second.

Coach third.
