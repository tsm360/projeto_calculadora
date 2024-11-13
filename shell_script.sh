#!/bin/bash

#verificando atualizações no usuário
sudo apt-get update

#instalando o python
sudo apt install python3

#interagindo com o usuário
echo "Inicializando a calculadora..."

#rodando o código python da calculadora
python3 projetocalculadora.py

#interagindo com o usuário
echo "Finalizando a calculadora..."
