'''Programa Um código em Python para percorrer arquivos e subdiretórios de um determinado diretório,
 identificar arquivos e contar o número de vezes que as palavras aparecem nesses arquivos.
As palavras serão então  classificadas com as 10000 principais palavras que ocorrem sendo exibidas
para o usuário'''

#importa biblioteca os do python
import os
import operator

def listdir_fullpath(d):
    #Função para criar o caminho completo do diretório ou arquivo fornecido
    return [os.path.join(d, f) for f in os.listdir(d)]

def getWordFiles(rootDir):
    #Função para recuperar os arquivos txt do diretório fornecido e quaisquer outros subdiretórios
    #Esta função retornará uma lista com os nomes de arquivo de caminho completo de cada arquivo txt
    dirList = [rootDir]
    fileList = []
    while(len(dirList)!=0):
        for i in listdir_fullpath(dirList.pop()):
            if(os.path.isdir(i)):
                dirList.append(i)
            else:
                fileList.append(i)
    return fileList

def countWords(fileList):
    #Função para contar ocorrências de palavras em uma série de arquivos txt fornecidos em uma lista
    #Esta função retornará um dicionário onde a estrutura é {"palavra", número de ocorrências}
    words = {}
    for i in fileList:
        wordFile = open(i, "r+")
        for word in wordFile.read().split():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    return words

def sortWords(wordList):
    #Função para ordenar um dicionário de palavras e suas ocorrências
    #A função irá ordenar as chaves por seus valores e retornar uma lista de tuplas
    # A lista ordenada estará em Ordem Decrescente
    return sorted(wordList.items(), key=operator.itemgetter(1), reverse=True)

def display100000(wordList):
    #Função para exibir as 10000 principais palavras e o número de ocorrências
     #Se houver menos de 10000 palavras em todos os arquivos txt, o número superior x de palavras será exibido com x sendo o número de palavras existentes
    displayCount = 100000
    if (len(wordList)<100000):
        displayCount = len(wordList)

    for i in range(displayCount):
        print( str((i+1))+ ". "+ wordList[i][0] + "("+str(wordList[i][1])+" times)")

#Peça ao usuário o caminho do diretório raiz
#Continue perguntando até que eles forneçam um caminho válido
pathname = ""
while (os.path.isdir(pathname)==False):
    pathname = input('Enter a valid directory path: ')

fileList = getWordFiles(pathname)
words = countWords(fileList)
words = sortWords(words)
display100000(words)