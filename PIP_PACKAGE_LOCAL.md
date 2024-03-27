Para importar módulos de seu pacote omitindo o diretório `src` no caminho de importação, de modo que `src` atue como a raiz do seu pacote Python, você pode ajustar a configuração do seu ambiente de desenvolvimento e a estrutura do seu pacote. Aqui estão as etapas que você pode seguir para atingir esse objetivo:

### 1. Estrutura de Diretórios

Certifique-se de que a estrutura do seu projeto esteja organizada corretamente. A presença de um diretório `src` é uma prática recomendada para separar o código fonte do seu pacote das outras partes do projeto (como testes, documentação, etc.). Porém, para que `src` não apareça nos seus imports, você precisará garantir que o Python saiba onde encontrar os módulos do seu pacote.

```
meu_pacote/
│
├── src/
│   └── loader/
│       ├── __init__.py
│       └── datasets.py
│
├── tests/
│
├── setup.py
└── ...
```

### 2. Ajustando `setup.py`

No seu arquivo `setup.py`, assegure-se de que o argumento `package_dir` está configurado para tratar `src` como a raiz do pacote:

```python
from setuptools import setup, find_packages

setup(
    name="meu_pacote",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # Outras configurações...
)
```

Esse ajuste informa ao setuptools que os pacotes estão localizados no diretório `src`, mas não é necessário incluir `src` no caminho de importação.

### 3. Instalando o Pacote em Modo Editável

Para que as importações funcionem conforme esperado durante o desenvolvimento, instale seu pacote localmente em modo editável. Isso cria um link do seu ambiente de desenvolvimento para o pacote, permitindo que você importe módulos sem incluir `src` no caminho. Na raiz do seu projeto, execute:

```bash
pip install -e .
```

Esse comando deve ser executado no ambiente virtual onde você deseja usar o pacote.

### 4. Importando Módulos

Depois de seguir estas etapas, você pode importar módulos do seu pacote sem mencionar `src`. Por exemplo, no seu código, você pode fazer:

```python
from loader.datasets import load
print(load("bank_info.csv"))
```

### 5. Verificando o PYTHONPATH (Se Necessário)

Se você encontrar problemas, verifique se o `PYTHONPATH` está configurado corretamente para incluir a raiz do seu projeto. Isso não é normalmente necessário quando se usa `pip install -e .`, mas pode ser útil para diagnóstico.

### Resumo

Organizando a estrutura do seu projeto corretamente, ajustando o `setup.py` para tratar `src` como a raiz do pacote, e instalando seu pacote em modo editável, você pode importar módulos sem incluir `src` no caminho. Isso torna o desenvolvimento e a importação de módulos mais limpos e mais próximos de como o pacote funcionará quando for instalado por outros usuários.




Se você tem vários módulos dentro da pasta `loader` e está utilizando a configuração no seu `setup.py` como mostrado, todos os módulos dentro da pasta `loader` serão incluídos automaticamente no seu pacote quando ele for instalado. O `find_packages(where="src")`, juntamente com `package_dir={"": "src"}`, cuida disso para você, procurando por pacotes Python (diretórios que contêm um arquivo `__init__.py`) dentro do diretório especificado (`src` neste caso) e tratando-os como parte do pacote que você está definindo.

### O que acontece com múltiplos módulos?

Quando você usa `find_packages(where="src")`, o setuptools procura automaticamente por todos os diretórios dentro de `src` que contêm um arquivo `__init__.py`, tratando cada um como um pacote. Isso significa que todos os módulos (arquivos `.py`) e subpacotes (diretórios com `__init__.py`) dentro de cada pacote encontrado também serão incluídos.

Por exemplo, se sua estrutura de diretório dentro de `src` parecer com isso:

```
src/
└── loader/
    ├── __init__.py
    ├── modulo1.py
    ├── modulo2.py
    └── subpacote/
        ├── __init__.py
        └── modulo3.py
```

Todos os módulos (`modulo1.py`, `modulo2.py`, `modulo3.py`) e o subpacote (`subpacote`) serão incluídos no pacote `loader` quando ele for instalado.

### Importando Módulos e Subpacotes

Após a instalação do pacote, os módulos e subpacotes podem ser importados diretamente em seu código Python, por exemplo:

```python
from loader import modulo1, modulo2
from loader.subpacote import modulo3
```

### Notas Adicionais

- **Organização**: Manter uma estrutura clara e lógica de diretórios facilita o entendimento de como o pacote está organizado, tanto para você quanto para outros desenvolvedores que podem usar ou contribuir para o seu pacote.
- **Instalação**: Lembre-se de instalar o pacote em seu ambiente de desenvolvimento (usando `pip install -e .` para instalação editável) para testar as importações e garantir que tudo está sendo incluído como esperado.
- **Distribuição**: Quando estiver pronto para distribuir seu pacote, o processo descrito (usando `setup.py` e eventualmente publicando no PyPI) garante que quem instalar seu pacote poderá acessar todos os módulos e subpacotes que você definiu.

Essa abordagem oferece flexibilidade na organização do seu código e facilita a expansão do seu pacote adicionando mais módulos e funcionalidades no futuro.