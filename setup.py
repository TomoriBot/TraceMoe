from setuptools import find_packages, setup
import tracemoe

install_requires = [
    'requests',
]
packages = [
    'tracemoe'
]

setup(
    name="TraceMoe",
    version=tracemoe.__version__,
    description="Search screenshot of anime and reverse it!",
    author="Anysz, Soruly, Fauzanardh",
    author_email="fauzanardh@gmail.com",
    url="https://trace.moe",
    packages=packages,
    license="MIT License",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.0",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video"
    ],
)
