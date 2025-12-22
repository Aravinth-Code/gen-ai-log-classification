import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message):
            return label
    return None

if __name__ == "__main__":
    test_logs = [
        "User User123 logged in.",
        "Backup started at 2024-06-01 10:00:00.",
        "System updated to version 2.1.0.",
        "File report.pdf uploaded successfully by user Alice.",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user Admin.",
        "Account with ID 456 created by Bob."
    ]
    for log in test_logs:
        classification = classify_with_regex(log)
        print(f"Log: '{log}' => Classification: '{classification}'")