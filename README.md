# Sistema de Cadastro de Alunos - Faculdade

Realizado por: Igor Silva Martins; Mateus Bresciani

Trabalho N3 da disciplina **Estrutura de Dados e Organização de Arquivos**.

Programa em Python, executado pelo terminal, que gerencia o cadastro de alunos de uma faculdade. Os dados ficam salvos em um arquivo JSON, então continuam existindo depois que o programa é fechado.

## Arquivos do projeto

| Arquivo | Descrição |
|---|---|
| `sistema_faculdade.py` | Código do programa (menu e todas as funções) |
| `faculdade.json` | Banco de dados em JSON com cursos e alunos de exemplo |
| `README.md` | Documentação |

## Como executar

1. Ter o Python 3 instalado.
2. Deixar `sistema_faculdade.py` e `faculdade.json` na mesma pasta.
3. No terminal, dentro da pasta, rodar:

```bash
python sistema_faculdade.py
```

Não é preciso instalar nenhuma biblioteca externa (usa apenas o módulo `json`, que já vem com o Python).

## Estrutura dos dados (`faculdade.json`)

O arquivo tem duas listas: `cursos` e `alunos`.

```json
{
  "cursos": [
    {"codigo": "ADS", "nome": "Análise e Desenvolvimento de Sistemas",
     "coordenador": "Prof. Marcos Ribeiro", "carga_horaria": 2000}
  ],
  "alunos": [
    {"matricula": 20260001, "nome": "Ana Beatriz Souza", "curso": "ADS",
     "semestre": 3, "email": "ana.souza@faculdade.edu.br", "cidade": "Sinop"}
  ]
}
```

**Cursos:** `codigo`, `nome`, `coordenador`, `carga_horaria`

**Alunos:** `matricula` (número, identificador único), `nome`, `curso` (código de um curso existente), `semestre`, `email`, `cidade`

## Funcionalidades

O programa mostra um menu com as opções abaixo.

### 1 - Incluir aluno
Pede matrícula, nome, curso, semestre, e-mail e cidade. Antes de salvar, valida:
- a matrícula não pode já existir;
- o curso informado precisa existir na lista de cursos.

### 2 - Alterar aluno
Busca o aluno pela matrícula, mostra os dados atuais e pede os novos valores. Se o campo for deixado em branco, o valor atual é mantido. A matrícula não pode ser alterada.

### 3 - Excluir aluno
Busca o aluno pela matrícula, mostra os dados e pede confirmação (`s`/`n`) antes de remover.

### 4 - Pesquisar aluno
Pesquisa por campos do tipo texto: **nome**, **curso**, **cidade** ou **e-mail**. A busca ignora maiúsculas e minúsculas e encontra o texto em qualquer parte do campo (por exemplo, `ana` encontra "Ana Beatriz Souza").

### 5 - Listar alunos ordenados
Imprime a lista de alunos em duas ordenações diferentes:
- **Por nome** (ordem alfabética A-Z);
- **Por curso e, dentro do mesmo curso, por nome**.

### 0 - Sair
Encerra o programa.

## Como o código funciona

- `carregar()` lê o `faculdade.json` com `json.load` e devolve os dados.
- `salvar(dados)` grava os dados de volta no arquivo com `json.dump` (com `ensure_ascii=False` para manter os acentos e `indent=2` para o arquivo ficar legível). É chamada depois de cada inclusão, alteração e exclusão.
- A pesquisa e a exclusão usam *list comprehension* para filtrar a lista de alunos.
- A ordenação usa `sorted()` com `key=lambda`; na segunda ordenação a chave é uma tupla `(curso, nome)`, o que ordena pelos dois campos.
- Entradas numéricas (matrícula e semestre) são validadas para evitar erro caso o usuário digite texto.

## Requisitos da atividade atendidos

| Requisito | Onde está |
|---|---|
| Incluir, alterar, excluir | opções 1, 2 e 3 do menu |
| Persistência em JSON | `carregar()` e `salvar()` |
| Pesquisa por campos de texto | opção 4 do menu |
| Listas ordenadas por 2 campos diferentes | opção 5 do menu (nome; curso + nome) |
| Linguagem Python | `sistema_faculdade.py` |
