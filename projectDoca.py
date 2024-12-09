class RegistroDocas:
    def __init__(self, veiculo, placa, empresa, nome_motorista, rg_motorista, ajudante, telefone, loja_destino, observacoes):
        self.veiculo = veiculo
        self.placa = placa
        self.empresa = empresa
        self.nome_motorista = nome_motorista
        self.rg_motorista = rg_motorista
        self.ajudante = ajudante
        self.telefone = telefone
        self.loja_destino = loja_destino
        self.observacoes = observacoes

    def exibir_registro(self):
        print("----- Registro de Acesso -----")
        print(f"Veículo: {self.veiculo}")
        print(f"Placa: {self.placa}")
        print(f"Empresa: {self.empresa}")
        print(f"Nome do Motorista: {self.nome_motorista}")
        print(f"RG do Motorista: {self.rg_motorista}")
        print(f"Ajudante: {self.ajudante}")
        print(f"Telefone: {self.telefone}")
        print(f"Loja Destino: {self.loja_destino}")
        print(f"Observações: {self.observacoes}")
        print("----------------------------")

# Função para registrar o acesso
def registrar_acesso():
    print("Cadastro de Acesso à Doca\n")
    veiculo = input("Digite o tipo de veículo: ")
    placa = input("Digite a placa do veículo: ")
    empresa = input("Digite o nome da empresa: ")
    nome_motorista = input("Digite o nome do motorista: ")
    rg_motorista = input("Digite o RG do motorista: ")
    ajudante = input("Digite o nome do ajudante: ")
    telefone = input("Digite o telefone de contato: ")
    loja_destino = input("Digite a loja de destino: ")
    observacoes = input("Digite observações adicionais: ")

    # Criação do objeto de registro e exibição do mesmo
    registro = RegistroDocas(veiculo, placa, empresa, nome_motorista, rg_motorista, ajudante, telefone, loja_destino, observacoes)
    registro.exibir_registro()

# Função principal
def main():
    while True:
        print("\nControle de Acesso a Docas")
        print("1. Registrar novo acesso")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_acesso()
        elif opcao == '2':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
1