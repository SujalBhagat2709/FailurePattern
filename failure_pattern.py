"""
FailurePattern
==============

A small Python OOP system for recording failures and identifying
recurring patterns across them.

Example:

Failure 1 → API → Timeout → Production
Failure 2 → API → Timeout → Production
Failure 3 → API → Timeout → Production

These may look like three separate incidents, but they share
the same characteristics.

FailurePattern groups those characteristics to reveal repeated
failure patterns.
"""


class FailurePattern:
    """Stores failures and analyzes recurring failure patterns."""

    def __init__(self):
        self.failures = {}

    def record_failure(
        self,
        failure_id,
        title,
        component,
        category,
        cause,
        environment,
        severity="medium"
    ):
        """
        Record a failure.

        severity:
            low
            medium
            high
            critical
        """
        if failure_id in self.failures:
            return False, "Failure ID already exists."

        valid_severities = {
            "low",
            "medium",
            "high",
            "critical"
        }

        severity = severity.lower().strip()

        if severity not in valid_severities:
            return False, (
                "Severity must be low, medium, high, "
                "or critical."
            )

        self.failures[failure_id] = {
            "title": title,
            "component": component,
            "category": category,
            "cause": cause,
            "environment": environment,
            "severity": severity
        }

        return True, "Failure recorded successfully."

    def get_failure(self, failure_id):
        """Return a failure by ID."""
        return self.failures.get(failure_id)

    def list_failures(self):
        """Return all recorded failures."""
        return self.failures

    def count_failures(self):
        """Return the total number of recorded failures."""
        return len(self.failures)

    def _normalize(self, value):
        """Normalize text for consistent pattern grouping."""
        return str(value).strip().lower()

    def get_component_patterns(self):
        """Group failures by component."""
        patterns = {}

        for failure in self.failures.values():
            component = self._normalize(
                failure["component"]
            )

            patterns[component] = (
                patterns.get(component, 0) + 1
            )

        return patterns

    def get_category_patterns(self):
        """Group failures by category."""
        patterns = {}

        for failure in self.failures.values():
            category = self._normalize(
                failure["category"]
            )

            patterns[category] = (
                patterns.get(category, 0) + 1
            )

        return patterns

    def get_cause_patterns(self):
        """Group failures by cause."""
        patterns = {}

        for failure in self.failures.values():
            cause = self._normalize(
                failure["cause"]
            )

            patterns[cause] = (
                patterns.get(cause, 0) + 1
            )

        return patterns

    def get_environment_patterns(self):
        """Group failures by environment."""
        patterns = {}

        for failure in self.failures.values():
            environment = self._normalize(
                failure["environment"]
            )

            patterns[environment] = (
                patterns.get(environment, 0) + 1
            )

        return patterns

    def get_severity_patterns(self):
        """Group failures by severity."""
        patterns = {}

        for failure in self.failures.values():
            severity = self._normalize(
                failure["severity"]
            )

            patterns[severity] = (
                patterns.get(severity, 0) + 1
            )

        return patterns

    def get_repeated_patterns(self, pattern_type):
        """
        Return patterns that occur more than once.

        Supported pattern types:
            component
            category
            cause
            environment
            severity
        """
        pattern_methods = {
            "component": self.get_component_patterns,
            "category": self.get_category_patterns,
            "cause": self.get_cause_patterns,
            "environment": self.get_environment_patterns,
            "severity": self.get_severity_patterns
        }

        pattern_type = pattern_type.lower().strip()

        if pattern_type not in pattern_methods:
            return {}

        patterns = pattern_methods[pattern_type]()

        return {
            name: count
            for name, count in patterns.items()
            if count > 1
        }

    def get_top_pattern(self, pattern_type):
        """Return the most frequently repeated pattern."""
        pattern_methods = {
            "component": self.get_component_patterns,
            "category": self.get_category_patterns,
            "cause": self.get_cause_patterns,
            "environment": self.get_environment_patterns,
            "severity": self.get_severity_patterns
        }

        pattern_type = pattern_type.lower().strip()

        if pattern_type not in pattern_methods:
            return None

        patterns = pattern_methods[pattern_type]()

        if not patterns:
            return None

        return max(
            patterns.items(),
            key=lambda item: item[1]
        )

    def find_matching_failures(
        self,
        component=None,
        category=None,
        cause=None,
        environment=None,
        severity=None
    ):
        """
        Find failures sharing the supplied characteristics.
        """
        matches = []

        for failure_id, failure in self.failures.items():

            if (
                component is not None
                and self._normalize(
                    failure["component"]
                ) != self._normalize(component)
            ):
                continue

            if (
                category is not None
                and self._normalize(
                    failure["category"]
                ) != self._normalize(category)
            ):
                continue

            if (
                cause is not None
                and self._normalize(
                    failure["cause"]
                ) != self._normalize(cause)
            ):
                continue

            if (
                environment is not None
                and self._normalize(
                    failure["environment"]
                ) != self._normalize(environment)
            ):
                continue

            if (
                severity is not None
                and self._normalize(
                    failure["severity"]
                ) != self._normalize(severity)
            ):
                continue

            matches.append({
                "failure_id": failure_id,
                **failure
            })

        return matches

    def find_exact_patterns(self):
        """
        Find combinations of component, category, cause,
        and environment that appear more than once.
        """
        combinations = {}

        for failure in self.failures.values():
            key = (
                self._normalize(failure["component"]),
                self._normalize(failure["category"]),
                self._normalize(failure["cause"]),
                self._normalize(failure["environment"])
            )

            combinations[key] = (
                combinations.get(key, 0) + 1
            )

        repeated = []

        for key, count in combinations.items():
            if count > 1:
                repeated.append({
                    "component": key[0],
                    "category": key[1],
                    "cause": key[2],
                    "environment": key[3],
                    "count": count
                })

        return sorted(
            repeated,
            key=lambda pattern: pattern["count"],
            reverse=True
        )

    def get_high_impact_failures(self):
        """Return high and critical severity failures."""
        return [
            {
                "failure_id": failure_id,
                **failure
            }
            for failure_id, failure in self.failures.items()
            if failure["severity"] in {
                "high",
                "critical"
            }
        ]

    def get_pattern_strength(self, count):
        """
        Classify how strongly a pattern is repeating.
        """
        if count <= 1:
            return "Unique"

        if count == 2:
            return "Emerging Pattern"

        if count <= 4:
            return "Recurring Pattern"

        return "Strong Pattern"

    def get_overall_pattern_status(self):
        """Determine the overall pattern status."""
        if not self.failures:
            return "No Failures Recorded"

        exact_patterns = self.find_exact_patterns()

        if not exact_patterns:
            repeated_causes = self.get_repeated_patterns(
                "cause"
            )

            if repeated_causes:
                return "Partial Pattern"

            return "No Clear Pattern"

        strongest = exact_patterns[0]

        if strongest["count"] >= 5:
            return "Strong Recurring Pattern"

        if strongest["count"] >= 3:
            return "Recurring Pattern"

        return "Emerging Pattern"

    def generate_recommendation(self):
        """Generate a recommendation from the detected patterns."""
        if not self.failures:
            return (
                "Record failures before attempting to identify "
                "recurring patterns."
            )

        exact_patterns = self.find_exact_patterns()

        if exact_patterns:
            strongest = exact_patterns[0]

            return (
                "Investigate the recurring combination of "
                f"component '{strongest['component']}', "
                f"cause '{strongest['cause']}', and "
                f"environment '{strongest['environment']}'. "
                f"It appears {strongest['count']} times."
            )

        repeated_causes = self.get_repeated_patterns(
            "cause"
        )

        if repeated_causes:
            cause, count = max(
                repeated_causes.items(),
                key=lambda item: item[1]
            )

            return (
                f"Investigate the repeated cause "
                f"'{cause}'. It appears in {count} "
                "recorded failures."
            )

        repeated_components = self.get_repeated_patterns(
            "component"
        )

        if repeated_components:
            component, count = max(
                repeated_components.items(),
                key=lambda item: item[1]
            )

            return (
                f"Review component '{component}' because "
                f"it appears in {count} recorded failures."
            )

        return (
            "No strong recurring pattern has been identified. "
            "Continue recording failures to build enough "
            "evidence for pattern analysis."
        )

    def analyze(self):
        """Return a complete failure-pattern analysis."""
        return {
            "failure_count": self.count_failures(),
            "component_patterns": (
                self.get_component_patterns()
            ),
            "category_patterns": (
                self.get_category_patterns()
            ),
            "cause_patterns": (
                self.get_cause_patterns()
            ),
            "environment_patterns": (
                self.get_environment_patterns()
            ),
            "severity_patterns": (
                self.get_severity_patterns()
            ),
            "repeated_components": (
                self.get_repeated_patterns("component")
            ),
            "repeated_categories": (
                self.get_repeated_patterns("category")
            ),
            "repeated_causes": (
                self.get_repeated_patterns("cause")
            ),
            "repeated_environments": (
                self.get_repeated_patterns("environment")
            ),
            "exact_patterns": self.find_exact_patterns(),
            "high_impact_failures": (
                self.get_high_impact_failures()
            ),
            "overall_status": (
                self.get_overall_pattern_status()
            ),
            "recommendation": (
                self.generate_recommendation()
            )
        }

    def display_analysis(self):
        """Display the complete failure-pattern analysis."""
        analysis = self.analyze()

        print("\n" + "=" * 65)
        print("FAILUREPATTERN ANALYSIS")
        print("=" * 65)

        print(
            f"Total Failures: "
            f"{analysis['failure_count']}"
        )

        print(
            f"Overall Status: "
            f"{analysis['overall_status']}"
        )

        print("\nRepeated Components:")

        if analysis["repeated_components"]:
            for name, count in (
                analysis["repeated_components"].items()
            ):
                print(
                    f"  - {name}: {count}"
                )
        else:
            print("  None")

        print("\nRepeated Categories:")

        if analysis["repeated_categories"]:
            for name, count in (
                analysis["repeated_categories"].items()
            ):
                print(
                    f"  - {name}: {count}"
                )
        else:
            print("  None")

        print("\nRepeated Causes:")

        if analysis["repeated_causes"]:
            for name, count in (
                analysis["repeated_causes"].items()
            ):
                print(
                    f"  - {name}: {count}"
                )
        else:
            print("  None")

        print("\nRepeated Environments:")

        if analysis["repeated_environments"]:
            for name, count in (
                analysis["repeated_environments"].items()
            ):
                print(
                    f"  - {name}: {count}"
                )
        else:
            print("  None")

        print("\nExact Repeating Patterns:")

        if analysis["exact_patterns"]:
            for number, pattern in enumerate(
                analysis["exact_patterns"],
                start=1
            ):
                print(
                    f"\n  {number}. "
                    f"{pattern['component']} | "
                    f"{pattern['category']} | "
                    f"{pattern['cause']} | "
                    f"{pattern['environment']}"
                )

                print(
                    f"     Occurrences: "
                    f"{pattern['count']}"
                )

                print(
                    f"     Strength: "
                    f"{self.get_pattern_strength(pattern['count'])}"
                )
        else:
            print("  None")

        print("\nHigh-Impact Failures:")

        if analysis["high_impact_failures"]:
            for failure in (
                analysis["high_impact_failures"]
            ):
                print(
                    f"  - "
                    f"{failure['failure_id']}: "
                    f"{failure['title']} "
                    f"({failure['severity']})"
                )
        else:
            print("  None")

        print("\nRecommendation:")
        print(
            f"  {analysis['recommendation']}"
        )

        print("=" * 65)
