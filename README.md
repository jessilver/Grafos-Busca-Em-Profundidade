# Projeto de Grafos em Python

Este projeto é uma implementação de algoritmos de grafos em Python.

## Configuração do Ambiente Virtual

Para configurar o ambiente virtual, siga os passos abaixo:

### Criar o Ambiente Virtual

```bash
python -m venv venv
```

### Ativar o Ambiente Virtual

No Windows:

```bash
.\venv\Scripts\activate
```

No macOS/Linux:

```bash
source venv/bin/activate
```

### Instalar Bibliotecas Necessárias

1. **Instalar as dependências do Python**:
   - Ative o ambiente virtual:
     - No Windows:
       ```sh
       .\venv\Scripts\activate
       ```
     - No macOS/Linux:
       ```sh
       source venv/bin/activate
       ```
   - Instale as dependências:
     ```sh
     pip install -r requirements.txt
     ```

### Gerar Executável (.exe) do Projeto

Para gerar um executável (.exe) do projeto, você pode usar a biblioteca `pyinstaller`. Siga os passos abaixo:

1. Dentro da pasta `app`:

    ```sh
    cd app
    ```

2. Gere o executável:

    ```sh
    pyinstaller --onefile --add-data "imports;imports" main.py
    ```

2. O executável será gerado na pasta `dist`.