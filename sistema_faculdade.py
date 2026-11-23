import json

ARQUIVO = "faculdade.json"


def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)


def mostrar_aluno(aluno):
    print(f"{aluno['matricula']} | {aluno['nome']} | {aluno['curso']} | "
          f"{aluno['semestre']}º sem | {aluno['email']} | {aluno['cidade']}")


def buscar_por_matricula(dados, matricula):
    for aluno in dados["alunos"]:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def curso_existe(dados, codigo):
    return any(curso["codigo"] == codigo for curso in dados["cursos"])


def listar_cursos(dados):
    print("Cursos disponíveis:")
    for curso in dados["cursos"]:
        print(f"  {curso['codigo']} - {curso['nome']}")


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def incluir(dados):
    print("\n--- Incluir aluno ---")
    matricula = ler_inteiro("Matrícula: ")
    if buscar_por_matricula(dados, matricula):
        print("Já existe um aluno com essa matrícula.")
        return

    nome = input("Nome: ")
    listar_cursos(dados)
    curso = input("Código do curso: ").upper()
    if not curso_existe(dados, curso):
        print("Curso não encontrado.")
        return

    semestre = ler_inteiro("Semestre: ")
    email = input("E-mail: ")
    cidade = input("Cidade: ")

    dados["alunos"].append({
        "matricula": matricula,
        "nome": nome,
        "curso": curso,
        "semestre": semestre,
        "email": email,
        "cidade": cidade
    })
    salvar(dados)
    print("Aluno incluído com sucesso!")


def alterar(dados):
    print("\n--- Alterar aluno ---")
    matricula = ler_inteiro("Matrícula do aluno: ")
    aluno = buscar_por_matricula(dados, matricula)
    if not aluno:
        print("Aluno não encontrado.")
        return

    mostrar_aluno(aluno)
    print("Deixe em branco para manter o valor atual.")

    nome = input(f"Nome [{aluno['nome']}]: ")
    curso = input(f"Curso [{aluno['curso']}]: ").upper()
    semestre = input(f"Semestre [{aluno['semestre']}]: ")
    email = input(f"E-mail [{aluno['email']}]: ")
    cidade = input(f"Cidade [{aluno['cidade']}]: ")

    if nome:
        aluno["nome"] = nome
    if curso:
        if curso_existe(dados, curso):
            aluno["curso"] = curso
        else:
            print("Curso inexistente, mantido o anterior.")
    if semestre:
        if semestre.isdigit():
            aluno["semestre"] = int(semestre)
        else:
            print("Semestre inválido, mantido o anterior.")
    if email:
        aluno["email"] = email
    if cidade:
        aluno["cidade"] = cidade

    salvar(dados)
    print("Aluno alterado com sucesso!")


def excluir(dados):
    print("\n--- Excluir aluno ---")
    matricula = ler_inteiro("Matrícula do aluno: ")
    aluno = buscar_por_matricula(dados, matricula)
    if not aluno:
        print("Aluno não encontrado.")
        return

    mostrar_aluno(aluno)
    confirma = input("Confirma a exclusão? (s/n): ").lower()
    if confirma == "s":
        dados["alunos"] = [item for item in dados["alunos"] if item["matricula"] != matricula]
        salvar(dados)
        print("Aluno excluído com sucesso!")
    else:
        print("Exclusão cancelada.")



def pesquisar(dados):
    print("\n--- Pesquisar aluno ---")
    print("Campo | 1: Nome | 2: Curso | 3: Cidade | 4: E-mail")
    opcao = input("Escolha o campo: ")
    campos = {"1": "nome", "2": "curso", "3": "cidade", "4": "email"}

    if opcao not in campos:
        print("Opção inválida.")
        return

    campo = campos[opcao]
    termo = input("Digite o texto da busca: ").lower()

    encontrados = [item for item in dados["alunos"] if termo in item[campo].lower()]

    if not encontrados:
        print("Nenhum aluno encontrado.")
        return

    for aluno in encontrados:
        mostrar_aluno(aluno)


def listar_ordenado(dados):
    print("\n--- Listar alunos ordenados ---")
    print("Ordenar por | 1: Nome (A-Z) | 2: Curso e depois Nome")
    opcao = input("Escolha a ordenação: ")

    if opcao == "1":
        ordenados = sorted(dados["alunos"], key=lambda item: item["nome"].lower())
    elif opcao == "2":
        ordenados = sorted(dados["alunos"], key=lambda item: (item["curso"], item["nome"].lower()))
    else:
        print("Opção inválida.")
        return

    for aluno in ordenados:
        mostrar_aluno(aluno)


def menu():
    dados = carregar()

    while True:
        print("\n===== Sistema de Cadastro da Faculdade =====")
        print("1 - Incluir aluno")
        print("2 - Alterar aluno")
        print("3 - Excluir aluno")
        print("4 - Pesquisar aluno")
        print("5 - Listar alunos ordenados")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir(dados)
        elif opcao == "2":
            alterar(dados)
        elif opcao == "3":
            excluir(dados)
        elif opcao == "4":
            pesquisar(dados)
        elif opcao == "5":
            listar_ordenado(dados)
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")


menu()
