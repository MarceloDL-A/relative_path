from setuptools import setup, find_packages

setup(
    name="local_scripts",
    version="0.1.0",
    description="Uma breve descrição do que o pacote faz",
    author="Seu Nome",
    author_email="seuemail@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Dependências necessárias para instalar junto com seu pacote
        # Exemplo: "requests >= 2.19.1"
    ],
    classifiers=[
        # Classificadores de como o pacote pode ser encontrado
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Adicione mais opções conforme necessário
)