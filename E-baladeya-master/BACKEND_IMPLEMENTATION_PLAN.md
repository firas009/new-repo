# E-Baladiya Backend Implementation Plan

## 1. Objective

This document defines the backend work required to transform the current Django
frontend prototype into a working municipal-services platform based on the
cahier des charges and the logigramme.

The backend must support:

- Citizen registration, login, logout, and account management.
- Municipal service catalogue management.
- Service requests and their complete lifecycle.
- Secure document upload and storage.
- Automatic document verification using OCR/AI/data checks.
- Correction and re-upload loops for invalid or incomplete documents.
- Automatic document generation for eligible services.
- Municipal employee review for services requiring human intervention.
- Approval, rejection, comments, and additional-document requests.
- Email and in-platform notifications.
- Citizen request tracking.
- Employee dashboards and real analytics.
- Security, validation, auditability, testing, and deployment readiness.

The implementation is planned for one week and follows the requested order:

1. Firas
2. Ichrak
3. Yosser
4. Sarah

Each person must finish the deliverables and tests in their section before
handing the project to the next person.

---

## 2. Current Starting Point

The current project is a Django template frontend:

- Django project: `eb_web/`
- Main app: `core/`
- Routes: `core/urls.py`
- Views: `core/views.py`
- Service definitions: `core/services.py`
- Templates: `templates/`
- Static assets: `static/`
- Database configuration: SQLite in `eb_web/settings.py`
- Requirements: `requirements.txt`

The current application uses in-memory dictionaries and static HTML values.
There are no real models, forms, authentication workflows, uploads,
verification services, employee actions, notifications, or database-backed
analytics.

The existing URLs and templates should be preserved where possible so the
backend can be connected without unnecessarily redesigning the frontend.

---

## 3. Business Workflow to Implement

### Citizen workflow

1. Citizen opens the platform.
2. Citizen creates an account or logs in.
3. Citizen browses municipal services.
4. Citizen opens a service and reads eligibility, fees, processing type, and
   required documents.
5. Citizen starts a request.
6. Citizen completes the request information form.
7. Citizen uploads each required document.
8. The platform validates file type, size, security, and completeness.
9. The verification service checks the documents.
10. If documents are invalid or incomplete, the citizen receives the reasons
    and uploads corrected files.
11. If the service is automatic, the platform generates the official result.
12. If the service requires an employee, the request enters the employee queue.
13. The citizen tracks the request status and history.
14. The citizen receives the final document or rejection notification by email.

### Automatic verification workflow

The verification pipeline must support:

- File safety and extension validation.
- Document type detection.
- OCR text extraction.
- Required-field extraction, such as name, CIN, date of birth, address, and
  reference number.
- Official template/format comparison.
- Issuing-authority verification.
- Signature, reference, or identifier checks where applicable.
- Trusted database matching where an external or test data source exists.
- Cross-document consistency checks.
- Required-document completeness checks.
- A verification score and per-check result.
- Human-readable error reasons.
- A clear final result: `valid`, `invalid`, `incomplete`, or `manual_review`.

The first implementation may use a provider abstraction and a deterministic
mock verifier for local development. The interface must allow a real OCR/AI
provider to be added later without changing request logic.

### Employee workflow

1. Employee logs in.
2. Employee views requests assigned to or available for the employee.
3. Employee opens a request.
4. Employee sees citizen data, request details, uploaded documents, automatic
   verification results, and audit history.
5. Employee can request additional documents.
6. Employee can add a comment.
7. Employee approves or rejects the request.
8. On approval, the final document is generated or uploaded and delivered.
9. On rejection, the employee records a reason and the citizen is notified.

---

## 4. Recommended Technical Design

### Django components

Use Django models, forms, class-based or function-based views following the
existing project style, Django authentication, Django messages, email
backends, and management commands where useful.

Recommended app split:

- `accounts`: citizen and employee profiles, roles, authentication helpers.
- `services_app`: municipal services and required document definitions.
- `applications`: requests, statuses, timelines, comments, decisions.
- `documents`: uploaded files, storage, validation, document versions.
- `verification`: verification providers, checks, OCR results, scores.
- `notifications`: email and in-platform notifications.
- `analytics_app`: reporting queries and dashboard metrics.

If splitting into multiple apps is too risky for the one-week deadline, start
with a single `core` app but keep models and services in separate modules:

```text
core/
  models/
    user.py
    service.py
    application.py
    document.py
    verification.py
    notification.py
  services/
    application_service.py
    document_service.py
    verification_service.py
    notification_service.py
    analytics_service.py
```

### Core entities

At minimum, implement:

- `User`: Django user or custom user with email login support.
- `Profile`: phone, CIN/identity reference, address, municipality, role.
- `MunicipalService`: name, slug, category, description, eligibility, fee,
  issuing authority, processing type, active flag.
- `RequiredDocument`: service, name, description, required flag, accepted
  extensions, maximum size, ordering.
- `Application`: applicant, service, reference number, status, submitted date,
  assigned employee, decision date, rejection reason.
- `ApplicationField`: dynamic service-specific values if needed.
- `UploadedDocument`: application, required-document type, file, version,
  original name, MIME type, size, hash, status.
- `DocumentVerification`: uploaded document, provider, score, status, raw
  result reference, checked date.
- `VerificationCheck`: verification, check type, passed flag, score, message.
- `ApplicationEvent`: application, actor, event type, message, timestamp.
- `EmployeeComment`: application, employee, text, visibility, timestamp.
- `Notification`: recipient, application, type, title, body, read status.
- `GeneratedDocument`: application, file, document type, generated date,
  delivery status.

### Status values

Use controlled choices rather than arbitrary strings.

Application statuses:

- `draft`
- `documents_pending`
- `verification_pending`
- `correction_required`
- `manual_review`
- `additional_documents_required`
- `approved`
- `rejected`
- `completed`
- `cancelled`

Document statuses:

- `pending`
- `checking`
- `valid`
- `invalid`
- `replaced`

Every status transition must be validated and recorded in
`ApplicationEvent`.

---

## 5. One-Week Work Distribution

## Day 1-2: Firas - Foundation, database, authentication

### Firas responsibilities

Firas owns the backend foundation and must complete it before the other team
members begin dependent work.

### Firas tasks

#### Project and environment setup

- Confirm Django settings for development and production-like environments.
- Add required backend packages to `requirements.txt`.
- Configure environment variables for:
  - `SECRET_KEY`
  - `DEBUG`
  - `ALLOWED_HOSTS`
  - database URL/settings
  - media storage path
  - email backend
  - verification provider settings
- Add `.env.example` without real secrets.
- Configure `MEDIA_ROOT` and `MEDIA_URL`.
- Configure static files correctly.
- Add logging for application errors, security events, verification failures,
  and email failures.
- Keep secrets out of Git.

#### Database models and migrations

- Create all core models listed in Section 4.
- Add indexes for:
  - application reference number
  - applicant and status
  - service and status
  - notification recipient and read status
  - application event timestamp
- Add unique constraints where required:
  - service slug
  - request reference number
  - one active document version per required document and application
- Add model validation and useful `__str__` methods.
- Create and run migrations.
- Register models in Django admin.
- Seed the existing service catalogue into the database.
- Move required-document definitions from the Python dictionary into database
  records while preserving the existing service slugs.

#### Authentication and authorization

- Implement registration with email, password, first name, last name, and
  optional phone/CIN fields.
- Implement login and logout.
- Add password validation and secure password handling.
- Add authenticated-only protection for citizen dashboard and request routes.
- Add employee-only protection for administration routes.
- Define roles:
  - citizen
  - employee
  - administrator
- Prevent citizens from viewing other citizens' applications or documents.
- Prevent ordinary employees from changing administrative configuration.
- Add login redirect behavior and clear error messages.
- Add CSRF protection to every POST form.

#### Firas handoff requirements

- Migrations run successfully on a clean database.
- A test citizen can register and log in.
- A test employee can log in and access only employee routes.
- A citizen cannot access another citizen's request.
- Service data exists in the database.
- All model tests and authentication tests pass.
- Provide Ichrak with model names, status choices, seed instructions, and
  example test credentials stored only locally.

---

## Day 3-4: Ichrak - Request lifecycle, uploads, verification

### Ichrak responsibilities

Ichrak owns the citizen request process and the complete document/verification
pipeline built on Firas's models.

### Ichrak tasks

#### Service catalogue integration

- Replace view usage of the in-memory service list with database queries.
- Keep service catalogue search and category filtering working.
- Add service detail pages using database relations.
- Show database-backed required documents and accepted file types.
- Add active/inactive service handling.

#### Application creation

- Create a request from a selected municipal service.
- Generate a unique human-readable reference such as `REQ-2026-00001`.
- Associate the request with the authenticated citizen.
- Store service-specific form values.
- Validate eligibility and required fields.
- Prevent duplicate accidental submissions where appropriate.
- Start every request as `draft` or `documents_pending`.
- Record an `ApplicationEvent` for request creation.

#### Upload system

- Add real multipart upload forms with `POST` and CSRF tokens.
- Upload one file per required document.
- Validate:
  - required document type
  - file extension
  - MIME type
  - maximum file size
  - empty/corrupted files
  - duplicate files
- Sanitize uploaded filenames.
- Store files outside the static directory.
- Prevent executable uploads.
- Generate a file hash.
- Create document versions when a citizen replaces a file.
- Do not expose private files through predictable public URLs.
- Implement an authorized download/view endpoint.
- Display upload success, validation errors, and replacement instructions.
- Add a configurable upload size limit.

#### Verification service

- Create a provider interface such as:

```python
class VerificationProvider:
    def verify(self, document, application):
        ...
```

- Implement a local deterministic provider for development and testing.
- Add OCR/provider abstraction without hard-coding an external vendor.
- Implement checks for:
  - document type
  - required fields
  - official format
  - issuing authority
  - reference/identifier format
  - extracted identity consistency
  - cross-document consistency
  - completeness
- Store one result per check.
- Store verification score and provider metadata safely.
- Never store unnecessary sensitive raw provider data.
- Map outcomes to:
  - valid
  - invalid
  - incomplete
  - manual review
- Make failures explicit and visible to the citizen.
- Add retry handling for temporary provider failures.
- Avoid marking a document valid when verification has silently failed.

#### Correction loop

- If documents are invalid or incomplete:
  - set application status to `correction_required`
  - identify the exact document and reason
  - notify the citizen
  - allow replacement upload
  - return the application to verification
- Preserve previous document versions and verification results.
- Prevent submission while required corrections remain unresolved.

#### Automatic versus manual routing

- Read the service processing type from the database.
- Route eligible automatic services to document generation.
- Route services requiring human intervention to `manual_review`.
- Record routing decisions as application events.

#### Ichrak handoff requirements

- A citizen can create a real request for a database service.
- Required documents can be uploaded securely.
- Invalid files are rejected with clear errors.
- Verification results are persisted.
- Invalid documents trigger correction and re-upload.
- Valid automatic requests enter document generation.
- Manual-review requests appear in the employee queue.
- Ichrak provides Yosser with endpoint names, service methods, fixtures, and
  verification test scenarios.

---

## Day 5-6: Yosser - Employee operations, decisions, documents, notifications

### Yosser responsibilities

Yosser owns the employee portal and all final decision paths from the
logigramme.

### Yosser tasks

#### Employee queue

- Replace static employee dashboard values with database queries.
- Show requests by status:
  - awaiting review
  - under review
  - additional documents required
  - completed
  - rejected
- Add filtering by service, status, date, and verification outcome.
- Add pagination.
- Add assignment to an employee.
- Record assignment events.
- Prevent unauthorized employee access.

#### Employee request detail

- Display:
  - citizen information
  - service information
  - submitted fields
  - uploaded documents
  - document versions
  - verification checks
  - confidence/score
  - request timeline
  - comments
- Add authorized document preview/download.
- Show whether the request is eligible for approval.
- Show warnings when automatic verification is incomplete or failed.

#### Employee actions

- Add `start review` action.
- Add `request additional documents` action with a mandatory explanation.
- Add employee comment support.
- Add `approve` action with validation.
- Add `reject` action with mandatory reason.
- Add confirmation pages or confirmation dialogs.
- Use POST requests, CSRF, permission checks, and transaction boundaries.
- Reject invalid state transitions.
- Record every action in `ApplicationEvent`.

#### Final document generation

- Create a service for automatic result generation.
- Create a service for employee-approved final document generation.
- Generate a PDF or equivalent official document with:
  - request reference
  - citizen name
  - service name
  - issue date
  - issuing authority
  - verification/approval reference
  - document authenticity identifier
- Store generated documents securely.
- Allow the citizen to download only their own documents.
- Keep generation replaceable so official templates can evolve.
- Record generation and delivery status.

#### Rejection and approval paths

- Approval:
  - set status to `approved` or `completed` according to the service flow
  - generate or attach final document
  - create an event
  - notify the citizen
- Rejection:
  - require rejection reason
  - set status to `rejected`
  - create an event
  - notify the citizen
- Additional documents:
  - set status to `additional_documents_required`
  - store the request reason
  - notify the citizen
  - allow upload and return to verification/review

#### Notifications and email

- Implement in-platform notifications.
- Implement email templates for:
  - account registration
  - request created
  - upload received
  - verification passed
  - correction required
  - additional documents required
  - request approved
  - request rejected
  - final document available
- Add a development email backend that prints or stores emails locally.
- Add production SMTP configuration through environment variables.
- Do not expose sensitive documents in email attachments by default; send
  authenticated download links.
- Record notification delivery status and failures.

#### Yosser handoff requirements

- Employee can review a real request.
- Employee can request documents, approve, or reject.
- State transitions and permissions are enforced.
- Final documents are generated and protected.
- Notifications are sent and persisted.
- Approval, rejection, and correction paths are tested end to end.
- Provide Sarah with analytics event definitions and notification templates.

---

## Day 7: Sarah - Analytics, integration, quality, security, deployment

### Sarah responsibilities

Sarah owns final integration, operational analytics, quality assurance,
security review, documentation, and delivery readiness.

### Sarah tasks

#### Analytics

- Replace hardcoded values in `templates/analytics.html`.
- Create database-backed analytics queries for:
  - total requests
  - requests by status
  - requests by service
  - verification success rate
  - correction rate
  - rejection rate
  - average processing time
  - automatic versus manual processing
  - daily/weekly/monthly request volume
- Add date-range filtering.
- Restrict analytics to authorized employees/administrators.
- Avoid exposing personal citizen data in aggregate charts.
- Add export endpoint for CSV administrative reports.
- Validate exported data permissions and escaping.

#### Integration testing

- Create tests for the complete citizen flow:
  - register
  - login
  - browse service
  - create request
  - upload documents
  - verify documents
  - correct invalid documents
  - submit
  - track status
  - download result
- Create tests for the employee flow:
  - login
  - view queue
  - inspect application
  - request additional documents
  - approve
  - reject
  - view analytics
  - export report
- Test automatic-service routing.
- Test manual-review routing.
- Test email notification creation.
- Test unauthorized access and object-level permissions.

#### Security review

- Verify CSRF protection on every state-changing request.
- Verify authentication on protected routes.
- Verify role and object-level authorization.
- Verify secure upload validation.
- Verify private media cannot be accessed directly.
- Verify filenames and user input are escaped.
- Verify SQL queries use Django ORM safely.
- Verify secrets are environment-based.
- Verify production settings disable `DEBUG`.
- Verify secure cookies, HTTPS settings, and HSTS documentation.
- Verify rate limiting or throttling for login and upload endpoints.
- Verify audit events do not log passwords, full identity numbers, or document
  contents.
- Verify sensitive data retention and deletion behavior.
- Run dependency vulnerability checks.

#### Reliability and operations

- Add database transaction handling around approval, rejection, and generation.
- Add clear error pages and user-facing error messages.
- Add logging with correlation/request IDs where practical.
- Add health-check endpoint.
- Add backup and restore instructions for the database and media files.
- Add deployment instructions for Django, static files, media, database, and
  email.
- Add a production configuration checklist.

#### Documentation

- Update `README.md` with:
  - setup instructions
  - migrations
  - seed commands
  - test commands
  - environment variables
  - local email configuration
  - local verification provider
  - employee creation
  - deployment notes
- Document API/view behavior and status transitions.
- Document how to replace the mock verification provider with a real provider.
- Document data protection and uploaded-file handling.
- Document known limitations and future improvements.

#### Sarah final acceptance requirements

- Clean installation works from the README.
- Migrations and seed data work from an empty database.
- All targeted and integration tests pass.
- Citizen and employee workflows work end to end.
- No critical security issue remains.
- Analytics are database-backed.
- No production secrets are committed.
- Final demo scenario follows the logigramme successfully.

---

## 6. Dependency Order

The work must be performed in this order:

1. Firas creates models, migrations, roles, authentication, and seeded services.
2. Ichrak uses those models to implement requests, documents, and verification.
3. Yosser uses requests and verification results to implement employee decisions,
   final documents, and notifications.
4. Sarah integrates all modules, adds analytics, tests, security checks, and
   deployment documentation.

No person should rewrite another person's completed module without first
discussing the change with the team. Fixes that are required for integration
are allowed, but should be documented in the handoff.

---

## 7. Shared Conventions

- Use Django ORM and migrations; do not write production data into Python
  dictionaries.
- Use service-layer functions for workflow logic rather than putting complex
  business rules directly in templates.
- Use POST for all state-changing operations.
- Include CSRF tokens in every form.
- Validate all user input server-side.
- Use explicit status choices and validate transitions.
- Preserve request history through audit events.
- Never trust a client-provided user ID, application ID, role, or status.
- Never expose private uploaded files through public static URLs.
- Never silently treat verification or email failure as success.
- Keep sensitive information out of logs and email bodies.
- Add tests with each feature, not only at the end.
- Keep the existing frontend route names where practical.

---

## 8. Minimum Definition of Done

The backend is considered complete for the one-week milestone only when:

- A citizen can register and log in.
- Services and required documents come from the database.
- A citizen can create a request.
- A citizen can securely upload required documents.
- Verification produces persisted, explainable results.
- Invalid documents trigger correction and re-upload.
- Valid requests route automatically or to an employee according to service type.
- Employees can inspect, request documents, approve, and reject.
- Approved results can be generated and downloaded securely.
- Rejections and required corrections notify the citizen.
- The citizen can track the complete timeline.
- Analytics and export use real database data.
- Permissions prevent cross-user and cross-role access.
- Tests cover the main citizen and employee workflows.
- Setup, environment, security, and deployment documentation exists.

---

## 9. Risks and Scope Controls

The following items must not block the first working version:

- A real government database integration.
- A production-grade AI model.
- Advanced electronic signatures.
- Payment integration.
- Multiple municipalities with separate workflows.
- Native mobile applications.

For these items, implement clean provider interfaces, configuration points,
mock/test providers, and documented integration points. Do not fake successful
verification in production-shaped code; mock behavior must be clearly limited
to development and tests.

The one-week target should deliver a secure, testable backend foundation and a
complete demonstrable workflow using local/mock integrations where external
systems are not yet available.