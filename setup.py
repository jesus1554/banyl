from setuptools import setup

setup(
    name="banyl",
    version="0.5",
    description="An easy-to-use tool to complete all the tags in your music catalog",
    author="Jesús Flores Espinoza",
    author_email='jesus.flores.esp@gmail.com',
    license="MIT",
    url="https://github.com/jesus1554/banyl",
    packages=["packages"],
    include_package_data=True,
    install_requires=[
        "requests",
        "eyed3",
        "wget",
        "termcolor"
    ],
    entry_points={"console_scripts": ["banyl=reader.__main__:main"]}
)
