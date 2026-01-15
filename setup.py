from setuptools import setup, find_packages

setup(
    name="codex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['rich'],
    entry_points={
        'console_scripts': [
            'codex = codex.main:main',
        ],
    },
    author="Gemini",
    author_email="no-reply@google.com",
    description="A simple CLI tool for developers.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/turjoyce20220103002-source/codex_cli_tutorial",
)
