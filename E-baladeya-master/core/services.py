SERVICES = [
    {
        'slug': 'birth-registration', 'name': 'Birth registration', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Declare a birth and establish the official civil status record.', 'required_documents_count': 4,
        'eligibility': 'Parent, legal guardian, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'marriage-contract', 'name': 'Marriage contract', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Prepare the civil status file for a marriage contract at the municipality.', 'required_documents_count': 6,
        'eligibility': 'Both future spouses or their authorized representatives', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'death-registration', 'name': 'Death registration', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Register a death and obtain the corresponding municipal record.', 'required_documents_count': 3,
        'eligibility': 'Relative, legal representative, or person who reported the death', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'birth-certificate-extract', 'name': 'Birth certificate extract', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Request an official extract from the civil status register.', 'required_documents_count': 2,
        'eligibility': 'The person concerned, parent, legal representative, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'marriage-certificate-extract', 'name': 'Marriage certificate extract', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Obtain an official extract of a marriage record held by the municipality.', 'required_documents_count': 2,
        'eligibility': 'One of the spouses, legal representative, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'death-certificate-extract', 'name': 'Death certificate extract', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Request an official extract of a death record.', 'required_documents_count': 2,
        'eligibility': 'Relative, legal representative, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'family-book-first-issuance', 'name': 'Family book - first issuance', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Apply for the first family book following a marriage registration.', 'required_documents_count': 5,
        'eligibility': 'One of the spouses after marriage registration', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'family-book-duplicate', 'name': 'Family book - duplicate', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Request a replacement family book when the original is lost or damaged.', 'required_documents_count': 3,
        'eligibility': 'Family book holder or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'assignment-family-name', 'name': 'Assignment of a family name', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Submit a request to assign a family name in the civil status records.', 'required_documents_count': 5,
        'eligibility': 'The person concerned, parent, or legal representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'burial-authorization', 'name': 'Burial authorization', 'category': 'Civil status', 'category_slug': 'civil-status',
        'description': 'Request authorization for burial within the municipal territory.', 'required_documents_count': 3,
        'eligibility': 'Family member, funeral representative, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Civil Status Office',
    },
    {
        'slug': 'signature-legalization', 'name': 'Signature legalization', 'category': 'Certification', 'category_slug': 'certification',
        'description': 'Legalize a signature before submitting a document to an authority.', 'required_documents_count': 2,
        'eligibility': 'The signatory in person or authorized legal representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Administration',
    },
    {
        'slug': 'copy-conformity-certification', 'name': 'Certification of conformity of copies to originals', 'category': 'Certification', 'category_slug': 'certification',
        'description': 'Have copies certified as conforming to the original documents.', 'required_documents_count': 3,
        'eligibility': 'Document holder or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Administration',
    },
    {
        'slug': 'building-permit', 'name': 'Building permit', 'category': 'Urbanism & construction', 'category_slug': 'urbanism',
        'description': 'Apply for authorization to construct, modify, or extend a building.', 'required_documents_count': 9,
        'eligibility': 'Property owner, authorized holder of rights, or appointed architect', 'fee': 'According to municipal tariff', 'issuing_authority': 'Urban Planning Department',
    },
    {
        'slug': 'subdivision-approval', 'name': 'Subdivision approval', 'category': 'Urbanism & construction', 'category_slug': 'urbanism',
        'description': 'Submit a subdivision project for municipal planning review.', 'required_documents_count': 8,
        'eligibility': 'Landowner, developer, or authorized project representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Urban Planning Department',
    },
    {
        'slug': 'municipal-land-registration-certificate', 'name': 'Certificate of registration of municipal land property', 'category': 'Urbanism & construction', 'category_slug': 'urbanism',
        'description': 'Request a certificate relating to the registration of municipal land property.', 'required_documents_count': 5,
        'eligibility': 'Property owner, rights holder, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Urban Planning Department',
    },
    {
        'slug': 'sidewalk-occupation-permit', 'name': 'Sidewalk occupation permit', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Request permission to occupy part of a sidewalk for an authorized activity.', 'required_documents_count': 5,
        'eligibility': 'Property owner, business operator, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'vehicle-access-protection-permit', 'name': 'Vehicle access protection permit', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Request protection for a vehicle entrance serving a property.', 'required_documents_count': 4,
        'eligibility': 'Property owner, tenant, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'parking-space-permit', 'name': 'Parking space permit', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Apply for a reserved parking space linked to a property or activity.', 'required_documents_count': 4,
        'eligibility': 'Property owner, business operator, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'disabled-parking-reservation', 'name': 'Disabled parking reservation', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Request a reserved parking space for a person with a disability.', 'required_documents_count': 4,
        'eligibility': 'Person with a disability, guardian, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'loading-unloading-zone-reservation', 'name': 'Loading/unloading zone reservation', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Request temporary use of a public area for loading or unloading.', 'required_documents_count': 4,
        'eligibility': 'Business owner, carrier, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'public-parking-operation-permit', 'name': 'Public parking operation permit', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Apply to operate a parking area within the municipal jurisdiction.', 'required_documents_count': 8,
        'eligibility': 'Company, public body, or authorized operator', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'pedestrian-zone-permit', 'name': 'Pedestrian-zone permit', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Request access or authorized activity in a pedestrian-only zone.', 'required_documents_count': 4,
        'eligibility': 'Resident, business operator, service provider, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'street-closure-authorization', 'name': 'Street closure authorization', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Request temporary closure of a street for works or an event.', 'required_documents_count': 5,
        'eligibility': 'Event organizer, property owner, contractor, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'street-naming-certificate', 'name': 'Street naming certificate', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Request an official certificate confirming a street name or address.', 'required_documents_count': 3,
        'eligibility': 'Property owner, resident, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Administration',
    },
    {
        'slug': 'taxi-public-transport-license', 'name': 'Taxi public transport license', 'category': 'Public space & traffic', 'category_slug': 'public-space',
        'description': 'Submit a municipal request related to operating public taxi transport.', 'required_documents_count': 7,
        'eligibility': 'Licensed taxi operator or authorized transport company', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Traffic Department',
    },
    {
        'slug': 'family-ceremony-authorization', 'name': 'Authorization for a family ceremony', 'category': 'Local authorizations', 'category_slug': 'authorizations',
        'description': 'Request authorization for a family ceremony held in a municipal area.', 'required_documents_count': 4,
        'eligibility': 'Adult organizer, venue owner, or authorized representative', 'fee': 'According to municipal tariff', 'issuing_authority': 'Municipal Administration',
    },
]

SERVICES_BY_SLUG = {service['slug']: service for service in SERVICES}

for service in SERVICES:
    service['processing_type'] = 'Instant service' if service['slug'] in {
        'birth-certificate-extract', 'marriage-certificate-extract', 'death-certificate-extract',
        'signature-legalization', 'copy-conformity-certification',
    } else 'Administrative review'

SERVICE_DETAILS = {
    'birth-registration': [
        {'label': 'Who can request', 'value': 'Parent, legal guardian, or authorized representative'},
        {'label': 'Main requirements', 'value': 'Birth declaration and identity documents; exact list to be confirmed by the Civil Status Office'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
        {'label': 'Where to apply', 'value': 'Relevant municipal civil status office'},
    ],
    'marriage-contract': [
        {'label': 'Who can request', 'value': 'Both future spouses or their authorized representatives'},
        {'label': 'Main requirements', 'value': 'Civil status documents for both spouses; exact file to be confirmed by the municipality'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
    ],
    'death-registration': [
        {'label': 'Who can request', 'value': 'Relative, legal representative, or person who reported the death'},
        {'label': 'Information required', 'value': 'Identity of the deceased, date and place of death, and supporting death document'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
        {'label': 'Where to apply', 'value': 'Municipality responsible for the civil status record'},
    ],
    'birth-certificate-extract': [
        {'label': 'Information required', 'value': 'Name, surname, date and place of birth'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
        {'label': 'Where available', 'value': 'Municipality, municipal district, or authorized administration office'},
    ],
    'marriage-certificate-extract': [
        {'label': 'Information required', 'value': 'Names of the spouses and date and place of marriage'},
        {'label': 'Who can request', 'value': 'One of the spouses or an authorized representative'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
    ],
    'death-certificate-extract': [
        {'label': 'Information required', 'value': 'Name of the deceased and date and place of death'},
        {'label': 'Who can request', 'value': 'Relative, legal representative, or authorized representative'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
    ],
    'family-book-first-issuance': [
        {'label': 'Who can request', 'value': 'Eligible Tunisian married applicant'},
        {'label': 'Main requirements', 'value': 'Marriage extract, required civil status extracts, identity documents, and photograph; exact list to be confirmed'},
        {'label': 'Processing time', 'value': 'To be confirmed by the relevant municipal office'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
    ],
    'family-book-duplicate': [
        {'label': 'Who can request', 'value': 'Family book holder or authorized representative'},
        {'label': 'Main requirements', 'value': 'Identity document and declaration or proof explaining the replacement request'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
    ],
    'assignment-family-name': [
        {'label': 'Who can request', 'value': 'Person concerned, parent, or legal representative'},
        {'label': 'Conditions', 'value': 'Subject to the applicable civil status rules and review by the competent office'},
        {'label': 'Main requirements', 'value': 'Civil status records and supporting identity or family documents; exact list to be confirmed'},
        {'label': 'Issued by', 'value': 'Municipal Civil Status Office'},
    ],
    'burial-authorization': [
        {'label': 'Who can request', 'value': 'Family member, funeral representative, or authorized representative'},
        {'label': 'Main requirements', 'value': 'Death-related supporting document and identity information; exact list to be confirmed'},
        {'label': 'Where to apply', 'value': 'Municipal office responsible for the burial location'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
    ],
    'signature-legalization': [
        {'label': 'Who can request', 'value': 'The signatory in person or authorized legal representative'},
        {'label': 'Required documents', 'value': 'Identity document and the document to be signed or legalized'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Administration'},
    ],
    'copy-conformity-certification': [
        {'label': 'Who can request', 'value': 'Document holder or authorized representative'},
        {'label': 'Required documents', 'value': 'Original document, copies to certify, and identity document'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Where to apply', 'value': 'Municipal administration or authorized office'},
    ],
    'building-permit': [
        {'label': 'Who can request', 'value': 'Property owner, rights holder, or appointed architect'},
        {'label': 'Main requirements', 'value': 'Property information, plans, and technical file; exact documents depend on the project'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Urban Planning Department'},
    ],
    'subdivision-approval': [
        {'label': 'Who can request', 'value': 'Landowner, developer, or authorized project representative'},
        {'label': 'Main requirements', 'value': 'Land title information, subdivision plans, and technical file'},
        {'label': 'Processing time', 'value': 'To be confirmed by the relevant municipal office'},
        {'label': 'Issued by', 'value': 'Urban Planning Department'},
    ],
    'municipal-land-registration-certificate': [
        {'label': 'Who can request', 'value': 'Property owner, rights holder, or authorized representative'},
        {'label': 'Required information', 'value': 'Property reference, location, and supporting ownership information'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Urban Planning Department'},
    ],
    'sidewalk-occupation-permit': [
        {'label': 'Who can request', 'value': 'Property owner, business operator, or authorized representative'},
        {'label': 'Main requirements', 'value': 'Location, surface or area requested, purpose, and duration of occupation'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'vehicle-access-protection-permit': [
        {'label': 'Who can request', 'value': 'Property owner, tenant, or authorized representative'},
        {'label': 'Required information', 'value': 'Property address, vehicle entrance location, and reason for protection'},
        {'label': 'Conditions', 'value': 'Subject to an assessment of access, circulation, and public-space constraints'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'parking-space-permit': [
        {'label': 'Who can request', 'value': 'Property owner, business operator, or authorized representative'},
        {'label': 'Main requirements', 'value': 'Address, justification, vehicle information, and requested location'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'disabled-parking-reservation': [
        {'label': 'Who can request', 'value': 'Person with a disability, guardian, or authorized representative'},
        {'label': 'Required information', 'value': 'Identity, address, vehicle information, and supporting disability documentation'},
        {'label': 'Conditions', 'value': 'Subject to municipal review of the location and supporting documentation'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'loading-unloading-zone-reservation': [
        {'label': 'Who can request', 'value': 'Business owner, carrier, or authorized representative'},
        {'label': 'Main requirements', 'value': 'Address, requested dates and times, activity, and vehicle information'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'public-parking-operation-permit': [
        {'label': 'Who can request', 'value': 'Company, public body, or authorized operator'},
        {'label': 'Main requirements', 'value': 'Operator information, site details, operating plan, and technical file'},
        {'label': 'Processing time', 'value': 'To be confirmed by the relevant municipal office'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'pedestrian-zone-permit': [
        {'label': 'Who can request', 'value': 'Resident, business operator, service provider, or authorized representative'},
        {'label': 'Required information', 'value': 'Purpose, access dates and times, location, and vehicle information where relevant'},
        {'label': 'Conditions', 'value': 'Access must remain compatible with pedestrian safety and municipal rules'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'street-closure-authorization': [
        {'label': 'Who can request', 'value': 'Event organizer, property owner, contractor, or authorized representative'},
        {'label': 'Main requirements', 'value': 'Location, reason, dates, traffic plan, and contact information'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'street-naming-certificate': [
        {'label': 'Who can request', 'value': 'Property owner, resident, or authorized representative'},
        {'label': 'Required information', 'value': 'Property address and the street or address reference concerned'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Administration'},
    ],
    'taxi-public-transport-license': [
        {'label': 'Who can request', 'value': 'Licensed taxi operator or authorized transport company'},
        {'label': 'Main requirements', 'value': 'Operator, vehicle, insurance, and professional authorization information'},
        {'label': 'Processing time', 'value': 'To be confirmed by the relevant municipal office'},
        {'label': 'Issued by', 'value': 'Municipal Traffic Department'},
    ],
    'family-ceremony-authorization': [
        {'label': 'Who can request', 'value': 'Adult organizer, venue owner, or authorized representative'},
        {'label': 'Main requirements', 'value': 'Venue, date, time, purpose, and organizer contact information'},
        {'label': 'Fee', 'value': 'According to municipal tariff'},
        {'label': 'Issued by', 'value': 'Municipal Administration'},
    ],
}

for service in SERVICES:
    service['details'] = SERVICE_DETAILS[service['slug']]

REQUIRED_DOCUMENTS = {
    'birth-registration': [
        {'name': 'Birth declaration', 'description': 'Official declaration relating to the birth.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Parent identity document', 'description': 'Identity document for the declaring parent.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'marriage-contract': [
        {'name': 'National identity documents', 'description': 'Identity documents for both future spouses.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Civil status extracts', 'description': 'Required civil status extracts for the marriage file.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Supporting marriage documents', 'description': 'Additional documents requested by the Civil Status Office.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'death-registration': [
        {'name': 'Death declaration or certificate', 'description': 'Official document recording the death.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Deceased person identity information', 'description': 'Identity document or civil status information for the deceased.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'birth-certificate-extract': [
        {'name': 'Identity document', 'description': 'Identity document of the person concerned or requester.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Civil status reference', 'description': 'Name, date, and place of birth or existing record reference.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'marriage-certificate-extract': [
        {'name': 'Identity document', 'description': 'Identity document of a spouse or authorized requester.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Marriage record information', 'description': 'Names and date or place of the marriage record.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'death-certificate-extract': [
        {'name': 'Requester identity document', 'description': 'Identity document of the requester.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Death record information', 'description': 'Name and date or place of the death record.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'family-book-first-issuance': [
        {'name': 'Marriage extract', 'description': 'Extract relating to the marriage registration.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Civil status extracts', 'description': 'Required extracts for the spouses and family record.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Identity documents and photograph', 'description': 'Identity documents and photograph requested for the family book.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'family-book-duplicate': [
        {'name': 'Identity document', 'description': 'Identity document of the family book holder.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Replacement explanation', 'description': 'Declaration or supporting information for the duplicate request.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'assignment-family-name': [
        {'name': 'Identity and civil status documents', 'description': 'Documents establishing the identity and civil status record concerned.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Supporting family documents', 'description': 'Supporting documents required for examination of the request.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'burial-authorization': [
        {'name': 'Death-related document', 'description': 'Document supporting the burial request.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Requester identity document', 'description': 'Identity document of the family member or representative.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'signature-legalization': [
        {'name': 'Identity document', 'description': 'Identity document of the person signing.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Document to legalize', 'description': 'Document bearing the signature to be legalized.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'copy-conformity-certification': [
        {'name': 'Original document', 'description': 'Original document presented for comparison.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Copy to certify', 'description': 'Copy or copies requested for certification.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Identity document', 'description': 'Identity document of the requester.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'building-permit': [
        {'name': 'Proof of property or right to build', 'description': 'Property reference or document establishing the applicant\'s right.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Architectural plans', 'description': 'Plans and technical documents for the proposed work.', 'required': True, 'accepted_file_types': 'PDF'},
        {'name': 'Application and technical file', 'description': 'Application file required by the Urban Planning Department.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'subdivision-approval': [
        {'name': 'Land ownership information', 'description': 'Documents identifying the land and the applicant\'s rights.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Subdivision plans', 'description': 'Plans and technical file for the subdivision project.', 'required': True, 'accepted_file_types': 'PDF'},
        {'name': 'Project application', 'description': 'Application submitted to the Urban Planning Department.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'municipal-land-registration-certificate': [
        {'name': 'Property reference', 'description': 'Location and identifying information for the municipal land property.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Ownership or rights information', 'description': 'Supporting information relating to the applicant or property rights.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'sidewalk-occupation-permit': [
        {'name': 'Location and occupation plan', 'description': 'Location, area, and layout of the requested occupation.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Activity authorization information', 'description': 'Purpose, duration, and applicant information.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'vehicle-access-protection-permit': [
        {'name': 'Property address', 'description': 'Address and location of the vehicle entrance.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Applicant identity or business document', 'description': 'Document establishing the applicant and connection to the property.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'parking-space-permit': [
        {'name': 'Address and justification', 'description': 'Property address and reason for the requested space.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Vehicle information', 'description': 'Vehicle and applicant information relevant to the request.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'disabled-parking-reservation': [
        {'name': 'Identity document', 'description': 'Identity document of the person concerned or representative.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Disability supporting document', 'description': 'Supporting disability documentation required for review.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Address and vehicle information', 'description': 'Address and vehicle details for the requested reservation.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'loading-unloading-zone-reservation': [
        {'name': 'Business or activity information', 'description': 'Information about the activity requiring access.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Location and schedule', 'description': 'Requested location, dates, and times.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Vehicle information', 'description': 'Vehicle information for the loading or unloading operation.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'public-parking-operation-permit': [
        {'name': 'Operator information', 'description': 'Legal and contact information for the operator.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Site and operating plan', 'description': 'Location, layout, and proposed operating arrangements.', 'required': True, 'accepted_file_types': 'PDF'},
        {'name': 'Technical and administrative file', 'description': 'Additional file requested by the Municipal Traffic Department.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'pedestrian-zone-permit': [
        {'name': 'Purpose and access request', 'description': 'Reason, location, dates, and times for the requested access.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Applicant identity or business document', 'description': 'Document establishing the applicant or activity.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'street-closure-authorization': [
        {'name': 'Closure plan', 'description': 'Street location, dates, times, and proposed traffic arrangements.', 'required': True, 'accepted_file_types': 'PDF'},
        {'name': 'Purpose and organizer information', 'description': 'Reason for closure and responsible person or organization.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Supporting authorization documents', 'description': 'Additional documents requested for the specific closure.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'street-naming-certificate': [
        {'name': 'Property address information', 'description': 'Address and location concerned by the certificate.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Applicant identity document', 'description': 'Identity document of the owner, resident, or representative.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'taxi-public-transport-license': [
        {'name': 'Operator authorization information', 'description': 'Professional and operator information for the transport activity.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Vehicle documents', 'description': 'Vehicle, insurance, and registration documents where applicable.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Professional file', 'description': 'Additional file requested by the Municipal Traffic Department.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
    'family-ceremony-authorization': [
        {'name': 'Organizer identity document', 'description': 'Identity document of the adult organizer or representative.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
        {'name': 'Venue and ceremony information', 'description': 'Venue, date, time, purpose, and contact information.', 'required': True, 'accepted_file_types': 'PDF, JPG, PNG'},
    ],
}

for service in SERVICES:
    service['required_documents'] = REQUIRED_DOCUMENTS[service['slug']]
    service['required_documents_count'] = len(service['required_documents'])

SUMMARY_DETAILS = {
    'birth-registration': [('Applicant', 'Parent / legal representative'), ('Responsible office', 'Civil Status Office'), ('Application location', 'Relevant municipality')],
    'marriage-contract': [('Applicant', 'Future spouses'), ('Responsible office', 'Civil Status Office'), ('Application location', 'Relevant municipality')],
    'death-registration': [('Applicant', 'Family member / representative'), ('Responsible office', 'Civil Status Office'), ('Application location', 'Relevant municipality')],
    'birth-certificate-extract': [('Applicant', 'Person concerned / representative'), ('Issued by', 'Civil Status Office'), ('Available at', 'Municipality / authorized office')],
    'marriage-certificate-extract': [('Applicant', 'Spouse / representative'), ('Issued by', 'Civil Status Office'), ('Available at', 'Municipality / authorized office')],
    'death-certificate-extract': [('Applicant', 'Relative / representative'), ('Issued by', 'Civil Status Office'), ('Available at', 'Municipality / authorized office')],
    'family-book-first-issuance': [('Applicant', 'Married applicant'), ('Responsible office', 'Civil Status Office'), ('Application location', 'Relevant municipality')],
    'family-book-duplicate': [('Applicant', 'Family book holder'), ('Responsible office', 'Civil Status Office'), ('Application location', 'Relevant municipality')],
    'assignment-family-name': [('Applicant', 'Person concerned / representative'), ('Responsible office', 'Civil Status Office'), ('Application location', 'Relevant municipality')],
    'burial-authorization': [('Applicant', 'Family member / representative'), ('Responsible office', 'Civil Status Office'), ('Application location', 'Burial municipality')],
    'signature-legalization': [('Applicant', 'Signatory'), ('Responsible office', 'Municipal Administration'), ('Application location', 'Municipal office')],
    'copy-conformity-certification': [('Applicant', 'Document holder / representative'), ('Responsible office', 'Municipal Administration'), ('Application location', 'Municipal office')],
    'building-permit': [('Applicant', 'Owner / authorized architect'), ('Responsible office', 'Urban Planning Department'), ('Application location', 'Relevant municipality')],
    'subdivision-approval': [('Applicant', 'Landowner / developer'), ('Responsible office', 'Urban Planning Department'), ('Application location', 'Relevant municipality')],
    'municipal-land-registration-certificate': [('Applicant', 'Owner / rights holder'), ('Responsible office', 'Urban Planning Department'), ('Application location', 'Relevant municipality')],
    'sidewalk-occupation-permit': [('Applicant', 'Owner / business operator'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'vehicle-access-protection-permit': [('Applicant', 'Owner / tenant'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'parking-space-permit': [('Applicant', 'Owner / business operator'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'disabled-parking-reservation': [('Applicant', 'Person concerned / representative'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'loading-unloading-zone-reservation': [('Applicant', 'Business owner / carrier'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'public-parking-operation-permit': [('Applicant', 'Company / authorized operator'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'pedestrian-zone-permit': [('Applicant', 'Resident / business operator'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'street-closure-authorization': [('Applicant', 'Organizer / contractor'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'street-naming-certificate': [('Applicant', 'Owner / resident'), ('Issued by', 'Municipal Administration'), ('Available at', 'Relevant municipality')],
    'taxi-public-transport-license': [('Applicant', 'Taxi operator / company'), ('Responsible office', 'Municipal Traffic Department'), ('Application location', 'Relevant municipality')],
    'family-ceremony-authorization': [('Applicant', 'Adult organizer'), ('Responsible office', 'Municipal Administration'), ('Application location', 'Relevant municipality')],
}

for service in SERVICES:
    service['summary_details'] = [{'label': label, 'value': value} for label, value in SUMMARY_DETAILS[service['slug']]]

DELIVERY_BY_SERVICE = {
    'birth-registration': 'Physical collection',
    'marriage-contract': 'Physical collection',
    'death-registration': 'Physical collection',
    'birth-certificate-extract': 'Available online',
    'marriage-certificate-extract': 'Available online',
    'death-certificate-extract': 'Available online',
    'family-book-first-issuance': 'Physical collection',
    'family-book-duplicate': 'Physical collection',
    'assignment-family-name': 'Physical collection',
    'burial-authorization': 'Physical collection',
    'signature-legalization': 'Physical collection',
    'copy-conformity-certification': 'Physical collection',
    'building-permit': 'Physical collection',
    'subdivision-approval': 'Physical collection',
    'municipal-land-registration-certificate': 'Physical collection',
    'sidewalk-occupation-permit': 'Physical collection',
    'vehicle-access-protection-permit': 'Physical collection',
    'parking-space-permit': 'Physical collection',
    'disabled-parking-reservation': 'Physical collection',
    'loading-unloading-zone-reservation': 'Physical collection',
    'public-parking-operation-permit': 'Physical collection',
    'pedestrian-zone-permit': 'Physical collection',
    'street-closure-authorization': 'Physical collection',
    'street-naming-certificate': 'Available online',
    'taxi-public-transport-license': 'Physical collection',
    'family-ceremony-authorization': 'Sent by email',
}

PROCESSING_BY_SERVICE = {
    'birth-certificate-extract': 'After verification',
    'marriage-certificate-extract': 'After verification',
    'death-certificate-extract': 'After verification',
    'signature-legalization': 'At municipal office',
    'copy-conformity-certification': 'At municipal office',
}

for service in SERVICES:
    summary = [detail for detail in service['summary_details'] if detail['label'] not in {'Application location', 'Available at'}]
    summary.append({'label': 'Delivery', 'value': DELIVERY_BY_SERVICE[service['slug']]})
    summary.append({'label': 'Processing', 'value': PROCESSING_BY_SERVICE.get(service['slug'], 'Administrative review required')})
    service['summary_details'] = summary
