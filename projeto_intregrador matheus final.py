def mostrar_info_aula(opcao):
    academias = {
        1: {
            "nome": "Jiu-Jitsu",
            "professor": "matheus",
            "dias": ["Segunda", "Quarta", "Sexta"],
            "horario": "19:00 - 20:30",
            "plano": "Plano Multi"
        },
        2: {
            "nome": "Muay Thai",
            "professor": "joao",
            "dias": ["Terça", "Quinta", "Sábado"],
            "horario": "18:00 - 19:30",
            "plano": "Plano mult"
        },
        3: {
            "nome": "Boxe",
            "professor": "pedro",
            "dias": ["Segunda", "Quarta", "Sexta"],
            "horario": "20:30 - 22:00",
            "plano": "plano simples"
        },
        4: {
            "nome": "MMA",
            "professor": "matheus",
            "dias": ["Terça", "Quinta", "Sábado"],
            "horario": "19:30 - 21:00",
            "plano": "Plano simples"
        },
        5:{
            "nome": "Capoeira",
            "professor": "mestre pulga",
            "dias": ["Segunda", "Quarta", "Sexta"], 
            "horario": "17:30 - 19:00",
            "plano": "Plano mult"
        }
    }
    
    if opcao in academias:
        info = academias[opcao]
        print(f"\nAula: {info['nome']}")
        print(f"Professor: {info['professor']}")
        print(f"Dias da semana: {', '.join(info['dias'])}")
        print(f"Horário: {info['horario']}")
        print(f"Incluso no: {info['plano']}")
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

def main():
    print("Bem-vindo ao Centro de Treinamento Berg!")
    print("Escolha uma aula para mais informações:")
    print("1 - Jiu-Jitsu")
    print("2 - Muay Thai")
    print("3 - Boxe")
    print("4 - MMA")
    print("5 - Capoeira")
    
    try:
        escolha = int(input("Digite o número da opção desejada: "))
        mostrar_info_aula(escolha)
    except ValueError:
        print("Por favor, digite um número válido.")
if __name__ == "__main__":
    main()