from frappe import _

def get_data():
    return [
        {
            "module_name": "PropVault",
            "label": _("Property Management"),
            "type": "module",
            "icon": "color-house",
            "color": "blue",
            "link": "#workspace/PropVault Property Management",
            "onboard": 1,
        }
    ]