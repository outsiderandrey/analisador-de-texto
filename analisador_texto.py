import os
import string


### Importante: que o arquivo .txt esteja na mesma pasta que o arquivo deste codigo. ###
### Important: the .txt file must be in the same folder as this program. ###


def abrir_arquivo():
    while True:
        nome = input("Digite o nome do arquivo (.txt): ")

        if os.path.exists(nome):
            arq = open(nome, "r", encoding="utf-8")
            linhas = arq.readlines()
            arq.close()
            return linhas
        else:
            print("arquivo não encontrado, tenta de novo\n")



def limpar_texto(linhas):
    texto = "".join(linhas).lower()

    for p in string.punctuation:
        texto = texto.replace(p, "")

    return texto


def contar_palavras(linhas):   #op2
    palavras = limpar_texto(linhas).split()  
    print("Total de palavras:", len(palavras))


def contar_distintas(linhas):  #op2
    unicas = []
    palavras = limpar_texto(linhas).split() 

    for p in palavras:
        if p not in unicas:
            unicas.append(p)

    print("Palavras distintas:", len(unicas))


def contar_linhas(linhas):  #op3
    print("Quantidade de linhas:", len(linhas))


def frequencia(linhas):  #op4
    pal = limpar_texto(linhas)
    palavras = pal.split()
    freq = {}
    for p in palavras:
        freq[p] = freq.get(p, 0) + 1
    for palavra in freq:
        print(palavra, ":", freq[palavra])


def imprimir_linha(linhas):  #op5
    n = int(input("Digite o número da linha: "))
    if 1 <= n <= len(linhas):
        print(linhas[n-1])
    else:
        print("Linha inválida")


def buscar_palavra(linhas):  #op6
    busca = input("Digite a palavra: ").lower()
    for linha in linhas:
        if busca in linha.lower():
            print(linha)
            return
    print("Palavra não encontrada")


def substituir_palavra(linhas):  #op7
    antiga = input("Palavra antiga: ")
    nova = input("Nova palavra: ")
    nome = input("Nome do novo arquivo (.txt): ")

    novas_linhas = []

    for linha in linhas:
        novas_linhas.append(linha.replace(antiga, nova))

    novo_texto = "".join(novas_linhas)

    open(nome, "w", encoding="utf-8").write(novo_texto)
    print("Arquivo salvo!")

def texto_novo():  #op8
    while True:
        nome = input("Digite o novo arquivo (.txt): ")
        if os.path.exists(nome):
            with open(nome, "r", encoding="utf-8") as arq:
                return arq.readlines() 
        else:
            print("Arquivo não encontrado, tenta de novo\n")


def mostrar_menu():
    print("\n" + "="*50)
    print("      MENU DE OPÇÕES")
    print("="*50)
    print(" 1 - Número de palavras")
    print(" 2 - Palavras distintas")
    print(" 3 - Número de linhas")
    print(" 4 - Frequência das palavras")
    print(" 5 - Imprimir linha específica")
    print(" 6 - Buscar palavra")
    print(" 7 - Substituir palavra",)
    print(" 8 - Abrir outro arquivo")
    print(" 9 - Encerrar programa")
    print("="*50)


def main():
    arq = abrir_arquivo()


    while True:
        mostrar_menu()
        op = input("Escolha uma opção: ")

        if op == "1":
            contar_palavras(arq)

        elif op == "2":
            contar_distintas(arq)

        elif op == "3":
            contar_linhas(arq)

        elif op == "4":
            frequencia(arq)

        elif op == "5":  
            imprimir_linha(arq) 
            
        elif op == "6":
            buscar_palavra(arq)

        elif op == "7":
            substituir_palavra(arq)

        elif op == "8":
            arq = texto_novo()

        elif op == "9":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida, digite novamente!")
main()