# FailurePattern

FailurePattern is a small Python OOP project that identifies **recurring patterns across failures** instead of treating every failure as an isolated incident.

In real systems, the same type of failure may happen multiple times:

```text
Failure 1 → API → Timeout → Production
Failure 2 → API → Timeout → Production
Failure 3 → API → Timeout → Production
                    ↓
             RECURRING PATTERN
```

The project records failures and analyzes them across different dimensions such as:

* Component
* Category
* Cause
* Environment
* Severity
* Exact combinations of failure characteristics

The goal is to help identify repeated problems that may require a deeper investigation or permanent fix.

---

## Project Structure

```text
FailurePattern/
│
├── failure_pattern.py
├── failure_pattern_studio.py
├── README.md
└── .gitignore
```

---

## What Problem Does It Solve?

When failures are recorded individually, teams may notice each incident but miss the fact that several incidents are connected.

For example:

```text
Failure A
Component: Payment API
Cause: Timeout
Environment: Production

Failure B
Component: Payment API
Cause: Timeout
Environment: Production

Failure C
Component: Payment API
Cause: Timeout
Environment: Production
```

Looking at these as three separate incidents hides the bigger picture.

FailurePattern groups the information and can identify:

```text
Payment API
     ↓
Timeout
     ↓
Production
     ↓
Repeated 3 times
     ↓
Strong Recurring Pattern
```

This makes repeated failures easier to investigate.

---

## Key Features

### 1. Record Failures

Each failure can contain:

* Failure ID
* Title
* Component
* Category
* Cause
* Environment
* Severity

Example:

```text
Failure ID: F001
Title: Payment request timeout
Component: Payment API
Category: Timeout
Cause: Slow database query
Environment: Production
Severity: High
```

---

### 2. Analyze Components

The system can determine whether the same component appears repeatedly in failures.

Example:

```text
Payment API → 5 occurrences
Authentication Service → 2 occurrences
Notification Service → 1 occurrence
```

---

### 3. Analyze Failure Categories

Failures can be grouped by category.

Examples:

```text
Timeout       → 4
Authentication → 3
Database      → 2
Validation    → 1
```

---

### 4. Analyze Causes

The system can identify frequently repeated causes.

Example:

```text
Slow database query → 4 occurrences
Invalid token      → 2 occurrences
Configuration error → 1 occurrence
```

This can help teams focus investigation on causes that repeatedly appear.

---

### 5. Analyze Environments

Failures can also be grouped by environment.

Example:

```text
Production → 7
Staging    → 2
Development → 1
```

This can reveal whether a recurring problem is concentrated in a particular environment.

---

### 6. Analyze Severity

The system tracks failure severity:

```text
Low
Medium
High
Critical
```

This helps distinguish frequent minor failures from repeated high-impact failures.

---

### 7. Find Exact Repeated Patterns

The project can identify failures that share the same:

```text
Component
+
Category
+
Cause
+
Environment
```

For example:

```text
Payment API | Timeout | Database delay | Production
```

If this combination appears repeatedly, it becomes a strong signal of a recurring problem.

---

## Pattern Strength

Repeated patterns are classified based on how often they occur.

```text
1 occurrence  → Unique
2 occurrences → Emerging Pattern
3 occurrences → Recurring Pattern
4+ occurrences → Strong Pattern
```

This gives the raw counts more meaning.

---

## Overall Pattern Status

The system can classify the overall failure history as:

* No Failures Recorded
* Partial Pattern
* No Clear Pattern
* Emerging Pattern
* Recurring Pattern
* Strong Recurring Pattern

This provides a quick high-level view of the failure situation.

---

## High-Impact Failures

Failures marked as:

```text
High
Critical
```

can be retrieved separately.

This makes it easier to prioritize failures that could have a significant operational impact.

---

## Matching Failures

Specific failures can be searched using filters such as:

```text
Component
Category
Cause
Environment
Severity
```

Multiple filters can be combined.

For example:

```text
Component = Payment API
Cause = Timeout
Environment = Production
```

The system then returns failures matching those conditions.

---

## OOP Concepts Used

The project is intentionally built using Python object-oriented programming.

### Class

The main logic is contained inside:

```python
class FailurePattern:
```

### Encapsulation

Failure records and analysis logic are maintained inside the class.

### Methods

Different operations are represented through methods such as:

```python
record_failure()
get_failure()
list_failures()
get_component_patterns()
get_category_patterns()
get_cause_patterns()
find_matching_failures()
find_exact_patterns()
analyze()
generate_recommendation()
```

### Data Structures

The project primarily uses:

* Dictionaries
* Lists
* Sets

to store and analyze failure information.

---

## File Responsibilities

### `failure_pattern.py`

Contains the core OOP logic.

It handles:

* Failure recording
* Failure retrieval
* Pattern grouping
* Exact pattern detection
* Matching
* Severity analysis
* Pattern strength
* Overall analysis
* Recommendations

### `failure_pattern_studio.py`

Provides the interactive command-line interface.

It allows users to operate the system without modifying the core class.

---

## How to Run

Make sure Python is installed.

Run:

```bash
python failure_pattern_studio.py
```

---

## Example Workflow

Start the Studio:

```text
============================================================
             FAILURE PATTERN STUDIO
============================================================
1. Record Failure
2. View All Failures
3. Find Matching Failures
4. Show Repeated Patterns
5. Show High-Impact Failures
6. Analyze Failure Patterns
7. Show Recommendation
8. Exit
```

Record several failures.

For example:

```text
F001 → Payment API → Timeout → Database delay → Production
F002 → Payment API → Timeout → Database delay → Production
F003 → Payment API → Timeout → Database delay → Production
```

Then select:

```text
4. Show Repeated Patterns
```

The system can identify:

```text
Component Patterns:
  Payment API: 3 occurrence(s) -> Recurring Pattern

Category Patterns:
  Timeout: 3 occurrence(s) -> Recurring Pattern

Cause Patterns:
  Database delay: 3 occurrence(s) -> Recurring Pattern

Environment Patterns:
  Production: 3 occurrence(s) -> Recurring Pattern
```

It can also identify the exact repeated combination.

---

## Real-World Use Cases

FailurePattern can be useful for:

* Software incident analysis
* Production failure analysis
* IT operations
* QA teams
* DevOps workflows
* Service reliability analysis
* Manufacturing failures
* Equipment maintenance
* Customer support incidents
* Process quality analysis

The underlying idea is simple:

> **Repeated failures should be investigated as patterns, not only as individual incidents.**

---

## Future AI Enhancement

The current version intentionally uses deterministic Python logic.

An AI-enhanced version could later:

* Automatically classify failure categories
* Extract likely causes from incident descriptions
* Detect semantic similarity between different failure descriptions
* Discover patterns that use different wording
* Suggest likely root causes
* Summarize recurring incident clusters
* Predict which failure patterns may become more serious
* Recommend preventive actions

For example:

```text
"Payment request took too long"
"Checkout API exceeded timeout"
"Payment service response was delayed"
```

A traditional exact-value system may treat these as different descriptions.

An AI-enhanced version could recognize that they may describe the same underlying pattern.

---

## Why This Is Useful

Many systems already record failures.

The harder problem is recognizing:

```text
Individual Incidents
       ↓
Repeated Characteristics
       ↓
Recurring Pattern
       ↓
Investigation
       ↓
Preventive Action
```

FailurePattern demonstrates this reasoning using a small, understandable Python OOP implementation.

---

## Technologies

* Python
* Object-Oriented Programming
* Dictionaries
* Lists
* Sets
* Command-Line Interface

No external packages are required.

---

## License

This project is available for learning, portfolio, and personal development purposes.
