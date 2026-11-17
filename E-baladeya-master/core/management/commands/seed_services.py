
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core.models import MunicipalService, RequiredDocument
from core.services import SERVICES, REQUIRED_DOCUMENTS


class Command(BaseCommand):

    help = "Seed the E-Baladiya municipal service catalogue"

    @transaction.atomic
    def handle(self, *args, **options):

        service_slugs = [service["slug"] for service in SERVICES]

        if len(service_slugs) != len(set(service_slugs)):
            raise CommandError("Duplicate service slugs in source data.")

        if set(service_slugs) != set(REQUIRED_DOCUMENTS):
            raise CommandError(
                "Service and required-document definitions do not match."
            )

        for data in SERVICES:

            source_type = data["processing_type"]

            if source_type == "Instant service":
                processing_type = (
                    MunicipalService.ProcessingType.AUTOMATIC
                )
            elif source_type == "Administrative review":
                processing_type = (
                    MunicipalService.ProcessingType.MANUAL_REVIEW
                )
            else:
                raise CommandError(
                    f"Unknown processing type: {source_type}"
                )

            service, created = MunicipalService.objects.update_or_create(
                slug=data["slug"],
                defaults={
                    "name": data["name"],
                    "category": data["category"],
                    "category_slug": data["category_slug"],
                    "description": data["description"],
                    "eligibility": data["eligibility"],
                    "fee": data["fee"],
                    "issuing_authority": data["issuing_authority"],
                    "processing_type": processing_type,
                    "summary_details": data["summary_details"],
                },
            )

            documents = REQUIRED_DOCUMENTS[data["slug"]]

            document_names = [doc["name"] for doc in documents]

            if len(document_names) != len(set(document_names)):
                raise CommandError(
                    f"Duplicate document names for {data['slug']}"
                )

            for position, document in enumerate(documents, start=1):

                RequiredDocument.objects.update_or_create(
                    service=service,
                    name=document["name"],
                    defaults={
                        "description": document["description"],
                        "required": document["required"],
                        "accepted_file_types": document[
                            "accepted_file_types"
                        ],
                        "position": position,
                    },
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Municipal catalogue seeded successfully."
            )
        )

        self.stdout.write(
            f"Total services: {MunicipalService.objects.count()}"
        )

        self.stdout.write(
            f"Total required documents: "
            f"{RequiredDocument.objects.count()}"
        )
