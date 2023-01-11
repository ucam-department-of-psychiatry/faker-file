import os

from setuptools import find_packages, setup

version = "0.10.6"

try:
    readme = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()
except OSError:
    readme = ""

dependency_links = []

# Dependencies
install_requires = [
    "Faker",
]

tests_require = [
    "factory_boy",
    "parametrize",
    "pytest",
    "pytest-cov",
    "pytest-django",
    "pytest-pythonpath",
    "pytest-ordering",
    "coverage",
]

extras_require = {
    "all": [
        "Faker",  # core
        "imgkit",  # images
        "odfpy",  # ods
        "openpyxl",  # xlsx
        "pathy[all]",  # remote storages: azure, gcs, s3
        "pdfkit",  # pdf
        "python-docx",  # docx
        "python-pptx",  # pptx
        "tablib",  # ods, xlsx
        "xml2epub",  # epub
        "gtts",  # mp3
        "edge-tts",  # mp3
        "nlpaug",  # data-augmentation
        "torch",  # data-augmentation
        "transformers",  # data-augmentation
        "tika",  # data-augmentation
    ],
    "azure": ["pathy[azure]"],
    "django": ["Django>=2.2"],
    "docx": ["python-docx"],
    "epub": ["xml2epub"],
    "gcs": ["pathy[gcs]"],
    "images": ["imgkit"],
    "mp3": ["gtts", "edge-tts"],
    "mp3-edge-tts": ["edge-tts"],
    "mp3-gtts": ["gtts"],
    "ods": ["tablib", "odfpy"],
    "pdf": ["pdfkit"],
    "pptx": ["python-pptx"],
    "s3": ["pathy[s3]"],
    "sqlalchemy": ["SQLAlchemy>=1.0", "SQLAlchemy-Utils>=0.37.0"],
    "xlsx": ["tablib", "openpyxl"],
    "data-augmentation": ["nlpaug", "torch", "transformers", "tika"],
}

setup(
    name="faker-file",
    version=version,
    description="Generate files with fake data.",
    long_description=f"{readme}",
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/barseghyanartur/faker-file/issues",
        "Documentation": "https://faker-file.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/faker-file",
        "Changelog": "https://faker-file.readthedocs.io/"
        "en/latest/changelog.html",
    },
    keywords=(
        ", ".join(
            [
                "factories",
                "fake file",
                "fake files",
                "fake-file-generator",
                "fake-files-generator",
                "faker",
                "faker-file",
                "file-generator",
                "files",
                "files-generator",
                "test file",
                "test files",
                "test-file-generator",
                "test-files-generator",
                "testing",
            ]
        )
    ),
    author="Artur Barseghyan",
    author_email="artur.barseghyan@gmail.com",
    url="https://github.com/barseghyanartur/faker-file/",
    package_dir={"": "src"},
    packages=find_packages(where="./src"),
    license="MIT",
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    dependency_links=dependency_links,
    include_package_data=True,
)
