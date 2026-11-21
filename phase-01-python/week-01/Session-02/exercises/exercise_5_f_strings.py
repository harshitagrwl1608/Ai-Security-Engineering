"""Exercise 5: Format a security event using an f-string."""

event_type = "Failed Login"
source_ip = "192.168.1.105"
username = "admin"
severity = "HIGH"

message = f"[{severity}] {event_type} | Source: {source_ip} | User: {username}"
print(message)
