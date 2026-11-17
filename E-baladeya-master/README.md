# E-Baladiya frontend

A Django-template frontend for a Tunisian civic-tech administration platform.

## Structure

- `templates/base.html` - shared document shell and asset loading
- `templates/components/` - navbar, footer, and status badge partials
- `templates/home.html` - public homepage
- `templates/services.html` and `service_detail.html` - service catalogue
- `templates/dashboard.html` - citizen dashboard
- `templates/application_create.html`, `document_upload.html`, `verification_result.html`, `application_detail.html` - request flow
- `templates/employee_dashboard.html`, `employee_application_detail.html` - administration workspace
- `templates/analytics.html` - decision-support view
- `templates/login.html`, `register.html` - authentication screens
- `static/css/style.css` - public design system
- `static/css/app-shell.css` - authenticated and operational layouts
- `static/js/app.js` - small progressive-enhancement hooks

## URL names expected by the templates

`home`, `services`, `service_detail`, `dashboard`, `application_create`, `document_upload`, `verification_result`, `application_detail`, `employee_dashboard`, `employee_application_detail`, `analytics`, `login`, and `register`.

The project was scaffolded into this folder because the workspace did not contain an existing Django project or `manage.py`. Add the templates and static directories to the Django settings and connect the named views when wiring the backend.
