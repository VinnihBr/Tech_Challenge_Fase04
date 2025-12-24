# Tech_Challenge_Fase04

## Simulador de Obesidade com Análise Preditiva

Este projeto foi desenvolvido como parte do Tech Challenge – Fase 04 da Pós-Graduação em Data Analytics (FIAP).
O objetivo é analisar fatores associados à obesidade, identificar padrões comportamentais e biométricos e disponibilizar uma aplicação web usando o Streamlit.

## Objetivo do Projeto

- Analisar dados populacionais relacionados à obesidade

- Identificar correlações entre hábitos alimentares, comportamento e perfil biométrico

- Desenvolver modelos de Machine Learning para apoio à análise

## Base de Dados

- A base utilizada (df_target.csv) contém 2.111 registros, incluindo variáveis como:

- Idade, gênero, peso e altura

- Hábitos alimentares (vegetais, alimentos hipercalóricos, lanches)

- Nível de atividade física

- Monitoramento de calorias

- Histórico familiar de obesidade

Os dados permitem uma análise integrada entre perfil biométrico, comportamental e predisposição genética.

## Modelagem e Análise Preditiva

Foram utilizados modelos de Machine Learning para apoio à análise, com foco em:

- Identificação de padrões associados à obesidade

- Avaliação do impacto combinado de múltiplas variáveis

- Apoio à interpretação dos dados (não substituindo diagnóstico médico)

Principais bibliotecas utilizadas:

- pandas

- numpy

- scikit-learn

- xgboost

- joblib

## Aplicação Web – Streamlit

A aplicação foi desenvolvida em Streamlit e permite:

- Visualização interativa dos dados

- Exploração dos perfis populacionais

- Simulação e análise dos fatores relacionados à obesidade

Deploy realizado com sucesso no Streamlit Cloud, utilizando:

- Python 3.10

- Streamlit >= 1.33.0

## Principais Conclusões

A obesidade na amostra analisada não é um fenômeno isolado

Há forte relação entre:

- Balanço energético positivo

- Falta de monitoramento alimentar

- Sedentarismo

- Predisposição genética

Estratégias eficazes devem focar no controle calórico global e mudança de hábitos, e não apenas na inclusão de alimentos saudáveis pontuais.

# Executando o Projeto Localmente no VS Code

Como configurar o ambiente e executar a aplicação Streamlit localmente utilizando o Visual Studio Code.

Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

Python 3.10
https://www.python.org/downloads/release/python-3100/

Visual Studio Code
https://code.visualstudio.com/

Extensão Python no VS Code (Microsoft)

Para verificar a versão do Python:

python --version

Clonar o Repositório

Abra o Terminal do VS Code (`Ctrl + ``) e execute:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Criar e Ativar Ambiente Virtual (Recomendado)
Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate


Após ativar, o nome do ambiente (venv) deve aparecer no terminal.

Instalar as Dependências

Com o ambiente virtual ativo:

pip install --upgrade pip
pip install -r requirements.txt

Configurar o Python no VS Code

Pressione Ctrl + Shift + P

Selecione Python: Select Interpreter

Escolha o interpretador do ambiente virtual:

venv\Scripts\python.exe (Windows)

venv/bin/python (macOS/Linux)

Executar a Aplicação Streamlit

No terminal do VS Code:

streamlit run app.py

Após executar o comando:

O Streamlit iniciará um servidor local

O navegador abrirá automaticamente em:

http://localhost:8501

E agora usar a aplicação.

## Autores

Vinicius Dias, Bruno de Andrade e João Pedro

Pós-Graduação em Data Analytics – FIAP
