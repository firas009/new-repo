# E-Baladiya — Ichrak's Setup, Implementation & Handoff Guide

**From:** Firas (backend foundation)  
**To:** Ichrak (citizen requests, document uploads, verification)  
**Project:** E-Baladiya — Tunisian digital municipal services  
**Stack:** Python 3.13 (version used for Firas's verified run), Django 5.2-compatible project, SQLite, Django templates, Bootstrap  
**Delivery method:** Project ZIP shared through Messenger (no Git required)

> **Read this first.** This is an execution guide, not a claim that Ichrak's features already exist. Firas has built the database foundation, authentication and role-based route protection. The application-creation, upload, verification and correction workflows are still to be implemented. **Do not remove existing URL names, models, migrations or security decorators.**

---

## 0. Current baseline and ownership

### Verified on Firas's machine (16 November 2026)

| Check | Verified result |
|---|---|
| `python manage.py check` | No issues |
| `python manage.py makemigrations --check --dry-run` | No changes detected |
| `python manage.py test core -v 2` | **39 tests passed** (12 database, 14 authentication, 13 permissions) |
| `python manage.py seed_services` | **26 municipal services, 62 required documents** |
| Citizen registration/login/logout | Implemented, tested |
| Employee / citizen route restrictions | Implemented, tested |
| Local Django security audit | Appropriate for **local HTTP development** |
| Application ownership and private file download endpoints | **Not yet implemented/verified end to end** |

**Role boundaries:** Firas built the foundation; **Ichrak** owns catalogue database integration, request creation, document upload, verification, corrections and routing; **Yosser** owns employee decisions, final-document generation and notifications; **Sarah** owns analytics, end-to-end QA and deployment readiness.

### Do not share these files in the ZIP

- `.env` (real secret key and environment values)
- `db.sqlite3` (local user and application data)
- `.venv/` (machine-specific packages)
- `private_media/` and `media/` (private uploaded files)
- `__pycache__/`, `*.pyc`, logs and generated `staticfiles/`

**Include** `manage.py`, `requirements.txt`, `.env.example`, `eb_web/`, `core/` **including migrations and management commands**, `templates/`, `static/`, and this guide. If `BACKEND_HANDOFF_FIRAS.md` exists, include it too.

---

# PART A — INSTALL AND LAUNCH THE PROJECT

## A1. Extract the ZIP

1. Download the project ZIP from Messenger.
2. Extract it into a normal Windows folder, for example `C:\Users\Ichrak\Documents\E-Baladiya`.
3. Open **the folder containing `manage.py`** in Visual Studio Code (**File → Open Folder**).
4. Open **Terminal → New Terminal**; use **PowerShell**.

Expected structure (additional files are normal):

```text
E-Baladiya/
├── manage.py
├── requirements.txt
├── .env.example
├── eb_web/
│   ├── settings.py
│   └── urls.py
├── core/
│   ├── models.py
│   ├── admin.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── migrations/
│   ├── management/commands/seed_services.py
│   ├── test_auth.py
│   ├── test_permissions.py
│   └── tests/
├── templates/
└── static/
```

**If `manage.py`, `.env.example`, migrations or `seed_services.py` is missing, ask Firas for a corrected ZIP before proceeding.**

## A2. Verify Python

```powershell
python --version
py --version
```

Prefer **Python 3.13**, the version on which the 39 baseline tests passed. If Python is missing, install it and reopen the terminal. The `py` launcher is commonly available on Windows; if not, use `python` for virtual-environment creation.

## A3. Create and activate a new virtual environment

From the root directory containing `manage.py`:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Expected prefix: `(.venv) PS ...`.

If PowerShell blocks activation, for this terminal session only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

If `py -3.13` does not exist but `python --version` shows a compatible version, use `python -m venv .venv` instead.

## A4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m django --version
```

**Package check:** The initial uploaded requirements file listed Django only, while the configured `eb_web/settings.py` uses `from dotenv import load_dotenv`. Firas should include **`python-dotenv` in the final requirements file**. If the copied environment produces `ModuleNotFoundError: No module named 'dotenv'`, temporarily run:

```powershell
python -m pip install python-dotenv
```

Then update `requirements.txt` in the project copy so the next teammate does not encounter the same error. Do not replace or downgrade dependencies blindly; use the compatible versions provided in the final ZIP.

## A5. Create a local `.env` file

```powershell
Copy-Item .env.example .env
```

Generate a **new** Django secret key on Ichrak's machine:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated string into `.env` as `SECRET_KEY=...`. Do **not** reuse Firas's personal `.env` or share the resulting secret.

Example local-development values (adjust to match `eb_web/settings.py` and `.env.example`):

```dotenv
SECRET_KEY=REPLACE_WITH_THE_LOCALLY_GENERATED_SECRET
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_PATH=db.sqlite3
MEDIA_ROOT=private_media
MEDIA_URL=/media/
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=noreply@ebaladiya.local
VERIFICATION_PROVIDER=mock
```

Use these **only for local development**. Do not enable HTTPS-only cookies or automatic HTTPS redirects while testing on plain `http://127.0.0.1:8000/`.

## A6. Create the local database and run migrations

Because the ZIP should **not** include Firas's `db.sqlite3`, the database starts empty.

```powershell
python manage.py migrate
```

Expected: migrations for `core`, `auth`, `admin`, `contenttypes` and `sessions` apply successfully.

**Do not recreate the existing migration files with `makemigrations`.** They should already be in the ZIP.

## A7. Seed the municipal service catalogue

```powershell
python manage.py seed_services
```

Expected:

```text
Municipal catalogue seeded successfully.
Total services: 26
Total required documents: 62
```

Confirm using an independent database query:

```powershell
python manage.py shell -c "from core.models import MunicipalService, RequiredDocument; print('Services:', MunicipalService.objects.count()); print('Documents:', RequiredDocument.objects.count())"
```

Expected: `Services: 26`, `Documents: 62`. The seed is intended to be rerunnable without duplicating existing definitions.

## A8. Verify the untouched baseline before coding

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test core -v 2
```

Expected:

```text
System check identified no issues (0 silenced).
No changes detected
...
Ran 39 tests
OK
```

**Stop and fix any setup discrepancy before modifying the application.** The 39 tests comprise 12 model-integrity tests, 14 authentication tests and 13 role-permission tests. The six earlier catalogue-seeding checks were not visible in Firas's final 39-test output; do not assume those are currently discovered by Django.

Warnings from CSRF tests rejecting requests without tokens are expected **when those tests pass**.

## A9. Start the server and create local accounts

```powershell
python manage.py createsuperuser
python manage.py runserver
```

The first command creates a **new local** superuser. Use a strong unique password; never put it in this document. The second starts the development server.

Open these pages:

| URL (prepend `http://127.0.0.1:8000`) | Expected |
|---|---|
| `/` | Homepage opens |
| `/services/` | Catalogue template opens (may still use Python dictionary) |
| `/register/` | Citizen registration works |
| `/login/` | Email-based login works |
| `/dashboard/` | Requires authentication |
| `/administration/` | Requires employee/admin role |
| `/admin/` | Django superuser admin |

Create a **citizen** through `/register/`. Public registration must always assign `Profile.Role.CITIZEN`, not employee/admin privileges. For staff workflow tests, use a separately created municipal employee profile; do not grant `is_superuser=True` or `is_staff=True` just to access E-Baladiya's employee portal.

For a baseline manual security check: anonymous visitors should be redirected away from `/dashboard/`; logged-in citizens should receive HTTP 403 on `/administration/`; a superuser can access `/administration/`.

**At this point, setup is finished. Begin Part B.**

---

# PART B — WHAT ALREADY EXISTS AND WHAT TO PRESERVE

## B1. Read the current files first

| File | Purpose |
|---|---|
| `eb_web/settings.py` | Database, installed apps, dotenv, private media, security |
| `eb_web/urls.py` | Main project URL entry points |
| `core/models.py` | Shared models and integrity rules |
| `core/admin.py` | Admin registrations |
| `core/services.py` | Original in-memory service catalogue; source for seed |
| `core/views.py` | Existing views and authentication views |
| `core/urls.py` | Public, request, auth, administration routes |
| `core/forms.py` | Registration/login forms |
| `core/permissions.py` | `employee_required` and `administrator_required` |
| `templates/services.html`, `service_detail.html` | Catalogue views |
| `templates/application_create.html` | Application form |
| `templates/document_upload.html` | File upload page |
| `templates/verification_result.html` | Verification page |
| `templates/application_detail.html` | Application tracking/details |
| `templates/employee_dashboard.html` | Employee placeholder, primarily Yosser's work |

### Existing models (do not duplicate them)

1. `User` — custom Django user, login identifier is `email`.
2. `Profile` — citizen contact/identity fields and role.
3. `MunicipalService` — service metadata, `slug`, `is_active`, `processing_type`.
4. `RequiredDocument` — per-service document definitions, allowed types, max file size.
5. `Application` — applicant, service, reference, status, assigned employee, timestamps.
6. `ApplicationField` — service-specific field/value pairs.
7. `UploadedDocument` — file metadata, version, document status, active flag, hash.
8. `DocumentVerification` — provider, score, overall result, timestamp.
9. `VerificationCheck` — check type, result, score, message.
10. `ApplicationEvent` — auditable request history.
11. `EmployeeComment` — employee notes.
12. `Notification` — notification record.
13. `GeneratedDocument` — final output file and delivery information.

Key relations:

```text
User ── Profile
User ──< Application >── MunicipalService ──< RequiredDocument
Application ──< ApplicationField
Application ──< ApplicationEvent
Application ──< UploadedDocument >── RequiredDocument
UploadedDocument ──< DocumentVerification ──< VerificationCheck
```

### Application statuses — use these exact values

`draft`, `documents_pending`, `verification_pending`, `correction_required`, `manual_review`, `additional_documents_required`, `approved`, `rejected`, `completed`, `cancelled`.

Document upload statuses: `pending`, `checking`, `valid`, `invalid`, `replaced`.

Verification outcomes: `valid`, `invalid`, `incomplete`, `manual_review`.

Service processing types: `automatic`, `manual_review`.

### Security contracts to preserve

- `login_required` protects citizen request routes and dashboard.
- `employee_required` protects `/administration/` views; Django `is_staff` alone does **not** grant municipal employee access.
- Registration must not allow users to choose elevated roles or privileges.
- Logout must be an HTTP **POST** with `{% csrf_token %}`.
- Never use a submitted `applicant_id` to choose the citizen owner. Use `request.user`.
- Firas did **not** finish or verify per-application ownership and private file-download endpoints. **Ichrak must implement these with the real workflows**.
- Django project's `eb_web/urls.py` has **no public media-serving route**. Keep private media inaccessible by direct public URL.

### Current route names worth preserving

`home`, `services`, `service_detail`, `service_detail_slug`, `register`, `login`, `logout`, `dashboard`, `application_create_generic`, `application_create`, `document_upload`, `document_upload_service`, `verification_result`, `verification_result_service`, `application_review`, `application_review_service`, `application_complete`, `application_complete_service`, `application_detail`, `employee_dashboard`, `employee_application_detail`, `analytics`.

**Caution:** Several request routes and templates are currently static placeholders. Do not confuse a page that renders with a database-backed workflow. The existing generic `/requests/detail/` path is not a secure application-ID lookup; introduce authorization-aware record-specific routes as needed.

---

# PART C — ICHRAK'S DEVELOPMENT PLAN (IN ORDER)

Work one phase at a time. After each phase: run `python manage.py check`, test the relevant flow in the browser, and run `python manage.py test core -v 2`. Do not introduce new migrations unless you have actually changed a model and coordinated that change with the team.

## C1. Replace the in-memory catalogue with database-backed services

**Objective:** The frontend reads the `MunicipalService` and `RequiredDocument` tables created and seeded by Firas.

**Main files:** `core/views.py`, `templates/services.html`, `templates/service_detail.html` (and any frontend filtering logic).

1. Review `services_catalogue()`, `service_detail()`, and `default_service_detail()`.
2. Replace uses of `SERVICES` / `SERVICES_BY_SLUG` as the authoritative data source with ORM queries.
3. Display only **active** services to public visitors.
4. Group and render categories; preserve search/filter behavior and existing URLs/slugs.
5. Fetch the required documents and show accepted file types, maximum size, required/optional status and order.
6. Show the correct eligibility, fees, issuing authority, description and processing type.
7. Return HTTP 404 for nonexistent or inactive services.

Illustrative query (adapt the context structure to the existing templates):

```python
from django.shortcuts import get_object_or_404
from .models import MunicipalService

services = MunicipalService.objects.filter(is_active=True).order_by('category', 'name')
service = get_object_or_404(
    MunicipalService.objects.prefetch_related('required_documents'),
    slug=service_slug,
    is_active=True,
)
```

**Acceptance check:** Edit a service's display information or active flag in Django Admin. The public pages update correctly **without editing `core/services.py`**. Counts and document requirements remain consistent.

## C2. Create real citizen applications

**Objective:** A logged-in citizen selects an active service and saves a real `Application` plus service-specific `ApplicationField` records.

**Main files:** `core/views.py`, `core/forms.py` (create a dedicated application form if helpful), `core/urls.py`, `templates/application_create.html`, `core/models.py` (only if truly necessary).

1. Keep application-creation routes protected by `login_required`.
2. Confirm that a user eligible to submit can select an **active** service by its database ID/slug.
3. Validate required fields and relevant eligibility rules on the **server**, not just with HTML or JavaScript.
4. Set `applicant=request.user` in backend code. Ignore any untrusted submitted owner/user ID.
5. Save an `Application` with initial status `draft` or `documents_pending`.
6. Generate a **unique human-readable reference**, e.g., `REQ-2026-00001`, safely under concurrent submissions. The model's `reference_number` is currently nullable; a reference-generation workflow is **not** automatically provided by the field itself.
7. Save service-specific user inputs via `ApplicationField`.
8. Create a corresponding `ApplicationEvent` for creation; use `transaction.atomic()` for changes that must succeed together.
9. Prevent accidental duplicate submissions (e.g., double-click); do not make up uniqueness rules that would block legitimate reapplications.
10. Redirect to the correct next step using that particular application ID/reference (not only the service slug).

**Security requirement:** Add a real ownership-checked application detail/lookup. For citizen-facing endpoints, constrain database queries by both ID **and** `applicant=request.user`. A nonexistent or foreign-owned record should return an appropriate 404 without exposing its details. Employees require separate assignment/scope rules.

**Acceptance check:** Two separate citizens can create applications. Each application belongs to the correct user, has the right service and status, stores submitted fields and an event, and **cannot** be viewed or modified by the other citizen.

## C3. Secure private document uploads and versioning

**Objective:** A citizen submits every required document for **their own** application; files stay private and their metadata is persisted.

**Main files:** `core/views.py`, upload forms/validators, `templates/document_upload.html`, `UploadedDocument` and `RequiredDocument` models.

1. Use `<form method="post" enctype="multipart/form-data">` plus `{% csrf_token %}`.
2. Receive files through `request.FILES`; validate that the application belongs to the requester.
3. Validate against the `RequiredDocument` belonging to the application's service.
4. Check maximum size, nonempty file, extension and **actual file format/content** (do not rely solely on browser-supplied MIME type or extension).
5. Reject executable or malformed uploads, unsafe names, unsupported formats and unnecessary duplicate submissions.
6. Generate a safe storage name, preserve the original filename only as metadata, compute a SHA-256 hash and record MIME/size.
7. Save to the configured **private** `MEDIA_ROOT`, never under `static/` or a public web path.
8. Preserve document versions on replacement. Respect database constraints: `(application, required_document, version)` must be unique; only **one active version** for a given application and document requirement.
9. Implement authorized **download/preview** endpoints: check the authenticated user owns the application (or is a properly authorized employee) **before** opening the file. Avoid leaking private storage paths or accepting arbitrary file paths from URL parameters.
10. Return clear validation errors and display the current required/missing documents.
11. Add limits to prevent oversized uploads and excessive resource use.

**Acceptance check:** Correct test files upload and create metadata; invalid, oversized, malformed, wrong-service and unauthorized uploads fail safely; replacements produce new versions; a different citizen cannot fetch the file or its metadata.

## C4. Implement document verification using a mock provider first

**Objective:** Introduce a replaceable verifier and persist checks, scores, result and reasons.

**Main files:** New verification service module(s), `DocumentVerification`, `VerificationCheck`, `templates/verification_result.html`, integration in views.

1. Define a provider abstraction. Keep verification logic separate from HTTP views.
2. Start with a **deterministic local mock** provider for controlled scenarios; do not pretend its outputs prove real document authenticity.
3. Make provider selection configurable through `VERIFICATION_PROVIDER=mock`.
4. Define structured results for check type, pass/fail/unknown, numeric score when appropriate, message and overall outcome.
5. Persist `DocumentVerification` and its `VerificationCheck` children; associate them with the correct `UploadedDocument` and version.
6. Support required-field presence, document type, format, issuing authority, identifier/reference and cross-document consistency checks, beginning with what can actually be verified in the mock scenario.
7. Keep `valid`, `invalid`, `incomplete`, `manual_review` distinct. On provider error, **fail explicitly**, not as a silently successful validation.
8. Avoid storing unnecessary raw sensitive OCR/provider output.
9. Make future OCR/AI implementations plug into the same interface without rewriting application logic. A real OCR/trusted-database integration is **later work** unless separately agreed.

Suggested interface:

```python
class VerificationProvider:
    def verify(self, document, application):
        raise NotImplementedError
```

**Acceptance check:** Mock test cases yield predictable valid/invalid/incomplete/manual-review results. The outcome, check reasons, score and provider are saved and displayed to the citizen.

## C5. Correction and re-upload loop

**Objective:** Invalid or incomplete submissions can be corrected while preserving their history.

1. If verification fails, transition the application to `correction_required` when the workflow warrants it.
2. Record exactly **which document** failed and the human-readable reason.
3. Create an `ApplicationEvent` for the change.
4. Show the citizen the missing/invalid document and re-upload action.
5. Accept a replacement only after checking application ownership and document requirement.
6. Preserve previous file versions and their verification records; mark the replaced version appropriately.
7. Return the application to verification and recompute completeness.
8. Prevent an invalid/incomplete request from advancing as if it had passed verification.
9. Expose a suitable event/hook for Yosser's notification implementation rather than assuming emails already exist.

**Acceptance check:** Upload an intentionally invalid test document → see rejection reason → upload a valid replacement → verify again → retain past versions and event history.

## C6. Route requests to automatic or manual processing

**Objective:** Use database `MunicipalService.processing_type` after verification to move requests to the next part of the workflow.

1. Verify all **required** documents and completeness criteria before advancement.
2. If `processing_type == 'manual_review'`, transition to `Application.Status.MANUAL_REVIEW` and expose the request to the employee queue Yosser will implement.
3. If `processing_type == 'automatic'` and checks pass, prepare the eligible request for **Yosser's document-generation flow**. Do not claim a final document exists until generation succeeds.
4. Record every routing decision as an `ApplicationEvent`.
5. Centralize allowed status transitions; reject impossible transitions such as `rejected → approved` without an approved business process.
6. Make transitions atomic and safe against duplicate submissions or repeated callbacks.

**Acceptance check:** A valid manually processed service reaches the manual queue; an eligible automatic service enters the generation handoff; failed verification never reaches approval/generation. Audit entries explain what happened.

---

# PART D — TESTING AND SECURITY REQUIREMENTS

## D1. Run existing checks after each major change

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test core -v 2
```

- If intentional model changes were made, create/review migrations and apply them; otherwise `No changes detected` remains the goal.
- The **existing 39** tests must continue to pass. Add focused tests for the new functionality even though Firas deferred standalone object-access tests: ownership and private file security **must** be verified before handing the feature to Yosser.
- Do not change existing tests just to make an incorrect implementation appear green.

## D2. Required end-to-end scenarios

- [ ] Service catalogue uses database, supports categories and excludes inactive services.
- [ ] Citizen can create a correctly owned application with unique reference and initial status.
- [ ] Required fields and eligibility rules are validated server-side.
- [ ] Creation and status changes write audit events.
- [ ] Required documents upload to private storage and generate correct metadata.
- [ ] Wrong-service, invalid-format, corrupt and oversized files are rejected.
- [ ] Only the rightful citizen or explicitly authorized employee can access an application/document.
- [ ] Changing an application/document ID cannot reveal someone else's data.
- [ ] Replaced files create new versions while preserving prior evidence.
- [ ] Verification persists provider, outcome, score/checks and reasons.
- [ ] Provider failure cannot be mistaken for successful verification.
- [ ] Invalid/incomplete verification triggers the correction loop.
- [ ] A corrected upload can be reverified with intact audit history.
- [ ] Automatic/manual routing follows `processing_type` and appropriate permissions.
- [ ] Anonymous visitors cannot perform protected actions; POST forms have CSRF protection.
- [ ] Existing foundation tests still pass and new behavior has been checked.

## D3. Non-negotiable security notes

1. **Object-level access:** `@login_required` is not enough. Always check ownership on real application and document queries. Employee access must be scoped; the employee role should not imply unlimited access to every record.
2. **Private files:** Do not add `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` for private citizen uploads. Serve only through an authorized endpoint and secure storage configuration.
3. **Server-side validation:** Never trust IDs, status fields, MIME types, filenames, prices or roles sent by the browser.
4. **Transactions:** Coordinate document replacement, status changes, reference generation and events atomically when required.
5. **Sensitive data:** Do not paste real citizen documents/CINs or passwords into logs, screenshots, tests, Messenger, source code or fixtures.
6. **Local vs production:** Firas saw five expected `check --deploy` warnings because local development uses `DEBUG=True` and HTTP. Production deployment must later enable HTTPS, secure cookies, appropriate hosts, HSTS (after HTTPS validation) and `DEBUG=False`; Sarah owns deployment readiness.
7. **No public role elevation:** Citizen registration must remain citizen-only; do not permit profile-role changes through ordinary public forms.

---

# PART E — HANDOFF FROM ICHRAK TO YOSSER

## E1. What Yosser needs from Ichrak

Provide a short completion report and the updated project ZIP containing:

- Updated database-backed catalogue views and template context descriptions.
- Working application creation flow and URL names.
- Reference-generation approach, state-transition rules and event types.
- Secure upload endpoints, upload limits, validation rules and authorized download pattern.
- Verification provider interface, configuration, mock implementation and stored-result format.
- Correction/re-upload behavior, versioning rules and representative test cases.
- How a valid manual-review application becomes available for the employee queue.
- How a valid automatic application becomes eligible for Yosser's generation flow.
- Tests run and results, including any remaining known gaps.

**Yosser's scope** begins with employee queues/assignment, review/approval/rejection, final document generation and notifications. **Sarah's scope** includes analytics, complete integration tests, privacy/security audit and deployment.

## E2. How to send the updated ZIP without Git

1. Keep one working project copy; create **a separate clean handoff copy**.
2. In the clean copy, remove `.venv/`, `.env`, `db.sqlite3`, `private_media/`, `media/`, temporary files and caches.
3. Keep `manage.py`, `core/`, `eb_web/`, migrations, commands, `templates/`, `static/`, `requirements.txt`, `.env.example`, this guide, and any new source/test files.
4. Make sure `requirements.txt` includes dependencies actually required by the new features.
5. Compress the clean copy as something descriptive such as `E-Baladiya_ICHRAK_to_YOSSER.zip`.
6. Send the ZIP via Messenger with a brief changelog. **Never send working account passwords or real uploaded identity documents**.
7. Tell Yosser to recreate `.env`, run `migrate`, `seed_services`, and tests in a new virtual environment using Part A of this guide.
8. Because there is no Git collaboration, agree on **one latest canonical ZIP** and avoid independently modifying an older project copy.

## E3. Final handoff acceptance checklist

- [ ] Clean setup succeeds on another PC.
- [ ] Migrations and seed succeed on a new SQLite database.
- [ ] All original authentication, model and permission tests pass.
- [ ] New request/upload/verification functionality works on real DB records.
- [ ] Citizens cannot read one another's applications or documents.
- [ ] File storage remains private; invalid files are rejected.
- [ ] Corrections preserve versions and audit history.
- [ ] Processing paths correctly hand off to Yosser.
- [ ] Updated endpoints, provider API and outstanding risks are documented.
- [ ] Clean ZIP excludes secrets, databases and uploaded private files.

---

# PART F — QUICK COMMAND REFERENCE (WINDOWS POWERSHELL)

Run these commands **in sequence**, not as a single blind paste; `.env` needs to be edited between creation and migration.

```powershell
# In extracted folder containing manage.py
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env

# Generate a new secret; paste it into .env before continuing
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Once .env is configured
python manage.py migrate
python manage.py seed_services
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test core -v 2
python manage.py createsuperuser
python manage.py runserver
```

### Troubleshooting

| Symptom | Likely cause | Action |
|---|---|---|
| `No module named django` | Wrong Python environment / packages missing | Activate `.venv`; install `requirements.txt` |
| `No module named dotenv` | `python-dotenv` missing | Install it and update requirements |
| `SECRET_KEY` missing error | `.env` absent or placeholder | Create `.env` and generate a new secret |
| `No module named core` | Wrong working folder or incomplete ZIP | Open folder containing `manage.py`; check `core/` |
| Empty service catalogue | Seed not run, or view still uses placeholders | Run `seed_services`; implement C1 |
| `No such table` | Migrations not applied to local DB | Run `python manage.py migrate` |
| Cannot log in with Firas's account | `db.sqlite3` intentionally excluded | Create a new local user; never request shared passwords |
| HTTP 403 on `/administration/` for citizen | **Expected RBAC behavior** | Use an appropriately authorized employee or administrator |
| Test command finds 0 tests | Test module absent, empty or named incorrectly | Verify `core/test_*.py`, class `TestCase`, methods `test_*` |
| Login/session fails on local HTTP | HTTPS-only cookies or redirects enabled prematurely | Restore local HTTP settings; configure HTTPS later for production |

---

## First working session: recommended milestone

**Do Part A completely → read Part B → implement C1 only.** Confirm database-backed catalogue pages before starting C2. This avoids trying to debug the catalogue, application submission and file upload all at once.

**Definition of success for Ichrak:** A citizen can browse real database services, submit a correctly owned request, upload required documents securely, receive persisted verification results, correct invalid documents, and reach the correct manual/automatic next stage; Yosser can then build employee decisions and final-document processing on that foundation.

*Reference basis: `BACKEND_IMPLEMENTATION_PLAN(1).md`, `SETTINGS_SETUP.md`, original E-Baladiya frontend README, Firas's inspected Django models, and the reported final local test output (39 passing tests, 26 services, 62 document definitions).*
