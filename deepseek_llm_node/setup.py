from setuptools import setup, find_packages

setup(
    name="deepseek_llm_node",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
) 