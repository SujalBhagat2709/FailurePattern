from failure_pattern import FailurePattern


def print_failure(failure):
    print("\n" + "-" * 60)
    print(f"Failure ID   : {failure['failure_id']}")
    print(f"Title        : {failure['title']}")
    print(f"Component    : {failure['component']}")
    print(f"Category     : {failure['category']}")
    print(f"Cause        : {failure['cause']}")
    print(f"Environment  : {failure['environment']}")
    print(f"Severity     : {failure['severity']}")
    print("-" * 60)


def show_failures(system):
    failures = system.list_failures()

    if not failures:
        print("\nNo failures recorded.")
        return

    print("\n=== Recorded Failures ===")

    for failure in failures:
        print_failure(failure)


def show_patterns(system):
    print("\n=== Repeated Failure Patterns ===")

    pattern_types = [
        ("component", "Component"),
        ("category", "Category"),
        ("cause", "Cause"),
        ("environment", "Environment"),
        ("severity", "Severity"),
    ]

    found = False

    for pattern_type, label in pattern_types:
        patterns = system.get_repeated_patterns(pattern_type)

        if patterns:
            found = True
            print(f"\n{label} Patterns:")

            for value, count in patterns.items():
                print(
                    f"  {value}: {count} occurrence(s) "
                    f"-> {system.get_pattern_strength(count)}"
                )

    exact_patterns = system.find_exact_patterns()

    if exact_patterns:
        found = True
        print("\nExact Failure Patterns:")

        for pattern in exact_patterns:
            print(
                f"  {pattern['component']} | "
                f"{pattern['category']} | "
                f"{pattern['cause']} | "
                f"{pattern['environment']} "
                f"-> {pattern['count']} occurrence(s)"
            )

    if not found:
        print("\nNo repeated patterns found.")


def create_failure(system):
    print("\n=== Record Failure ===")

    failure_id = input("Failure ID: ").strip()
    title = input("Failure title: ").strip()
    component = input("Component: ").strip()
    category = input("Category: ").strip()
    cause = input("Cause: ").strip()
    environment = input("Environment: ").strip()
    severity = input(
        "Severity (low/medium/high/critical): "
    ).strip().lower()

    try:
        system.record_failure(
            failure_id=failure_id,
            title=title,
            component=component,
            category=category,
            cause=cause,
            environment=environment,
            severity=severity,
        )

        print("\nFailure recorded successfully.")

    except ValueError as error:
        print(f"\nError: {error}")


def find_matching_failures(system):
    print("\n=== Find Matching Failures ===")
    print("Press Enter to skip any filter.")

    component = input("Component: ").strip() or None
    category = input("Category: ").strip() or None
    cause = input("Cause: ").strip() or None
    environment = input("Environment: ").strip() or None
    severity = input("Severity: ").strip().lower() or None

    matches = system.find_matching_failures(
        component=component,
        category=category,
        cause=cause,
        environment=environment,
        severity=severity,
    )

    if not matches:
        print("\nNo matching failures found.")
        return

    print(f"\nFound {len(matches)} matching failure(s).")

    for failure in matches:
        print_failure(failure)


def analyze_system(system):
    print("\n=== Failure Pattern Analysis ===")

    analysis = system.analyze()

    print(f"\nTotal Failures       : {analysis['total_failures']}")
    print(f"Overall Status       : {analysis['overall_status']}")

    print("\nTop Patterns:")

    for pattern_type, data in analysis["top_patterns"].items():
        if data:
            print(
                f"  {pattern_type.title():<15}: "
                f"{data['value']} "
                f"({data['count']} occurrence(s))"
            )
        else:
            print(f"  {pattern_type.title():<15}: None")

    print("\nExact Repeated Patterns:")

    if analysis["exact_patterns"]:
        for pattern in analysis["exact_patterns"]:
            print(
                f"  {pattern['component']} | "
                f"{pattern['category']} | "
                f"{pattern['cause']} | "
                f"{pattern['environment']} "
                f"-> {pattern['count']} occurrence(s)"
            )
    else:
        print("  None")

    print(f"\nHigh-Impact Failures : {analysis['high_impact_count']}")

    print("\nRecommendation:")
    print(f"  {analysis['recommendation']}")


def show_high_impact(system):
    failures = system.get_high_impact_failures()

    print("\n=== High-Impact Failures ===")

    if not failures:
        print("No high-impact failures found.")
        return

    for failure in failures:
        print_failure(failure)


def main():
    system = FailurePattern()

    while True:
        print("\n" + "=" * 60)
        print("             FAILURE PATTERN STUDIO")
        print("=" * 60)

        print("1. Record Failure")
        print("2. View All Failures")
        print("3. Find Matching Failures")
        print("4. Show Repeated Patterns")
        print("5. Show High-Impact Failures")
        print("6. Analyze Failure Patterns")
        print("7. Show Recommendation")
        print("8. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            create_failure(system)

        elif choice == "2":
            show_failures(system)

        elif choice == "3":
            find_matching_failures(system)

        elif choice == "4":
            show_patterns(system)

        elif choice == "5":
            show_high_impact(system)

        elif choice == "6":
            analyze_system(system)

        elif choice == "7":
            print("\n=== Recommendation ===")
            print(system.generate_recommendation())

        elif choice == "8":
            print("\nExiting Failure Pattern Studio. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
