'''13 de janeiro de 2025
   23h34min. Noite chuvosa'''

'''DESAFIO 002: Faça um programa que leia o nome de uma pessoa e mostre uma
mensagem de boas-vindas.'''

import os
os.system('cls') or None

'''Usando o operador + para fazer a junção da variável com a vírgula.'''
print('Primeira solução:')
nome = 'Gustavo'
print(nome + ',', 'seja bem vindo!\n')

'''Usando a resposta do Curso:'''
print('Segunda solução:')
nome2 = input('Digite o seu nome: ')
print('É um prazer te conhecer, {}'.format(nome),'\n')