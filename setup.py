from setuptools import setup
import json


with open("metadata.json", encoding="utf-8") as fp:
    metadata = json.load(fp)


setup(
    name="lexibank_deepadungpalaung",
    version="1.0",
    description=metadata["title"],
    license=metadata.get("license", ""),
    url=metadata.get("url", ""),
    py_modules=["lexibank_deepadungpalaung"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["deepadungpalaung=lexibank_deepadungpalaung:Dataset"]},
    install_requires=["pylexibank>=3", "pyedictor>=0.1.2"],
    extras_require={"test": ["pytest-cldf"]},
)
