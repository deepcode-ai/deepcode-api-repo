from setuptools import setup, find_packages

setup(
    name="deepcode-api",  # Replace with your desired package name
    version="0.1.0",  # Initial version of the package
    description="A FastAPI project to handle codebase analysis with DeepCode integration",
    long_description=open('README.md').read(),  # Read the README.md for long description
    long_description_content_type="text/markdown",  # Ensures the README is interpreted as Markdown
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    url="https://github.com/deepcode-ai/deepcode-api-repo",  # Replace with the project URL
    packages=find_packages(where="api"),  # Automatically find all packages under the `api` directory
    include_package_data=True,
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn[gunicorn]>=0.18.0",
        "pydantic>=1.9.0",
        "python-dotenv>=0.19.0",
        "jwt>=3.2.1",
        "requests>=2.26.0",
        "pytest>=6.2.5",
        # Add any additional dependencies here
    ],
    extras_require={
        "dev": [
            "black",  # For code formatting
            "isort",  # For sorting imports
            "flake8",  # For linting
            "pytest-cov",  # For code coverage
        ],
        "docs": [
            "sphinx",  # For generating documentation
            "sphinx-rtd-theme",  # For theme
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",  # You can add more specific versions
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # You can adjust the minimum Python version as needed
    entry_points={
        "console_scripts": [
            "deepcode-api=api.main:app",  # Command-line entry point
        ],
    },
)
