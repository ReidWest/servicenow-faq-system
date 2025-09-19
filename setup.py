from setuptools import setup, find_packages

setup(
    name="servicenow-faq-system",
    version="1.0.0",
    description="A ServiceNow-themed Employee FAQ web application built with Flask",
    author="ServiceNow FAQ Team",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "Werkzeug==2.3.7",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.3",
        "itsdangerous==2.1.2",
        "click==8.1.7"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Flask",
    ],
)