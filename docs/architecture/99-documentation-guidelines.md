# 99 – Documentation Guidelines

## Purpose

This document defines the standards for all architecture documentation within the Nordschleifen Coach project.

The goal is to keep documentation consistent, understandable, and maintainable throughout the project's lifetime.

---

# General Principles

* Documentation is part of the source code.
* Every architectural decision should be documented.
* Documentation is maintained together with the implementation.
* Git provides the history; documents represent the current state.

---

# Language

The project language is English.

This includes:

* Documentation
* Source code
* Comments
* Commit messages
* Issue titles
* Pull requests

Exceptions:

* Discussions
* Meeting notes
* Internal communication

---

# File Naming

Architecture documents use numbered filenames.

Example:

```text
00-vision.md
01-requirements.md
02-system-context.md
...
```

---

# Document Header

Every architecture document starts with:

```markdown
# Title

**Status:** Draft
**Version:** 0.1
**Last Updated:** YYYY-MM-DD

---
```

---

# Status Values

Possible document states:

* Draft
* Review
* Approved
* Deprecated

---

# Diagrams

Architecture diagrams should use Mermaid whenever possible.

Benefits:

* Text-based
* Version controlled
* GitHub compatible
* Easy to maintain

---

# Markdown

Use standard Markdown.

Avoid HTML unless absolutely necessary.

---

# Code Examples

Code examples should be minimal and illustrate architectural concepts only.

Implementation details belong in the source code.

---

# Architecture Decisions

Major decisions should be documented as Architecture Decision Records (ADR).

Location:

```text
docs/decisions/
```

---

# Versioning

Architecture documents describe the current architecture only.

Historical changes are tracked by Git.

---

# Commit Convention

Each commit should represent one logical change.

Examples:

* Add project vision
* Define system requirements
* Design feature engine

Avoid combining unrelated changes in a single commit.

---

# Review

Architecture documents should be reviewed before major implementation work begins.

---

# Guiding Principle

Good documentation reduces future complexity.
