# python-automation-pdf-to-json

Automação em Python e Django que permite enviar um arquivo PDF via upload, processá-lo usando a API do ChatGPT (OpenAI) e gerar um JSON estruturado com todas as informações extraídas.

## Visão Geral

Este projeto oferece uma interface web simples para que o usuário envie um PDF.  
O sistema então utiliza um script Python para:

1. Ler e interpretar o conteúdo do PDF.
2. Enviar o texto para a API do ChatGPT.
3. Receber e organizar os dados extraídos em um **JSON estruturado**.
4. Disponibilizar o resultado para download diretamente pelo navegador.

## Estrutura Principal

- **`manage.py`** — ponto de entrada para iniciar o servidor Django.
- **`python_automation/uploads/convertion.py`** — script responsável pela conversão do PDF para JSON usando o ChatGPT.
- **Templates HTML** — exibem formulário de upload e botão de download.
- **Pasta `uploads`** — módulo que gerencia o upload, conversão e resposta.

## Pré-requisitos

- Python **3.8+**
- Django
- Bibliotecas listadas em `requirements.txt`
- Chave de API válida da OpenAI (`OPENAI_API_KEY`)
- Conexão com a internet

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/pedrofortunato2804/python-automation-pdf-to-json.git
   cd python-automation-pdf-to-json
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure sua chave da OpenAI no `.env`:
   ```env
   OPENAI_API_KEY=sua_chave_aqui
   ```

## Como usar

1. Inicie o servidor Django:
   ```bash
   python manage.py runserver
   ```
2. No navegador, acesse:
   ```
   http://127.0.0.1:8000/upload
   ```
3. Faça o upload do PDF desejado.
4. Aguarde alguns minutos (o ChatGPT processará o documento).
5. Assim que a conversão terminar, a página exibirá um botão **Download** para salvar o arquivo JSON gerado.

## Exemplo de Saída (JSON)

```json
{
  "documento": "MINUTA DE ESCRITURA PÚBLICA DE VENDA E COMPRA",
  "fonte": {
    "site": "www.siteleilao.com.br",
    "leiloeiro": "Fulano de Tal - Leiloeiro Público Oficial"
  },
  "escritorios": [
    {
      "cidade": "Cidade Um",
      "estado": "UF",
      "endereco": "Rua do Sul, 1234",
      "cep": "99999-123",
      "telefone": "(55) 3333-3333",
      "celular": "(51) 99999-9999",
      "email": "cidadeum@siteleilao.com.br"
    },
    {
      "cidade": "Cidade Dois",
      "estado": "UF",
      "endereco": "Rua do Norte, 123",
      "cep": "99999-123",
      "telefone": "(51) 3333-3333",
      "celular": "(51) 99999-9999",
      "email": "leilao@siteleilao.com.br"
    }
  ],
  "partes": {
    "outorgante_vendedor": {
      "nome": "Fulano de Tal",
      "estabelecido": "Capital do Estado de Minas Gerais",
      "sede": "Cidade Tal",
      "cnpj": "99.999.999/0001-99",
      "representacao": {
        "procuração": {
          "cartorio": "Alguma Coisa Cartório Tal de Tal",
          "livro": "Tal Qual",
          "folhas": "1 - 517"
        }
      }
    },
    "outorgados_compradores": [
      {
        "nome": "Fulana Ciclana da Silva Santos Silva e Santos"
      }
    ]
  },
  "imovel": {
    "propriedade": {
      "registro_numero": "0123495",
      "matricula": "21",
      "cri": "123",
      "ano": "2011"
    },
    "descricao": "(DESCREVER O IMÓVEL)",
    "aquisição_anterior": {
      "forma": "Forma",
      "registro_numero": "211",
      "matriculas": [
        "244",
        "245"
      ],
      "cartorio": "Cartório de Imóveis de Cidade Fulano"
    },
    "cadastro_prefeitura": {
      "municipio": "Cidade Fulano",
      "inscricoes": [
        "218",
        "2178",
        "312",
        "1234"
      ],
      "valor_venal": {
        "valor": 1000.0,
        "moeda": "BRL",
        "extenso": "MIL REAIS",
        "exercicio": "presente exercício"
      }
    }
  },
  "leilao": {
    "condicoes_incorporadas_ao_instrumento": true,
    "data_edital": "23/01/2020",
    "data_leilao_lance_vencedor": "21/03/2020",
    "preco_venda": {
      "valor": 1500.0,
      "moeda": "BRL",
      "extenso": "MIL E QUINHENTOS REAIS"
    },
    "data_pagamento": "25/03/2020",
    "quitacao_conferida": true,
    "transferencia_dominio": true
  },
  "clausulas": [],
  "foro_eleito": "Comarca da Capital",
  "assinaturas": {
    "data": {
      "dia": "01",
      "mes": "01",
      "ano": "2000"
    },
    "vendedor": "Fulano",
    "comprador": "Ciclano",
    "testemunhas": [
      {
        "nome": "Fulana",
        "rg": "12345678",
        "cpf": "12345678901"
      },
      {
        "nome": "Ciclana",
        "rg": "12345678",
        "cpf": "12345678901"
      }
    ]
  }
}
```

> O formato final pode variar dependendo do conteúdo do PDF e da lógica implementada no `convertion.py`.
