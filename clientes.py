from util import calcular_media

def ler_dados_clientes():
    with open('clientes.txt', 'r') as arquivo:
        idades = []
        rendas = []
        for linha in arquivo:
            _, _, idade, renda = linha.strip().split(';')
            idades.append(int(idade))
            rendas.append(float(renda))
        return idades, rendas

def main():
    idades, rendas = ler_dados_clientes()
    media_idade = calcular_media(idades)
    media_renda = calcular_media(rendas)
    print(f"Média de idade: {media_idade:.2f} anos")
    print(f"Média de renda mensal: R${media_renda:.2f}")

if __name__ == "__main__":
    main()
