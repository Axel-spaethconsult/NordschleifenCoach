# ADR-0005 – Deterministic Analysis Before AI

**Status:** Accepted

**Date:** 2026-07-22

---

# Context

Nordschleifen Coach analyzes racing telemetry to evaluate driving performance and generate personalized coaching recommendations.

Modern Large Language Models are capable of producing convincing explanations, but they are probabilistic systems and may generate incorrect or unsupported conclusions.

The project requires analysis results that are:

* Reproducible
* Explainable
* Testable
* Independent of a specific AI provider

Therefore, the correctness of the analysis must never depend on AI.

---

# Decision

All telemetry analysis, feature extraction, and skill evaluation shall be performed using deterministic algorithms.

Artificial Intelligence shall only interpret and explain results that have already been produced by deterministic analysis.

AI must never invent measurements, scores, or conclusions that are not supported by computed data.

---

# Analysis Pipeline

The analysis workflow is defined as follows:

```text
Telemetry
    ↓
Validation
    ↓
Feature Extraction
    ↓
Skill Evaluation
    ↓
Training Recommendation
    ↓
AI Explanation
```

Each stage before AI produces structured, deterministic output.

The AI receives only validated analysis results as input.

---

# Responsibilities

## Deterministic Components

Responsible for:

* Telemetry validation
* Lap segmentation
* Feature extraction
* Skill calculation
* Progress tracking
* Training plan generation

Outputs from these components are considered the source of truth.

---

## AI Components

Responsible for:

* Explaining analysis results
* Summarizing strengths and weaknesses
* Answering user questions
* Generating natural language feedback
* Improving readability of technical results

AI does not modify analysis results.

AI does not calculate scores.

AI does not generate telemetry-derived facts.

---

# Consequences

## Advantages

* Fully reproducible analyses
* High confidence in calculated results
* Easier automated testing
* Clear separation between computation and explanation
* AI providers can be replaced without changing the analysis engine

## Trade-offs

* More deterministic algorithms must be implemented.
* AI cannot compensate for missing analytical functionality.
* Initial development effort is higher.

These trade-offs are accepted because reliability and transparency are core project goals.

---

# Alternatives Considered

## AI-driven analysis

Rejected because results would not be consistently reproducible or independently verifiable.

## Hybrid AI scoring

Rejected because deterministic and probabilistic reasoning would become difficult to distinguish.

## AI-only coaching

Rejected because coaching recommendations must always be traceable to measurable telemetry data.

---

# Decision Outcome

The Nordschleifen Coach follows a **deterministic-first architecture**.

Deterministic algorithms produce all measurable results.

Artificial Intelligence serves exclusively as an explanation and interaction layer.

This principle applies throughout the entire project and is considered a fundamental architectural rule.
