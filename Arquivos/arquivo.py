# Função para abrir um arquivo
#variavel_arquivo = open("nome arquivo", "modo")

# r leitura
# r+ leitura e escrivta
# w escrever 
#a append
try:
   variavel_arquivo = open("nome arquivo", "modo")
   print("Abri arquivo com sucesso")
except:
    print("Não deu certo.") 