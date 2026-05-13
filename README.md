# 💊 Remédio em Dia

> Aplicação web em Python desenvolvida para auxiliar no controle de medicamentos de idosos, cuidadores e familiares, promovendo mais organização, segurança e acompanhamento da rotina medicamentosa.

## 🌐 Acesso online

A aplicação está disponível em:

**👉 https://juanpbarros.pythonanywhere.com**

---

## 📌 Sobre o projeto

O **Remédio em Dia** é uma aplicação web desenvolvida com o objetivo de auxiliar no controle da administração de medicamentos, especialmente para **idosos**, **cuidadores** e **familiares** que necessitam acompanhar horários e doses de forma mais organizada.

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

## 💡 Funcionalidades

* ✅ Cadastrar medicamento com nome e dosagem
* ✅ Definir horários de uso
* ✅ Visualizar medicamentos com código de cores (tomado, atrasado, pendente)
* ✅ Marcar doses como tomadas
* ✅ Remover medicamentos
* ✅ Identificador único (UUID) para cada medicamento
* ✅ Ordenação automática por horário
* ✅ Persistência local em arquivo JSON
* ✅ Integração com API pública REST (timeapi.io) para data/hora
* ✅ Fallback local automático caso a API esteja indisponível

---

## 🛠️ Tecnologias utilizadas

* **Python 3.14**
* **Flask** — framework web
* **Pytest** — testes automatizados
* **Ruff** — linting / análise estática
* **requests** — consumo de API REST
* **zoneinfo** — fuso horário local (fallback)
* **Git** — controle de versão
* **GitHub** — hospedagem do repositório
* **GitHub Actions** — integração contínua (CI)
* **GitHub Issues** — gestão de demandas
* **PythonAnywhere** — deploy

---

## 📂 Estrutura do projeto

```text
remedio-em-dia/
├── src/
│   ├── medication_manager.py         # Lógica de negócio
│   ├── models.py                     # Modelo Medicamento (com UUID)
│   ├── validation.py                 # Validação
│   ├── storage.py                    # Persistência JSON
│   ├── api/
│   │   └── time_service.py           # Integração com timeapi.io
│   └── web/
│       ├── app.py                    # Aplicação Flask
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

## 🖥️ Interface

A interface web exibe os medicamentos em cards com código de cores:

* 🟢 **Verde** — dose já tomada
* 🔴 **Vermelho** — horário atrasado
* 🔵 **Azul** — pendente

---

## ▶️ Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/juanpbarros/Rem-dioEmDia.git
cd Rem-dioEmDia
```

### 2. Criar e ativar ambiente virtual

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar

```bash
python -m flask --app src/web/app run
```

Acesse no navegador: **http://localhost:5000**

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

O projeto utiliza **Ruff** para análise estática.

```bash
python -m ruff check .
```

---

## ⚙️ Integração Contínua (CI)

O projeto conta com uma pipeline de **Integração Contínua** configurada com **GitHub Actions**. A cada `push` ou `pull request` na branch `main`, o GitHub executa automaticamente:

* instalação do ambiente Python;
* instalação das dependências;
* análise estática com Ruff;
* execução dos testes com Pytest.

---

## 🚀 Deploy

A aplicação está publicada em:

**👉 https://juanpbarros.pythonanywhere.com**

O deploy foi realizado no **PythonAnywhere** (plano gratuito), com configuração WSGI manual e ambiente virtual isolado.

---

## 📦 Persistência de dados

Os dados ficam armazenados localmente em um arquivo JSON:

```text
data/medications.json
```

---

## 🔖 Versionamento

O projeto utiliza **versionamento semântico** (MAJOR.MINOR.PATCH). Versão atual: **1.0.1**.

---

## 👨‍💻 Autor

**Juan Barros** — Projeto acadêmico desenvolvido para atividade de BootCamp.

---

## 📄 Licença

Este projeto foi desenvolvido para fins **acadêmicos e educacionais**.
