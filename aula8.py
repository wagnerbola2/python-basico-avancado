from datetime import datetime

nome = "Roberval"
sobrenome = "Silva"
idade = 35
ano_nascimento = datetime.now().year - idade
maior_de_idade = idade >= 18
altura_metros = 1.65

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_nascimento)
print("É maior de idade?", "sim" if maior_de_idade else "não")
print("Altura em Metros:", altura_metros)