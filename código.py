# Lista para armazenar aluno
alunos = []

# Função para adicionar alunos
def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno = {'nome': nome, 'notas': [], 'frequencia': 0}
    alunos.append(aluno)
    print(f"Aluno {nome} adicionado com sucesso!")

# Função para editar o nome de um aluno
def editar_aluno():
    nome = input("Digite o nome do aluno que deseja editar: ")
    for aluno in alunos:
        if aluno['nome'] == nome:
            novo_nome = input(f"Digite o novo nome para {nome}: ")
            aluno['nome'] = novo_nome
            print(f"Nome do aluno {nome} atualizado para {novo_nome}.")
            return
    print(f"Aluno {nome} não encontrado.")

# Função para remover um aluno
def remover_aluno():
    nome = input("Digite o nome do aluno que deseja remover: ")
    for aluno in alunos:
        if aluno['nome'] == nome:
            alunos.remove(aluno)
            print(f"Aluno {nome} removido com sucesso!")
            return
    print(f"Aluno {nome} não encontrado.")

# Função para adicionar notas a um aluno
def adicionar_notas():
    nome = input("Digite o nome do aluno que deseja adicionar notas: ")
    for aluno in alunos:
        if aluno['nome'] == nome:
            if len(aluno['notas']) < 4:
                nota = float(input(f"Digite a nota (0-10) para {nome}: "))
                aluno['notas'].append(nota)
                print(f"Nota {nota} adicionada ao aluno {nome}.")
            else:
                print("Esse aluno já tem 4 notas.")
            return
    print(f"Aluno {nome} não encontrado.")

# Função para adicionar frequência
def adicionar_frequencia(carga_horaria):
    nome = input("Digite o nome do aluno que deseja adicionar frequência: ")
    for aluno in alunos:
        if aluno['nome'] == nome:
            frequencia = int(input(f"Digite a frequência (número de aulas assistidas) para {nome}: "))
            aluno['frequencia'] = frequencia
            print(f"Frequência {frequencia} aulas adicionada ao aluno {nome}.")
            return
    print(f"Aluno {nome} não encontrado.")

# Função para calcular a média de notas
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Função para calcular a situação do aluno
def calcular_situacao(aluno, carga_horaria):
    media = calcular_media(aluno['notas'])
    frequencia = aluno['frequencia']
    
    if frequencia < 0.75 * carga_horaria:
        return "Reprovado por Falta"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado por Nota"

# Função para imprimir o relatório de todos os alunos
def imprimir_relatorio_geral(carga_horaria):
    print("\nRelatório Geral dos Alunos:")
    for i, aluno in enumerate(alunos, 1):
        media = calcular_media(aluno['notas'])
        situacao = calcular_situacao(aluno, carga_horaria)
        print(f"{i}. {aluno['nome']} - Nota: {media:.1f} / Frequência: {aluno['frequencia']} aulas - ({situacao})")

# Função para imprimir relatório filtrado por situação
def imprimir_relatorio_filtrado(carga_horaria):
    situacao_filtro = input("Digite a situação para filtrar (Aprovado, Reprovado por Falta, Reprovado por Nota): ")
    print(f"\nRelatório de Alunos com situação: {situacao_filtro}")
    for i, aluno in enumerate(alunos, 1):
        situacao = calcular_situacao(aluno, carga_horaria)
        if situacao == situacao_filtro:
            media = calcular_media(aluno['notas'])
            print(f"{i}. {aluno['nome']} - Nota: {media:.1f} / Frequência: {aluno['frequencia']} aulas - ({situacao})")

# Função principal para o menu
def menu():
    carga_horaria = int(input("Digite a carga horária total da disciplina: "))
    
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Aluno")
        print("2. Editar Aluno")
        print("3. Remover Aluno")
        print("4. Adicionar Notas")
        print("5. Adicionar Frequência")
        print("6. Imprimir Relatório Geral")
        print("7. Imprimir Relatório por Situação")
        print("8. Sair")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            adicionar_aluno()
        elif opcao == 2:
            editar_aluno()
        elif opcao == 3:
            remover_aluno()
        elif opcao == 4:
            adicionar_notas()
        elif opcao == 5:
            adicionar_frequencia(carga_horaria)
        elif opcao == 6:
            imprimir_relatorio_geral(carga_horaria)
        elif opcao == 7:
            imprimir_relatorio_filtrado(carga_horaria)
        elif opcao == 8:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Execução do programa
menu()

#testando:
