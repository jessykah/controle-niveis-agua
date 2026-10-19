# 💧 Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.15%2B-blue?logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Biblioteca-Colorama-yellow)
![Status](https://img.shields.io/badge/Status-Em_desenvolvimento-orange)

## 📌 Sobre o projeto

Este projeto simula o monitoramento dos níveis de água de um reservatório, exibindo mensagens de alerta com cores diferentes no terminal, conforme a situação identificada.

A atividade foi desenvolvida para a **Agenda 11 — Desenvolvimento de Sistemas I**, da Etec.

## 🎯 Objetivo

Aplicar conceitos de programação estruturada utilizando listas, funções, estruturas condicionais, laços de repetição e bibliotecas Python.

## 🛠️ Tecnologias utilizadas

- 🐍 Python
- 🎨 Colorama

## ⚙️ Funcionalidades

- Armazena os cinco níveis de água em uma lista.
- Define a cor da mensagem conforme o nível informado.
- Exibe as situações do reservatório com cores no terminal.
- Restaura o estilo padrão após a exibição das mensagens.

## 🚦 Níveis do reservatório

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | 🔴 Vermelho |
| 2 | Baixo | 🟡 Amarelo |
| 3 | Médio | 🟢 Verde |
| 4 | Alto | 🩵 Ciano |
| 5 | Muito alto (alerta) | 🔵 Azul |

## ▶️ Como executar

### 1. Pré-requisitos

É necessário ter o Python instalado no computador.

### 2. Instalar a biblioteca

No terminal, execute:

```bash
py -m pip install colorama
```

Se o comando `py` não funcionar, tente:

```bash
python -m pip install colorama
```

### 3. Executar o programa

Na pasta do projeto, execute:

```bash
py app.py
```

Caso o comando `py` não funcione, tente:

```bash
python app.py
```

## 📁 Estrutura do projeto

```text
controle-niveis-agua/
├── app.py
└── README.md
```

## 📚 Aprendizados

Este projeto permite praticar listas, funções, estruturas condicionais, laços de repetição, importação de bibliotecas e formatação de mensagens no terminal.

## 👩‍💻 Autoria

Projeto acadêmico desenvolvido como atividade da Agenda 11 de Desenvolvimento de Sistemas I — Etec.