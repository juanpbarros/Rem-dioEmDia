# 💊 Remédio em Dia

> Aplicação em Python desenvolvida para auxiliar no controle de medicamentos de idosos, cuidadores e familiares, promovendo mais organização, segurança e acompanhamento da rotina medicamentosa.

## 🌐 Acesso online

A versão web da aplicação está disponível em:

**👉 https://juanpbarros.pythonanywhere.com**

## ⬇️ Download da aplicação

A aplicação também pode ser utilizada por meio da versão executável para Windows:

* [Baixar Remédio em Dia (.zip)](https://github.com/juanpbarros/Rem-dioEmDia/releases/download/v1.0.1/RemedioEmDia.zip)
* [Ver página da release v1.0.1](https://github.com/juanpbarros/Rem-dioEmDia/releases/tag/v1.0.1)

---

## 📌 Sobre o projeto

O **Remédio em Dia** é uma aplicação desenvolvida com o objetivo de auxiliar no controle da administração de medicamentos, especialmente para **idosos**, **cuidadores** e **familiares** que necessitam acompanhar horários e doses de forma mais organizada.

A proposta do projeto é oferecer uma solução simples, prática e funcional para reduzir esquecimentos, melhorar o acompanhamento da rotina medicamentosa e facilitar o controle diário dos medicamentos utilizados.

Este projeto foi desenvolvido como parte de uma atividade prática de BootCamp, com foco não apenas na implementação da aplicação, mas também na adoção de práticas importantes do desenvolvimento de software moderno, como:

* versionamento com Git e GitHub;
* testes automatizados;
* análise estática de código;
* integração contínua (CI);
* documentação técnica;
* organização e reprodutibilidade do projeto.

---

## 🎯 Problema real abordado

Muitas pessoas, especialmente idosos, fazem uso contínuo de medicamentos em horários diferentes ao longo do dia. Em muitos casos, esse controle é feito de maneira manual, informal ou até mesmo apenas de memória, o que pode gerar problemas como:

* esquecimento de doses;
* administração incorreta de horários;
* dificuldade de acompanhamento por cuidadores e familiares;
* falhas no tratamento.

Diante desse cenário, o **Remédio em Dia** busca oferecer uma solução simples para organizar e acompanhar esse processo.

---

## 💡 Funcionalidades da versão atual

A aplicação atualmente oferece as seguintes funcionalidades:

* ✅ Cadastrar medicamento
* ✅ Informar dosagem
* ✅ Definir horários de uso
* ✅ Listar medicamentos cadastrados
* ✅ Marcar doses como tomadas
* ✅ Escolher manualmente qual horário da dose foi tomado
* ✅ Remover medicamentos
* ✅ Identificador único (UUID) para cada medicamento
* ✅ Ordenação automática por horário
* ✅ Persistência local em arquivo JSON
* ✅ Interface **CLI** (linha de comando)
* ✅ Interface **Web** (Flask)
* ✅ Integração com API pública REST (timeapi.io) para data/hora
* ✅ Fallback local automático caso a API esteja indisponível

---

## 🛠️ Tecnologias utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias e ferramentas:

* **Python 3.14**
* **Flask** → interface web
* **Pytest** → testes automatizados
* **Ruff** → linting / análise estática
* **requests** → consumo de API REST
* **zoneinfo** → fuso horário local (fallback)
* **Git** → controle de versão
* **GitHub** → hospedagem do repositório
* **GitHub Actions** → integração contínua (CI)
* **GitHub Issues** → gestão de demandas
* **PyInstaller** → geração da versão executável (`.exe`)
* **PythonAnywhere** → deploy da versão web

---

## 📂 Estrutura do projeto

```text
remedio-em-dia/
├── src/
│   ├── main.py                       # CLI (entrada principal)
│   ├── medication_manager.py         # Lógica de negócio
│   ├── models.py                     # Modelo Medicamento (com UUID)
│   ├── validation.py                 # Validação extraída
│   ├── storage.py                    # Persistência JSON
│   ├── api/
│   │   └── time_service.py           # Integração com timeapi.io
│   └── web/
│       ├── app.py                    # Flask (interface web)
│       └── templates/
│           └── index.html            # Template Jinja2
├── tests/
│   ├── test_medication_manager.py    # Testes unitários
│   ├── test_storage.py              # Testes de persistência
│   ├── test_time_api.py             # Teste de integração (API)
│   └── test_web_app.py             # Testes de integração (Flask)
├── data/
│   └── medications.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
├── pyproject.toml
├── VERSION
├── .gitignore
└── README.md
```

---

## 🖥️ Interfaces da aplicação

A aplicação conta com **duas interfaces** que compartilham a mesma lógica de negócio:

### Interface Web (Flask)

Acesse: **https://juanpbarros.pythonanywhere.com**

A interface web exibe os medicamentos em cards com código de cores:
* 🟢 **Verde** — dose já tomada
* 🔴 **Vermelho** — horário atrasado
* 🔵 **Azul** — pendente

### Interface CLI (linha de comando)

Menu principal com as opções de cadastro, listagem, marcação de doses e remoção:

```text
=== Remédio em Dia ===
1. Cadastrar medicamento
2. Listar medicamentos
3. Marcar dose como tomada
4. Remover medicamento
5. Sair
```

---

## ▶️ Como executar o projeto pelo código-fonte

### 1. Clonar o repositório

```bash
git clone https://github.com/juanpbarros/Rem-dioEmDia.git
cd Rem-dioEmDia
```

---

### 2. Criar um ambiente virtual (recomendado)

```bash
python -m venv .venv
```

---

### 3. Ativar o ambiente virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

---

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Executar a aplicação

#### Interface CLI

```bash
python src/main.py
```

#### Interface Web

```bash
python -m flask --app src/web/app run
```

---

## ⬇️ Como executar a versão executável (.exe)

Caso prefira, também é possível utilizar a versão executável da aplicação, sem necessidade de instalar Python.

### Download direto

[Baixar Remédio em Dia (.zip)](https://github.com/juanpbarros/Rem-dioEmDia/releases/download/v1.0.1/RemedioEmDia.zip)

### Passos para uso

1. Baixe o arquivo `.zip`
2. Extraia todos os arquivos
3. Execute o arquivo `.exe`

### Observações importantes

* Compatível com **Windows**
* **Não requer instalação do Python**
* O Windows pode exibir um aviso de segurança por se tratar de um executável **não assinado digitalmente**
* O código-fonte permanece disponível neste repositório para consulta e validação

---

## 🧪 Testes automatizados

O projeto possui **19 testes automatizados** utilizando **Pytest**, divididos em:

* **Testes unitários** — cadastro, validação, marcação de doses, remoção, ordenação
* **Testes de integração** — comunicação com API externa (timeapi.io)
* **Testes de integração web** — rotas do Flask (home, adicionar, remover, marcar)
* **Testes de persistência** — salvar/carregar JSON

### Rodar os testes

```bash
python -m pytest
```

---

## 🔍 Análise estática de código (Lint)

O projeto utiliza **Ruff** para análise estática de código, ajudando a manter a organização, padronização e qualidade do código-fonte.

### Rodar o lint

```bash
python -m ruff check .
```

---

## ⚙️ Integração Contínua (CI)

O projeto conta com uma pipeline de **Integração Contínua** configurada com **GitHub Actions**.

A cada `push` ou `pull request` na branch `main`, o GitHub executa automaticamente:

* instalação do ambiente Python;
* instalação das dependências;
* análise estática com Ruff;
* execução dos testes com Pytest.

Isso garante maior confiabilidade e reprodutibilidade do projeto.

## 🚀 Deploy

A versão web está publicada em:

**👉 https://juanpbarros.pythonanywhere.com**

O deploy foi realizado no **PythonAnywhere** (plano gratuito), com configuração WSGI manual e ambiente virtual isolado.

---

## 📦 Persistência de dados

Os dados da aplicação são armazenados localmente em um arquivo JSON:

```text
data/medications.json
```

Essa abordagem foi escolhida por ser simples, leve e suficiente para o escopo da versão inicial da aplicação.

---

## 🔖 Versionamento

O projeto utiliza **versionamento semântico**, no formato:

```text
MAJOR.MINOR.PATCH
```

Versão atual do projeto:

```text
1.0.1
```

---

## 🚀 Evoluções futuras

O projeto foi pensado com **escopo evolutivo**, permitindo futuras expansões. Algumas melhorias previstas para próximas versões incluem:

* sistema de lembretes (notificações);
* autenticação de usuários;
* histórico mais detalhado de doses;
* relatórios e exportação de dados;
* melhorias de usabilidade e acessibilidade.

---

## 👨‍💻 Autor

**Juan Barros**
Projeto acadêmico desenvolvido para atividade de BootCamp.

---

## 📄 Licença

Este projeto foi desenvolvido para fins **acadêmicos e educacionais**.
