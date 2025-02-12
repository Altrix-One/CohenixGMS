def get_notification_config():
    return {
        "for_doctype": {
            # Example configuration for notifications
            "Expense Claim": {"status": "Draft"},
            "Task": {"status": "Open"},
        }
    }