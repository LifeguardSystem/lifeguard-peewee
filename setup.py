from setuptools import find_packages, setup

setup(
    name="lifeguard-peewee",
    version="0.0.2",
    url="https://github.com/LifeguardSystem/lifeguard-peewee",
    author="Diego Rubin",
    author_email="contact@diegorubin.dev",
    license="GPL2",
    scripts=[],
    include_package_data=True,
    description="Lifeguard integration with SQL servers using peewee",
    install_requires=["lifeguard", "peewee"],
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages(),
)
