# 💊 Remédio em Dia

> Aplicação em Python desenvolvida para auxiliar no controle de medicamentos de idosos, cuidadores e familiares, promovendo mais organização, segurança e acompanhamento da rotina medicamentosa.

---

## ⬇️ Download da aplicação

A aplicação também pode ser utilizada por meio da versão executável para Windows:

* [Baixar Remédio em Dia (.zip)](https://github.com/juanpbarros/Rem-dioEmDia/releases/download/v1.0.1/RemediaEmDia.zip)
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
* ✅ Persistência local em arquivo JSON
* 🌐 Integração com API de data e hora

---

## 🌐 Integração com API

A aplicação consome uma API pública de data e hora para exibir informações atualizadas ao usuário durante a execução.

Essa integração permite:

* contextualizar os horários dos medicamentos;
* possibilitar futuras funcionalidades como alertas de atraso;
* enriquecer a experiência do usuário com dados em tempo real.

A comunicação com a API é realizada por meio de requisições HTTP, com tratamento de erros para garantir que a aplicação continue funcionando mesmo em caso de falhas externas.

---

## 🛠️ Tecnologias utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias e ferramentas:

* **Python 3.14**
* **Pytest** → testes automatizados
* **Ruff** → linting / análise estática
* **Requests** → consumo de API
* **Git** → controle de versão
* **GitHub** → hospedagem do repositório
* **GitHub Actions** → integração contínua (CI)
* **PyInstaller** → geração da versão executável (`.exe`)

---

## 📂 Estrutura do projeto

```text
remedio-em-dia/
├── src/
│   ├── main.py
│   ├── medication_manager.py
│   ├── models.py
│   ├── storage.py
│   └── api/
│       └── time_service.py
├── tests/
│   ├── test_medication_manager.py
│   ├── test_storage.py
│   └── test_time_api.py
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

## 🖥️ Interface da aplicação

A aplicação utiliza uma **interface CLI (Command Line Interface)**, permitindo interação via terminal.

### Exemplo de menu

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

```bash
python -m src.main
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
* Não requer instalação do Python
* O Windows pode exibir um aviso de segurança por se tratar de um executável não assinado digitalmente
* O código-fonte permanece disponível neste repositório para consulta e validação

---

## 🧪 Testes automatizados

O projeto possui testes automatizados utilizando **Pytest**, incluindo:

* testes unitários das funcionalidades principais;
* validação de entradas inválidas;
* testes de persistência;
* teste de integração com API (utilizando mock).

### Rodar os testes

```bash
python -m pytest
```

---

## 🔍 Análise estática de código (Lint)

O projeto utiliza **Ruff** para análise estática de código.

### Rodar o lint

```bash
python -m ruff check .
```

---

## ⚙️ Integração Contínua (CI)

O projeto conta com uma pipeline de **Integração Contínua** com GitHub Actions.

A cada push ou pull request:

* instalação do ambiente Python;
* instalação das dependências;
* execução do lint;
* execução dos testes.

---

## 📦 Persistência de dados

Os dados são armazenados em:

```text
data/medications.json
```

---

## 🔖 Versionamento

O projeto utiliza versionamento semântico:

```text
MAJOR.MINOR.PATCH
```

Versão atual:

```text
1.0.1
```

---

## 🚀 Evoluções futuras

O projeto foi planejado para evolução contínua, incluindo:

* interface gráfica (GUI);
* versão web da aplicação;
* sistema de lembretes;
* histórico detalhado de doses;
* melhorias de usabilidade e acessibilidade.

---

## 👨‍💻 Autor

**Juan Barros**  
Projeto acadêmico desenvolvido para BootCamp.

---

## 📄 Licença

Projeto desenvolvido para fins educacionais.
