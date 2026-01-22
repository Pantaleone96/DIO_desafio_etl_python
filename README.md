# 📅 Monitor de Feriados Nacionais (ETL Pipeline)

> Projeto de Engenharia de Dados (ETL) desenvolvido em Python para monitorar feriados nacionais e calcular a contagem regressiva para as próximas datas comemorativas.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 💻 Sobre o Projeto

Este projeto foi criado como parte do desafio de **ETL (Extract, Transform, Load)**.
O sistema consome uma API pública, processa as datas e gera um relatório útil para planejamento.

## ⚙️ Funcionalidades (Pipeline ETL)

O projeto segue rigorosamente a arquitetura ETL:

* **EXTRACT (Extração):**
    * Conecta à API pública **BrasilAPI** (`https://brasilapi.com.br/`) para obter os dados de feriados nacionais do ano corrente.
* **TRANSFORM (Transformação):**
    * Converte strings de data para objetos `datetime` do Python.
    * Traduz os dias da semana de Inglês para Português.
    * Calcula a **diferença de dias** entre a data atual e o feriado.
    * Filtra apenas os feriados futuros (ignora os que já passaram).
* **LOAD (Carregamento):**
    * Salva os dados processados em um arquivo `relatorio_feriados.csv` compatível com Excel (UTF-8).
    * Exibe um resumo tabular no console.

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem principal.
* **Requests**: Para consumo da API REST.
* **Pandas**: Para manipulação tabular dos dados e geração do CSV.
* **Datetime**: Para cálculos temporais.

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
    cd NOME-DO-REPO
    ```

2.  **Instale as dependências**
    ```bash
    pip install requests pandas
    ```

3.  **Execute o script**
    ```bash
    python app.py
    ```

4.  **Verifique o resultado**
    O arquivo `relatorio_feriados.csv` será gerado na pasta raiz do projeto.

## 📊 Exemplo de Saída (CSV)

| Feriado | Data | Dia da Semana | Dias Restantes | Status |
| :--- | :--- | :--- | :--- | :--- |
| Independência do Brasil | 07/09/2024 | Sábado | 15 | Em breve |
| Nossa Senhora Aparecida | 12/10/2024 | Sábado | 50 | Em breve |
| Finados | 02/11/2024 | Sábado | 71 | Em breve |

---

## 👨‍💻 Inácio Puntel

Desenvolvido por **Inácio Puntel**.
