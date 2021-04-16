import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dpy-peper",
    version="1.0.0",
    author="sevenc-nanashi",
    author_email="sevenc-nanashi@sevenbot.jp",
    description="Helper of discord.py's on_voice_state_update",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sevenc-nanashi/dpy_voice_helper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "discord.py > 1.0.0 < 2.0.0",
    ],
)
