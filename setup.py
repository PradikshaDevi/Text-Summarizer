import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
        name="text_summarizer",
        version="0.0.0",
        author="Pradiksha",
        author_email="pradiksha2790@gmail.com",
        description="A small python package for NLP app",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/PradikshaDevi/Text-Summarizer",
        project_urls={
            "Bug Tracker": "https://github.com/PradikshaDevi/Text-Summarizer/issues"
        },
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src")
    )