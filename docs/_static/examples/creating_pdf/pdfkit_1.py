# Required imports
from faker import Faker
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pdf_file.generators.pdfkit_generator import (
    PdfkitPdfGenerator,
)

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(PdfFileProvider)  # Register PdfFileProvider

# Generate PDF file using `pdfkit`
pdf_file = FAKER.pdf_file(pdf_generator_cls=PdfkitPdfGenerator)
