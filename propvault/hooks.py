app_name = "propvault"
app_title = "PropVault"
app_publisher = "EPI-USE"
app_description = "Secure Property and Rental Management"
app_email = "christiaan.swart@epiuse.com"
app_license = "mit"
app_icon = "/assets/propvault/PropVault.png"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
{
 		"name": "propvault",
		"logo": "/assets/propvault/PropVault.png",
 		"title": "PropVault",
		"route": "/app/propvault",
	}
]

# Includes in <head>
# ------------------
app_include_js = "/assets/propvault/js/propvault.js"
app_include_css = "/assets/propvault/css/propvault.css"

# Include desktop configuration
module_name = "PropVault"

# Call function

# Include js in doctype views

# Workspace
workspace_include_js = {
    "PropVault": "public/js/propvault_property_management.js"
}

#Add notifications
# notification_config = "propvault.notifications.get_notification_config"
# include js, css files in header of desk.html
# app_include_css = "/assets/propvault/css/propvault.css"
# app_include_js = "/assets/propvault/js/propvault.js"

# include js, css files in header of web template
# web_include_css = "/assets/propvault/css/propvault.css"
# web_include_js = "/assets/propvault/js/propvault.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "propvault/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "propvault/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "propvault.utils.jinja_methods",
# 	"filters": "propvault.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "propvault.install.before_install"
# after_install = "propvault.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "propvault.uninstall.before_uninstall"
# after_uninstall = "propvault.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "propvault.utils.before_app_install"
# after_app_install = "propvault.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "propvault.utils.before_app_uninstall"
# after_app_uninstall = "propvault.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "propvault.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"propvault.tasks.all"
# 	],
# 	"daily": [
# 		"propvault.tasks.daily"
# 	],
# 	"hourly": [
# 		"propvault.tasks.hourly"
# 	],
# 	"weekly": [
# 		"propvault.tasks.weekly"
# 	],
# 	"monthly": [
# 		"propvault.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "propvault.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "propvault.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "propvault.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["propvault.utils.before_request"]
# after_request = ["propvault.utils.after_request"]

# Job Events
# ----------
# before_job = ["propvault.utils.before_job"]
# after_job = ["propvault.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"propvault.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]
