# -*- coding: utf-8 -*-
"""ProjetoCalculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RleX6eOrVxwH_7ZmcSTDfgKXmdyIR3aC
"""

resposta = 1
operacao = 1

while resposta == 1:

  num1 = int(input("Digite o primeiro número:"))
  num2 = int(input("Digite o segundo número:"))

  print("\nEscolha a operação a ser realizada com os números.\n")
  print("1-Adição\n")
  print("2-Subtração\n")
  print("3-Multiplicação\n")
  print("4-Divisão\n")

  operacao = int(input("Operação selecionada:"))

  while operacao < 1 or operacao > 4:
    print("\nCódigo incorreto!! ")
    print("\nInsira um número correspondente ao código da operação a ser realizada!\n")
    print("1-Adição\n")
    print("2-Subtração\n")
    print("3-Multiplicação\n")
    print("4-Divisão\n")

    operacao = int(input("Insira um código válido de operação:"))

  if operacao == 1:
    print("Operação ADIÇÃO selecionada. Resultado:",num1+num2)
  elif operacao == 2:
    print("Operação SUBTRAÇÃO selecionada. Resultado:",num1-num2)
  elif operacao == 3:
    print("Operação MULTIPLICAÇÃO selecionada. Resultado:",num1*num2)
  elif operacao == 4:
    print("Operação DIVISÃO selecionada. Resultado:",num1/num2)

  resposta = int(input("Deseja realizar outro cálculo? 1-Sim/2-Não: "))

  while resposta != 1 and resposta != 2:
    print("Insira um número válido! O código deve ser 1 para Sim e 2 para Não.")
    resposta = int(input("Insira um código válido: "))