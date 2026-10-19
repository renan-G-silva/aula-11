# 🌊 Sistema de Monitoramento de Reservatório

Sistema simples em Python que exibe alertas coloridos no terminal conforme o nível de água de um reservatório.

## 📋 Descrição

O programa mostra 5 níveis de água, cada um com uma mensagem e uma cor diferente, usando a biblioteca **colorama** para destacar cada situação.

| Nível | Situação | Cor |
|-------|----------|-----|
| Nível 1 | Muito baixo (crítico) | Vermelho |
| Nível 2 | Baixo | Amarelo |
| Nível 3 | Médio | Verde |
| Nível 4 | Alto | Ciano |
| Nível 5 | Muito alto (alerta) | Azul |

## 🛠️ Requisitos

- Python 3 instalado
- Biblioteca `colorama`

## 📦 Instalação

No terminal, execute:

```bash
pip install colorama