from random_data_generator import random_generator


def report_generate(events):
    severity_counts = {"high": 0, "medium": 0, "low": 0}
    failed_login_count = 0
    unique_ips = set()
    invalid_severity_count = 0

    for event in events:
        severity = event["severity"]

        if severity in severity_counts:
            severity_counts[severity] += 1
        else:
            invalid_severity_count += 1

        if event["event"] == "Failed Login":
            failed_login_count += 1

        unique_ips.add(event["source_ip"])

    print("========== NETGUARD CLI V2 ==========")
    print(f"Total events: {len(events)}")
    print("\nSeverity summary:")
    for severity in ("high", "medium", "low"):
        print(f"{severity.title()}: {severity_counts[severity]}")

    print(f"Failed logins: {failed_login_count}")
    print(f"Unique source IPs: {len(unique_ips)}")
    if invalid_severity_count:
        print(f"Alerts with invalid severity: {invalid_severity_count}")
    print("=====================================")


def filter_by_severity(events, target_severity):
    target_severity = target_severity.strip().lower()
    return [
        event for event in events
        if event["severity"] == target_severity
    ]


def sort_by_severity(events):
    severity_rank = {"high": 1, "medium": 2, "low": 3}
    return sorted(
        events,
        key=lambda event: severity_rank.get(event["severity"], 99)
    )


def group_by_ip(events):
    grouped = {}

    for event in events:
        source_ip = event["source_ip"]

        if source_ip not in grouped:
            grouped[source_ip] = []

        grouped[source_ip].append(event)

    return grouped


def main():
    events = random_generator()
    report_generate(events)

    target_severity = input(
        "\nEnter the severity to filter (low/medium/high): "
    ).strip().lower()

    if target_severity not in ("low", "medium", "high"):
        print("Invalid severity. Choose low, medium, or high.")
    else:
        filtered_events = filter_by_severity(events, target_severity)
        print(f"\nMatching {target_severity} alerts: {len(filtered_events)}")
        for event in filtered_events[:5]:
            print(event)
        if len(filtered_events) > 5:
            print(f"... and {len(filtered_events) - 5} more")

    ranked_events = sort_by_severity(events)
    print("\nFirst 10 alerts ranked by severity:")
    for event in ranked_events[:10]:
        print(event)

    grouped_events = group_by_ip(events)
    print("\nAlerts per source IP:")
    for source_ip, alerts in grouped_events.items():
        print(f"{source_ip}: {len(alerts)} alerts")

    grouped_total = sum(len(alerts) for alerts in grouped_events.values())
    print(f"\nGrouping validation: {grouped_total}/{len(events)} events accounted for")


if __name__ == "__main__":
    main()
