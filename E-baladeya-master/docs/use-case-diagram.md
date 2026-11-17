# E-Baladiya Use Case Diagram

This diagram describes the use cases represented by the current E-Baladiya
frontend. It covers the two primary actors: citizens using municipal services
and municipal employees reviewing requests.

The standalone PlantUML source is available in
[use-case-diagram.puml](./use-case-diagram.puml).

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam shadowing false
skinparam actorStyle awesome
skinparam linetype ortho

actor Citizen
actor "Municipal Employee" as Employee

rectangle "E-Baladiya" {
  package "Citizen services" {
    usecase "Browse municipal services" as UC_Browse
    usecase "Search and filter services" as UC_Search
    usecase "View service requirements" as UC_Requirements
    usecase "Create account" as UC_Register
    usecase "Log in" as UC_Login
    usecase "Start a service request" as UC_Start
    usecase "Upload supporting documents" as UC_Upload
    usecase "Check document verification" as UC_Verify
    usecase "Track request status" as UC_Track
    usecase "Fix missing or invalid documents" as UC_Fix
    usecase "Receive the administrative result" as UC_Result
  }

  package "Municipal administration" {
    usecase "View requests needing attention" as UC_Queue
    usecase "Open an application" as UC_Open
    usecase "Inspect citizen documents" as UC_Inspect
    usecase "Review automatic verification" as UC_AutoReview
    usecase "Request additional documents" as UC_RequestDocs
    usecase "Approve an application" as UC_Approve
    usecase "View service analytics" as UC_Analytics
    usecase "Export an administrative report" as UC_Export
  }

  UC_Start .> UC_Requirements : <<include>>
  UC_Start .> UC_Upload : <<include>>
  UC_Upload .> UC_Verify : <<include>>
  UC_Fix .> UC_Track : <<extend>>

  UC_Open .> UC_Inspect : <<include>>
  UC_Open .> UC_AutoReview : <<include>>
  UC_RequestDocs .> UC_Open : <<extend>>
  UC_Approve .> UC_Open : <<extend>>
  UC_Export .> UC_Analytics : <<extend>>
}

Citizen --> UC_Browse
Citizen --> UC_Search
Citizen --> UC_Requirements
Citizen --> UC_Register
Citizen --> UC_Login
Citizen --> UC_Start
Citizen --> UC_Track
Citizen --> UC_Fix
Citizen --> UC_Result

Employee --> UC_Login
Employee --> UC_Queue
Employee --> UC_Open
Employee --> UC_RequestDocs
Employee --> UC_Approve
Employee --> UC_Analytics
Employee --> UC_Export

note "Authentication is required before starting a request or using administration features." as AuthNote
AuthNote .. UC_Start
AuthNote .. UC_Queue
@enduml
```

## Actor responsibilities

| Actor | Responsibilities represented in the current application |
|---|---|
| Citizen | Discover a municipal service, understand its requirements, create or access an account, submit documents, follow verification, track requests, and correct document issues. |
| Municipal Employee | Monitor the review queue, inspect applications and documents, assess automatic verification results, request more information, approve applications, and consult operational analytics. |

## Main citizen scenario

1. The citizen browses or searches the service catalogue.
2. The citizen opens a service and reviews eligibility, fees, issuing authority, and required documents.
3. The citizen logs in or creates an account.
4. The citizen starts a request and uploads the required supporting documents.
5. E-Baladiya checks the documents and displays the verification state.
6. The citizen tracks the request timeline.
7. If a document issue is found, the citizen uploads a correction.
8. The citizen receives the completed administrative result.

## Main employee scenario

1. The municipal employee logs in to the administration portal.
2. The employee views requests awaiting review or requiring attention.
3. The employee opens an application and inspects the citizen information and uploaded documents.
4. The employee reviews automatic checks such as authenticity, template matching, trusted issuer, and database matching.
5. The employee either requests additional documents or approves the application.
6. The employee uses analytics to monitor request volume, verification success, and processing time.
7. The employee can export an administrative report.

## Current implementation status

The diagram captures the intended behavior visible in the existing frontend.
The current project is a Django template prototype: routes render pages and
service data is stored in Python dictionaries, but authentication, persistence,
file uploads, verification, employee actions, notifications, and report
exporting are not yet connected to backend workflows.
