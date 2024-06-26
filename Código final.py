#Importações utilizadas no código, getpass utilizada para esconder o digito da senha e os nesse caso para quebrar a linha, para ficar mais organizado no console.
from getpass import getpass
import os

#Variaveis dos votos totais dos prefeitos

Total_Votos_Vinicius = 0
Total_Votos_Marcos = 0
Total_Votos_Gabriel = 0
Total_Votos_Fernando = 0
Total_Votos_Branco = 0
Votos_Nulo_Prefeito = 0

#Variaveis dos votos totais dos vereadores

Total_Votos_Marcio = 0
Total_Votos_Joao = 0
Total_Votos_Fabio = 0
Total_Votos_Edgar = 0
Total_Votos_Leticia = 0
Total_Votos_Marilia = 0
Total_Votos_Felipe = 0
Total_Votos_Mateus = 0
Total_Votos_Daniela = 0
Total_Votos_Alan = 0
Votos_Nulo_Vereador = 0

#Variavel utilizada para limitar o loop em 40 vezes e também usada para calcular os ausentes

total = 0

#Variaveis usadas para calcular as pessoas ausentes

Pessoas = 40
Faltas = 0



#Função de inicialização da urna, onde o administrador precisar selecionar a seha 'sim' antecipadamente para iniciar a votação

administrador = getpass('Digite a senha de inicialização da urna: ')
if administrador == 'sim':
        print('votação iniciada')
else:
        while administrador != 'sim':
                administrador = getpass('Digite a senha de inicialização da urna: ')
                if administrador == 'sim':
                        print('votação iniciada')

#Função de repetição do menu de votação, onde o código se repete 40 vezes no total. 

while total < 41:

        #Estrutura que será repetida 40 vezes, a variavel votação serve para começar a etapa de votação, caso digitar 'fim' o coódigo solicitara a senha para encerrar a votação caso o administrador precise encerrar antes dos 40 votantes, com a senha correta utilizada, os resultados serão apresentados.

        votacao = input('para começar sua votação digite qualquer tecla ')
        if votacao == '':
                print('sessão iniciada')
        if votacao == 'fim':

                #variavel senha que é solicitada para encerrar a votação.

                senha = getpass('digite a senha da urna')
                if senha == 'final':
                        if total < 2:
                                Faltas = Pessoas - total
                        print('')
                        print('*' * 80)
                        print('                                [RESULTADOS]                                   *')
                        print('                                                                               *')
                        print(f'O total de pessoas ausentes foram: {Faltas}                                          *')
                        print('----------------------------------------                                       *') 

                        #Tabela de resultados dos votos dos prefeitos, caso a votação seja encerrada antes dos 40 votantes pelo administrador

                        print(
                            f'                        |Tabela de votos prefeitos|                            *{os.linesep}                        ---------------------------                            *{os.linesep}- Total Vinicius: |{Total_Votos_Vinicius}|                                                          *{os.linesep}------------------------                                                       *{os.linesep}- Total Marcos:|{Total_Votos_Marcos}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}- Total Gabriel:|{Total_Votos_Gabriel}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}- Total Fernando:|{Total_Votos_Fernando}|                                                           *{os.linesep}------------------------                                                       *{os.linesep}- Total Nulo: |{Votos_Nulo_Prefeito}|                                                              *'
                        )

                        #sistema de if que mostrará quem foi o vencedor entre os prefeitos, ou se não houver vencedor, mostrará que houve empate ou maior quantidade de nulos

                        if Total_Votos_Vinicius > Total_Votos_Marcos and Total_Votos_Vinicius > Total_Votos_Gabriel and Total_Votos_Vinicius > Total_Votos_Fernando:
                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Vinicius venceu com {Total_Votos_Vinicius} votos|                                                  *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                        elif Total_Votos_Marcos > Total_Votos_Vinicius and Total_Votos_Marcos > Total_Votos_Gabriel and Total_Votos_Marcos > Total_Votos_Fernando:
                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Marcos venceu com {Total_Votos_Marcos} votos|                                                    *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                        elif Total_Votos_Gabriel > Total_Votos_Vinicius and Total_Votos_Gabriel > Total_Votos_Marcos and Total_Votos_Gabriel > Total_Votos_Fernando:
                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Gabriel venceu com {Total_Votos_Gabriel} votos|                                                   *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                        elif Total_Votos_Fernando > Total_Votos_Vinicius and Total_Votos_Fernando > Total_Votos_Marcos and Total_Votos_Fernando > Total_Votos_Gabriel:
                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Fernando venceu com {Total_Votos_Fernando} votos|                                                  *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                        elif Votos_Nulo_Prefeito > Total_Votos_Vinicius and Votos_Nulo_Prefeito > Total_Votos_Marcos and Votos_Nulo_Prefeito > Total_Votos_Gabriel and Votos_Nulo_Prefeito > Total_Votos_Fernando:
                                print('                                                                               *')
                                print('-------------------------------------------------------------------------      *')
                                print(f'|A quantidade de nulos foi maior que as dos candidatos a prefeito com {Votos_Nulo_Prefeito} votos| *')
                                print('-------------------------------------------------------------------------      *')
                                print('                                                                               *')
                        else:
                                print('                                                                               *')
                                print('------------------------------------------------------------------------       *')
                                print('|houve um empate e deverá ser feito um segundo turno entre os prefeitos|       *')
                                print('------------------------------------------------------------------------       *')
                                print('                                                                               *')
                        #Tabela de resultados dos votos dos vereadores, caso a votação seja encerrada antes dos 40 votantes pelo administrador

                        print(
                            f'                        |Tabela de votos vereadores|                           *{os.linesep}                        ----------------------------                           *{os.linesep}-Total Marcio: |{Total_Votos_Marcio}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total João: |{Total_Votos_Joao}|                                                               *{os.linesep}------------------------                                                       *{os.linesep}-Total Fabio: |{Total_Votos_Fabio}|                                                              *{os.linesep}------------------------                                                       *{os.linesep}-Total Edgar: |{Total_Votos_Edgar}|                                                              *{os.linesep}------------------------                                                       *{os.linesep}-Total Leticia: |{Total_Votos_Leticia}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Marilia: |{Total_Votos_Marilia}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Felipe: |{Total_Votos_Felipe}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total Mateus: |{Total_Votos_Mateus}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total Daniela: |{Total_Votos_Daniela}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Alan: |{Total_Votos_Alan}|                                                               *{os.linesep}------------------------                                                       *{os.linesep}-Total Nulos: |{Votos_Nulo_Vereador}|                                                              *'
                        )
                        #sistema de if que mostrará quem foi o vencedor entre os vereadores, ou se não houver vencedor, mostrará que houve empate ou maior quantidade de nulos
                        if Total_Votos_Marcio > Total_Votos_Joao and Total_Votos_Marcio > Total_Votos_Fabio and Total_Votos_Marcio > Total_Votos_Edgar and Total_Votos_Marcio > Total_Votos_Leticia and Total_Votos_Marcio > Total_Votos_Marilia and Total_Votos_Marcio > Total_Votos_Felipe and Total_Votos_Marcio > Total_Votos_Mateus and Total_Votos_Marcio > Total_Votos_Daniela and Total_Votos_Marcio > Total_Votos_Alan and Total_Votos_Marcio > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Marcio venceu com {Total_Votos_Marcio} votos|                                                    *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Joao > Total_Votos_Marcio and Total_Votos_Joao > Total_Votos_Fabio and Total_Votos_Joao > Total_Votos_Edgar and Total_Votos_Joao > Total_Votos_Leticia and Total_Votos_Joao > Total_Votos_Marilia and Total_Votos_Joao > Total_Votos_Felipe and Total_Votos_Joao > Total_Votos_Mateus and Total_Votos_Joao > Total_Votos_Daniela and Total_Votos_Joao > Total_Votos_Alan and Total_Votos_Joao > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|João venceu com {Total_Votos_Joao} votos|                                                      *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Fabio > Total_Votos_Marcio and Total_Votos_Fabio > Total_Votos_Joao and Total_Votos_Fabio > Total_Votos_Edgar and Total_Votos_Fabio > Total_Votos_Leticia and Total_Votos_Fabio > Total_Votos_Marilia and Total_Votos_Fabio > Total_Votos_Felipe and Total_Votos_Fabio > Total_Votos_Mateus and Total_Votos_Fabio > Total_Votos_Daniela and Total_Votos_Fabio > Total_Votos_Alan and Total_Votos_Fabio > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Fabio venceu com {Total_Votos_Fabio} votos|                                                     *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Edgar > Total_Votos_Marcio and Total_Votos_Edgar > Total_Votos_Joao and Total_Votos_Edgar > Total_Votos_Fabio and Total_Votos_Edgar > Total_Votos_Leticia and Total_Votos_Edgar > Total_Votos_Marilia and Total_Votos_Edgar > Total_Votos_Felipe and Total_Votos_Edgar > Total_Votos_Mateus and Total_Votos_Edgar > Total_Votos_Daniela and Total_Votos_Edgar > Total_Votos_Alan:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Edgar venceu com {Total_Votos_Edgar} votos|                                                     *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Leticia > Total_Votos_Marcio and Total_Votos_Leticia > Total_Votos_Joao and Total_Votos_Leticia > Total_Votos_Fabio and Total_Votos_Leticia > Total_Votos_Edgar and Total_Votos_Leticia > Total_Votos_Marilia and Total_Votos_Leticia > Total_Votos_Felipe and Total_Votos_Leticia > Total_Votos_Mateus and Total_Votos_Leticia > Total_Votos_Daniela and Total_Votos_Leticia > Total_Votos_Alan and Total_Votos_Leticia > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Leticia venceu com {Total_Votos_Leticia} votos|                                                   *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Marilia > Total_Votos_Marcio and Total_Votos_Marilia > Total_Votos_Joao and Total_Votos_Marilia > Total_Votos_Fabio and Total_Votos_Marilia > Total_Votos_Edgar and Total_Votos_Marilia > Total_Votos_Leticia and Total_Votos_Marilia > Total_Votos_Felipe and Total_Votos_Marilia > Total_Votos_Mateus and Total_Votos_Marilia > Total_Votos_Daniela and Total_Votos_Marilia > Total_Votos_Alan:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Marilia venceu com {Total_Votos_Marilia} votos|                                                   *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Felipe > Total_Votos_Marcio and Total_Votos_Felipe > Total_Votos_Joao and Total_Votos_Felipe > Total_Votos_Fabio and Total_Votos_Felipe > Total_Votos_Edgar and Total_Votos_Felipe > Total_Votos_Leticia and Total_Votos_Felipe > Total_Votos_Marilia and Total_Votos_Felipe > Total_Votos_Mateus and Total_Votos_Felipe > Total_Votos_Daniela and Total_Votos_Felipe > Total_Votos_Alan and Total_Votos_Felipe > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Felipe venceu com {Total_Votos_Felipe} votos|                                                    *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Mateus > Total_Votos_Marcio and Total_Votos_Mateus > Total_Votos_Joao and Total_Votos_Mateus > Total_Votos_Fabio and Total_Votos_Mateus > Total_Votos_Edgar and Total_Votos_Mateus > Total_Votos_Leticia and Total_Votos_Mateus > Total_Votos_Marilia and Total_Votos_Mateus > Total_Votos_Felipe and Total_Votos_Mateus > Total_Votos_Daniela and Total_Votos_Mateus > Total_Votos_Alan and Total_Votos_Mateus > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Mateus venceu com {Total_Votos_Mateus} votos|                                                    *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Daniela > Total_Votos_Marcio and Total_Votos_Daniela > Total_Votos_Joao and Total_Votos_Daniela > Total_Votos_Fabio and Total_Votos_Daniela > Total_Votos_Edgar and Total_Votos_Daniela > Total_Votos_Leticia and Total_Votos_Daniela > Total_Votos_Marilia and Total_Votos_Daniela > Total_Votos_Felipe and Total_Votos_Daniela > Total_Votos_Mateus and Total_Votos_Daniela > Total_Votos_Alan and Total_Votos_Daniela > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Daniela venceu com {Total_Votos_Daniela} votos|                                                   *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Alan > Total_Votos_Marcio and Total_Votos_Alan > Total_Votos_Joao and Total_Votos_Alan > Total_Votos_Fabio and Total_Votos_Alan > Total_Votos_Edgar and Total_Votos_Alan > Total_Votos_Leticia and Total_Votos_Alan > Total_Votos_Marilia and Total_Votos_Alan > Total_Votos_Felipe and Total_Votos_Alan > Total_Votos_Mateus and Total_Votos_Alan > Total_Votos_Daniela and Total_Votos_Alan > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Alan venceu com {Total_Votos_Alan} votos|                                                      *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Votos_Nulo_Vereador > Total_Votos_Marcio and Votos_Nulo_Vereador > Total_Votos_Joao and Votos_Nulo_Vereador > Total_Votos_Fabio and Votos_Nulo_Vereador > Total_Votos_Edgar and Votos_Nulo_Vereador > Total_Votos_Leticia and Votos_Nulo_Vereador > Total_Votos_Marilia and Votos_Nulo_Vereador > Total_Votos_Felipe and Votos_Nulo_Vereador > Total_Votos_Mateus and Votos_Nulo_Vereador > Total_Votos_Daniela and Votos_Nulo_Vereador > Total_Votos_Alan:

                                print('                                                                               *')
                                print('-'*80)
                                print(f'|A quantidade de nulos foi maior que as dos candidatos a candidatos com {Votos_Nulo_Vereador} votos|')
                                print('-'*80)
                                print('                                                                               *')
                                print('*' * 80)
                        else:

                                print('                                                                               *')
                                print('-------------------------------------------------------------------------      *')
                                print('|houve um empate e deverá ser feito um segundo turno entre os vereadores|      *')
                                print('-------------------------------------------------------------------------      *')
                                print('                                                                               *')
                                print('*' * 80)
                        break
                #caso a senha seja digitada incorretamente, esse sistema fará com o que o código volte para o início
                if senha != 'final':
                        print('senha incorreta - voltando ao inicio')
                        continue

        #Sistema de if que faz a contagem de votos dos prefeitos, por exemplo: caso o usuário digite o número 10, o sistema fará com que o usuário vote no candidato Vinicius, caso digite qualquer número que não seja dos prefeitos, será contabilizado como voto nulo

        Votosprefeitos = int(input(
                f'Digita o numero do seu Prefeito?{os.linesep}10 - Vinicius{os.linesep}12 - Marcos{os.linesep}14 - Gabriel{os.linesep}16 - Fernando{os.linesep}Outros - Nulo{os.linesep} Digite seu Voto: '
            ))

        if Votosprefeitos == 10:
                Total_Votos_Vinicius += 1
        if Votosprefeitos == 12:
                Total_Votos_Marcos += 1
        if Votosprefeitos == 14:
                Total_Votos_Gabriel += 1
        if Votosprefeitos == 16:
                Total_Votos_Fernando += 1
        if Votosprefeitos != 10 and Votosprefeitos != 12 and Votosprefeitos != 14 and Votosprefeitos != 16:
                Votos_Nulo_Prefeito += 1

        #Sistema de if que faz a contagem de votos dos vereadores, por exemplo: caso o usuário digite o número 10000, o sistema fará com que o usuário vote no candidato Marcio, caso digite qualquer número que não seja dos prefeitos, será contabilizado como voto nulo, também será contabilizada a variavel total em todas elas, para que seja feito a contagem de pessoas votantes.

        Votos_vereadores = int(input(
                f'Digite o numero do seu Vereador?{os.linesep}10000 - Marcio {os.linesep}10001 - João {os.linesep}10002 - Fabio {os.linesep}10003 - Edgar {os.linesep}10004 - Leticia {os.linesep}10005 - Marilia {os.linesep}10006 - Felipe {os.linesep}10007 - Mateus {os.linesep}10008 - Daniela {os.linesep}10009 - Alan {os.linesep}Outro - Nulo {os.linesep}Digite seu Voto: '
            ))

        if Votos_vereadores == 10000:
                Total_Votos_Marcio += 1
                total += 1
        if Votos_vereadores == 10001:
                Total_Votos_Joao += 1
                total += 1
        if Votos_vereadores == 10002:
                Total_Votos_Fabio += 1
                total += 1
        if Votos_vereadores == 10003:
                Total_Votos_Edgar += 1
                total += 1
        if Votos_vereadores == 10004:
                Total_Votos_Leticia += 1
                total += 1
        if Votos_vereadores == 10005:
                Total_Votos_Marilia += 1
                total += 1
        if Votos_vereadores == 10006:
                Total_Votos_Felipe += 1
                total += 1
        if Votos_vereadores == 10007:
                Total_Votos_Mateus += 1
                total += 1
        if Votos_vereadores == 10008:
                Total_Votos_Daniela += 1
                total += 1
        if Votos_vereadores == 10009:
                Total_Votos_Alan += 1
                total += 1
        if Votos_vereadores != 10000 and Votos_vereadores != 10001 and Votos_vereadores != 10002 and Votos_vereadores != 10003 and Votos_vereadores != 10004 and Votos_vereadores != 10005 and Votos_vereadores != 10006 and Votos_vereadores != 10007 and Votos_vereadores != 10008 and Votos_vereadores != 10009:
                Votos_Nulo_Vereador += 1
                total += 1
        #Caso seja atingida a quantidade total de votantes, o sistema irá encerrar a votação automaticamente, solicitando a senha para o administrador, caso a senha seja digitada corretamente, o sistema  mostra o resultado, mas se a senha for digitada incorretamente o sistema solicitara a senha novamamente e assim sucessivamente.
        if total == 40:    
                #senha solicitada para encerramento da votação
                senha = getpass('Digite a senha para encerrar a votação: ')
                if senha == 'final':

                        #Tabela de resultados dos votos dos prefeitos, caso a votação seja encerrada automaticamente após os 40 votantes, o sistema irá mostrar o resultado da votação, após a senha ser digitada corretamente.
                                print('*' * 80)
                                print('                                [RESULTADOS]                                   *')
                                print('                                                                               *')
                                print(f'O total de pessoas ausentes foram: {Faltas}                                           *')
                                print('----------------------------------------                                       *') 
                                print(
                                    f'                        |Tabela de votos prefeitos|                            *{os.linesep}                        ---------------------------                            *{os.linesep}- Total Vinicius: |{Total_Votos_Vinicius}|                                                          *{os.linesep}------------------------                                                       *{os.linesep}- Total Marcos:|{Total_Votos_Marcos}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}- Total Gabriel:|{Total_Votos_Gabriel}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}- Total Fernando:|{Total_Votos_Fernando}|                                                           *{os.linesep}------------------------                                                       *{os.linesep}- Total Nulo: |{Votos_Nulo_Prefeito}|                                                              *'
                                )

                                if Total_Votos_Vinicius > Total_Votos_Marcos and Total_Votos_Vinicius > Total_Votos_Gabriel and Total_Votos_Vinicius > Total_Votos_Fernando:
                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Vinicius venceu com {Total_Votos_Vinicius} votos|                                                  *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                elif Total_Votos_Marcos > Total_Votos_Vinicius and Total_Votos_Marcos > Total_Votos_Gabriel and Total_Votos_Marcos > Total_Votos_Fernando:
                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Marcos venceu com {Total_Votos_Marcos} votos|                                                    *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                elif Total_Votos_Gabriel > Total_Votos_Vinicius and Total_Votos_Gabriel > Total_Votos_Marcos and Total_Votos_Gabriel > Total_Votos_Fernando:
                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Gabriel venceu com {Total_Votos_Gabriel} votos|                                                   *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                elif Total_Votos_Fernando > Total_Votos_Vinicius and Total_Votos_Fernando > Total_Votos_Marcos and Total_Votos_Fernando > Total_Votos_Gabriel:
                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Fernando venceu com {Total_Votos_Fernando} votos|                                                  *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                elif Votos_Nulo_Prefeito > Total_Votos_Vinicius and Votos_Nulo_Prefeito > Total_Votos_Marcos and Votos_Nulo_Prefeito > Total_Votos_Gabriel and Votos_Nulo_Prefeito > Total_Votos_Fernando:
                                        print('                                                                               *')
                                        print('-------------------------------------------------------------------------      *')
                                        print(f'|A quantidade de nulos foi maior que as dos candidatos a prefeito com {Votos_Nulo_Prefeito} votos| *')
                                        print('-------------------------------------------------------------------------      *')
                                        print('                                                                               *')
                                else:
                                        print('                                                                               *')
                                        print('------------------------------------------------------------------------       *')
                                        print('|houve um empate e deverá ser feito um segundo turno entre os prefeitos|       *')
                                        print('------------------------------------------------------------------------       *')
                                        print('                                                                               *')

                        #Tabela de resultados dos votos dos vereadores, caso a votação seja encerrada automaticamente após os 40 votantes, o sistema irá mostrar o resultado da votação, após a senha ser digitada corretamente.

                                print(
                                    f'                        |Tabela de votos vereadores|                           *{os.linesep}                        ----------------------------                           *{os.linesep}-Total Marcio: |{Total_Votos_Marcio}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total João: |{Total_Votos_Joao}|                                                               *{os.linesep}------------------------                                                       *{os.linesep}-Total Fabio: |{Total_Votos_Fabio}|                                                              *{os.linesep}------------------------                                                       *{os.linesep}-Total Edgar: |{Total_Votos_Edgar}|                                                              *{os.linesep}------------------------                                                       *{os.linesep}-Total Leticia: |{Total_Votos_Leticia}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Marilia: |{Total_Votos_Marilia}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Felipe: |{Total_Votos_Felipe}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total Mateus: |{Total_Votos_Mateus}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total Daniela: |{Total_Votos_Daniela}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Alan: |{Total_Votos_Alan}|                                                               *{os.linesep}------------------------                                                       *{os.linesep}-Total Nulos: |{Votos_Nulo_Vereador}|                                                              *'
                                )
                                if Total_Votos_Marcio > Total_Votos_Joao and Total_Votos_Marcio > Total_Votos_Fabio and Total_Votos_Marcio > Total_Votos_Edgar and Total_Votos_Marcio > Total_Votos_Leticia and Total_Votos_Marcio > Total_Votos_Marilia and Total_Votos_Marcio > Total_Votos_Felipe and Total_Votos_Marcio > Total_Votos_Mateus and Total_Votos_Marcio > Total_Votos_Daniela and Total_Votos_Marcio > Total_Votos_Alan and Total_Votos_Marcio > Votos_Nulo_Vereador:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Marcio venceu com {Total_Votos_Marcio} votos|                                                    *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Joao > Total_Votos_Marcio and Total_Votos_Joao > Total_Votos_Fabio and Total_Votos_Joao > Total_Votos_Edgar and Total_Votos_Joao > Total_Votos_Leticia and Total_Votos_Joao > Total_Votos_Marilia and Total_Votos_Joao > Total_Votos_Felipe and Total_Votos_Joao > Total_Votos_Mateus and Total_Votos_Joao > Total_Votos_Daniela and Total_Votos_Joao > Total_Votos_Alan and Total_Votos_Joao > Votos_Nulo_Vereador:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|João venceu com {Total_Votos_Joao} votos|                                                      *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Fabio > Total_Votos_Marcio and Total_Votos_Fabio > Total_Votos_Joao and Total_Votos_Fabio > Total_Votos_Edgar and Total_Votos_Fabio > Total_Votos_Leticia and Total_Votos_Fabio > Total_Votos_Marilia and Total_Votos_Fabio > Total_Votos_Felipe and Total_Votos_Fabio > Total_Votos_Mateus and Total_Votos_Fabio > Total_Votos_Daniela and Total_Votos_Fabio > Total_Votos_Alan and Total_Votos_Fabio > Votos_Nulo_Vereador:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Fabio venceu com {Total_Votos_Fabio} votos|                                                     *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Edgar > Total_Votos_Marcio and Total_Votos_Edgar > Total_Votos_Joao and Total_Votos_Edgar > Total_Votos_Fabio and Total_Votos_Edgar > Total_Votos_Leticia and Total_Votos_Edgar > Total_Votos_Marilia and Total_Votos_Edgar > Total_Votos_Felipe and Total_Votos_Edgar > Total_Votos_Mateus and Total_Votos_Edgar > Total_Votos_Daniela and Total_Votos_Edgar > Total_Votos_Alan:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Edgar venceu com {Total_Votos_Edgar} votos|                                                     *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Leticia > Total_Votos_Marcio and Total_Votos_Leticia > Total_Votos_Joao and Total_Votos_Leticia > Total_Votos_Fabio and Total_Votos_Leticia > Total_Votos_Edgar and Total_Votos_Leticia > Total_Votos_Marilia and Total_Votos_Leticia > Total_Votos_Felipe and Total_Votos_Leticia > Total_Votos_Mateus and Total_Votos_Leticia > Total_Votos_Daniela and Total_Votos_Leticia > Total_Votos_Alan and Total_Votos_Leticia > Votos_Nulo_Vereador:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Leticia venceu com {Total_Votos_Leticia} votos|                                                   *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Marilia > Total_Votos_Marcio and Total_Votos_Marilia > Total_Votos_Joao and Total_Votos_Marilia > Total_Votos_Fabio and Total_Votos_Marilia > Total_Votos_Edgar and Total_Votos_Marilia > Total_Votos_Leticia and Total_Votos_Marilia > Total_Votos_Felipe and Total_Votos_Marilia > Total_Votos_Mateus and Total_Votos_Marilia > Total_Votos_Daniela and Total_Votos_Marilia > Total_Votos_Alan:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Marilia venceu com {Total_Votos_Marilia} votos|                                                   *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Felipe > Total_Votos_Marcio and Total_Votos_Felipe > Total_Votos_Joao and Total_Votos_Felipe > Total_Votos_Fabio and Total_Votos_Felipe > Total_Votos_Edgar and Total_Votos_Felipe > Total_Votos_Leticia and Total_Votos_Felipe > Total_Votos_Marilia and Total_Votos_Felipe > Total_Votos_Mateus and Total_Votos_Felipe > Total_Votos_Daniela and Total_Votos_Felipe > Total_Votos_Alan and Total_Votos_Felipe > Votos_Nulo_Vereador:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Felipe venceu com {Total_Votos_Felipe} votos|                                                    *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Mateus > Total_Votos_Marcio and Total_Votos_Mateus > Total_Votos_Joao and Total_Votos_Mateus > Total_Votos_Fabio and Total_Votos_Mateus > Total_Votos_Edgar and Total_Votos_Mateus > Total_Votos_Leticia and Total_Votos_Mateus > Total_Votos_Marilia and Total_Votos_Mateus > Total_Votos_Felipe and Total_Votos_Mateus > Total_Votos_Daniela and Total_Votos_Mateus > Total_Votos_Alan and Total_Votos_Mateus > Votos_Nulo_Vereador:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Mateus venceu com {Total_Votos_Mateus} votos|                                                    *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Daniela > Total_Votos_Marcio and Total_Votos_Daniela > Total_Votos_Joao and Total_Votos_Daniela > Total_Votos_Fabio and Total_Votos_Daniela > Total_Votos_Edgar and Total_Votos_Daniela > Total_Votos_Leticia and Total_Votos_Daniela > Total_Votos_Marilia and Total_Votos_Daniela > Total_Votos_Felipe and Total_Votos_Daniela > Total_Votos_Mateus and Total_Votos_Daniela > Total_Votos_Alan and Total_Votos_Daniela > Votos_Nulo_Vereador:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Daniela venceu com {Total_Votos_Daniela} votos|                                                   *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Total_Votos_Alan > Total_Votos_Marcio and Total_Votos_Alan > Total_Votos_Joao and Total_Votos_Alan > Total_Votos_Fabio and Total_Votos_Alan > Total_Votos_Edgar and Total_Votos_Alan > Total_Votos_Leticia and Total_Votos_Alan > Total_Votos_Marilia and Total_Votos_Alan > Total_Votos_Felipe and Total_Votos_Alan > Total_Votos_Mateus and Total_Votos_Alan > Total_Votos_Daniela and Total_Votos_Alan > Votos_Nulo_Vereador:

                                        print('                                                                               *')
                                        print('----------------------------------------------------------------------         *')
                                        print(f'|Alan venceu com {Total_Votos_Alan} votos|                                                      *')
                                        print('----------------------------------------------------------------------         *')
                                        print('                                                                               *')
                                        print('*' * 80)

                                elif Votos_Nulo_Vereador > Total_Votos_Marcio and Votos_Nulo_Vereador > Total_Votos_Joao and Votos_Nulo_Vereador > Total_Votos_Fabio and Votos_Nulo_Vereador > Total_Votos_Edgar and Votos_Nulo_Vereador > Total_Votos_Leticia and Votos_Nulo_Vereador > Total_Votos_Marilia and Votos_Nulo_Vereador > Total_Votos_Felipe and Votos_Nulo_Vereador > Total_Votos_Mateus and Votos_Nulo_Vereador > Total_Votos_Daniela and Votos_Nulo_Vereador > Total_Votos_Alan:

                                        print('                                                                               *')
                                        print('-'*80)
                                        print(f'|A quantidade de nulos foi maior que as dos candidatos a candidatos com {Votos_Nulo_Vereador} votos|')
                                        print('-'*80)
                                        print('                                                                               *')
                                        print('*' * 80)
                                else:

                                        print('                                                                               *')
                                        print('-------------------------------------------------------------------------      *')
                                        print('|houve um empate e deverá ser feito um segundo turno entre os vereadores|      *')
                                        print('-------------------------------------------------------------------------      *')
                                        print('                                                                               *')
                                        print('*' * 80)
                                break
                while senha != 'final':
                        print('senha incorreta')
                        senha = getpass('Digite a senha para encerrar a votação: ')
                        continue
                if senha == 'final':

                        #sistema de if que mostrará quem foi o vencedor entre os vereadores, ou se não houver vencedor, mostrará que houve empate ou maior quantidade de nulos

                        print('*' * 80)
                        print('                                [RESULTADOS]                                   *')
                        print('                                                                               *')
                        print(f'O total de pessoas ausentes foram: {Faltas}                                           *')
                        print('----------------------------------------                                       *') 
                        print(
                            f'                        |Tabela de votos prefeitos|                            *{os.linesep}                        ---------------------------                            *{os.linesep}- Total Vinicius: |{Total_Votos_Vinicius}|                                                          *{os.linesep}------------------------                                                       *{os.linesep}- Total Marcos:|{Total_Votos_Marcos}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}- Total Gabriel:|{Total_Votos_Gabriel}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}- Total Fernando:|{Total_Votos_Fernando}|                                                           *{os.linesep}------------------------                                                       *{os.linesep}- Total Nulo: |{Votos_Nulo_Prefeito}|                                                              *'
                        )
                        #sistema de if que mostrará quem foi o vencedor entre os prefeitos, ou se não houver vencedor, mostrará que houve empate ou maior quantidade de nulos

                        if Total_Votos_Vinicius > Total_Votos_Marcos and Total_Votos_Vinicius > Total_Votos_Gabriel and Total_Votos_Vinicius > Total_Votos_Fernando:
                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Vinicius venceu com {Total_Votos_Vinicius} votos|                                                  *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                        elif Total_Votos_Marcos > Total_Votos_Vinicius and Total_Votos_Marcos > Total_Votos_Gabriel and Total_Votos_Marcos > Total_Votos_Fernando:
                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Marcos venceu com {Total_Votos_Marcos} votos|                                                    *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                        elif Total_Votos_Gabriel > Total_Votos_Vinicius and Total_Votos_Gabriel > Total_Votos_Marcos and Total_Votos_Gabriel > Total_Votos_Fernando:
                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Gabriel venceu com {Total_Votos_Gabriel} votos|                                                   *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                        elif Total_Votos_Fernando > Total_Votos_Vinicius and Total_Votos_Fernando > Total_Votos_Marcos and Total_Votos_Fernando > Total_Votos_Gabriel:
                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Fernando venceu com {Total_Votos_Fernando} votos|                                                  *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                        elif Votos_Nulo_Prefeito > Total_Votos_Vinicius and Votos_Nulo_Prefeito > Total_Votos_Marcos and Votos_Nulo_Prefeito > Total_Votos_Gabriel and Votos_Nulo_Prefeito > Total_Votos_Fernando:
                                print('                                                                               *')
                                print('-------------------------------------------------------------------------      *')
                                print(f'|A quantidade de nulos foi maior que as dos candidatos a prefeito com {Votos_Nulo_Prefeito} votos| *')
                                print('-------------------------------------------------------------------------      *')
                                print('                                                                               *')
                        else:
                                print('                                                                               *')
                                print('------------------------------------------------------------------------       *')
                                print('|houve um empate e deverá ser feito um segundo turno entre os prefeitos|       *')
                                print('------------------------------------------------------------------------       *')
                                print('                                                                               *')
                        print(
                            f'                        |Tabela de votos vereadores|                           *{os.linesep}                        ----------------------------                           *{os.linesep}-Total Marcio: |{Total_Votos_Marcio}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total João: |{Total_Votos_Joao}|                                                               *{os.linesep}------------------------                                                       *{os.linesep}-Total Fabio: |{Total_Votos_Fabio}|                                                              *{os.linesep}------------------------                                                       *{os.linesep}-Total Edgar: |{Total_Votos_Edgar}|                                                              *{os.linesep}------------------------                                                       *{os.linesep}-Total Leticia: |{Total_Votos_Leticia}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Marilia: |{Total_Votos_Marilia}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Felipe: |{Total_Votos_Felipe}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total Mateus: |{Total_Votos_Mateus}|                                                             *{os.linesep}------------------------                                                       *{os.linesep}-Total Daniela: |{Total_Votos_Daniela}|                                                            *{os.linesep}------------------------                                                       *{os.linesep}-Total Alan: |{Total_Votos_Alan}|                                                               *{os.linesep}------------------------                                                       *{os.linesep}-Total Nulos: |{Votos_Nulo_Vereador}|                                                              *'
                        )
                        #sistema de if que mostrará quem foi o vencedor entre os vereadores, ou se não houver vencedor, mostrará que houve empate ou maior quantidade de nulos

                        if Total_Votos_Marcio > Total_Votos_Joao and Total_Votos_Marcio > Total_Votos_Fabio and Total_Votos_Marcio > Total_Votos_Edgar and Total_Votos_Marcio > Total_Votos_Leticia and Total_Votos_Marcio > Total_Votos_Marilia and Total_Votos_Marcio > Total_Votos_Felipe and Total_Votos_Marcio > Total_Votos_Mateus and Total_Votos_Marcio > Total_Votos_Daniela and Total_Votos_Marcio > Total_Votos_Alan and Total_Votos_Marcio > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Marcio venceu com {Total_Votos_Marcio} votos|                                                    *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Joao > Total_Votos_Marcio and Total_Votos_Joao > Total_Votos_Fabio and Total_Votos_Joao > Total_Votos_Edgar and Total_Votos_Joao > Total_Votos_Leticia and Total_Votos_Joao > Total_Votos_Marilia and Total_Votos_Joao > Total_Votos_Felipe and Total_Votos_Joao > Total_Votos_Mateus and Total_Votos_Joao > Total_Votos_Daniela and Total_Votos_Joao > Total_Votos_Alan and Total_Votos_Joao > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|João venceu com {Total_Votos_Joao} votos|                                                      *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Fabio > Total_Votos_Marcio and Total_Votos_Fabio > Total_Votos_Joao and Total_Votos_Fabio > Total_Votos_Edgar and Total_Votos_Fabio > Total_Votos_Leticia and Total_Votos_Fabio > Total_Votos_Marilia and Total_Votos_Fabio > Total_Votos_Felipe and Total_Votos_Fabio > Total_Votos_Mateus and Total_Votos_Fabio > Total_Votos_Daniela and Total_Votos_Fabio > Total_Votos_Alan and Total_Votos_Fabio > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Fabio venceu com {Total_Votos_Fabio} votos|                                                     *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Edgar > Total_Votos_Marcio and Total_Votos_Edgar > Total_Votos_Joao and Total_Votos_Edgar > Total_Votos_Fabio and Total_Votos_Edgar > Total_Votos_Leticia and Total_Votos_Edgar > Total_Votos_Marilia and Total_Votos_Edgar > Total_Votos_Felipe and Total_Votos_Edgar > Total_Votos_Mateus and Total_Votos_Edgar > Total_Votos_Daniela and Total_Votos_Edgar > Total_Votos_Alan:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Edgar venceu com {Total_Votos_Edgar} votos|                                                     *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Leticia > Total_Votos_Marcio and Total_Votos_Leticia > Total_Votos_Joao and Total_Votos_Leticia > Total_Votos_Fabio and Total_Votos_Leticia > Total_Votos_Edgar and Total_Votos_Leticia > Total_Votos_Marilia and Total_Votos_Leticia > Total_Votos_Felipe and Total_Votos_Leticia > Total_Votos_Mateus and Total_Votos_Leticia > Total_Votos_Daniela and Total_Votos_Leticia > Total_Votos_Alan and Total_Votos_Leticia > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Leticia venceu com {Total_Votos_Leticia} votos|                                                   *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Marilia > Total_Votos_Marcio and Total_Votos_Marilia > Total_Votos_Joao and Total_Votos_Marilia > Total_Votos_Fabio and Total_Votos_Marilia > Total_Votos_Edgar and Total_Votos_Marilia > Total_Votos_Leticia and Total_Votos_Marilia > Total_Votos_Felipe and Total_Votos_Marilia > Total_Votos_Mateus and Total_Votos_Marilia > Total_Votos_Daniela and Total_Votos_Marilia > Total_Votos_Alan:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Marilia venceu com {Total_Votos_Marilia} votos|                                                   *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Felipe > Total_Votos_Marcio and Total_Votos_Felipe > Total_Votos_Joao and Total_Votos_Felipe > Total_Votos_Fabio and Total_Votos_Felipe > Total_Votos_Edgar and Total_Votos_Felipe > Total_Votos_Leticia and Total_Votos_Felipe > Total_Votos_Marilia and Total_Votos_Felipe > Total_Votos_Mateus and Total_Votos_Felipe > Total_Votos_Daniela and Total_Votos_Felipe > Total_Votos_Alan and Total_Votos_Felipe > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Felipe venceu com {Total_Votos_Felipe} votos|                                                    *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Mateus > Total_Votos_Marcio and Total_Votos_Mateus > Total_Votos_Joao and Total_Votos_Mateus > Total_Votos_Fabio and Total_Votos_Mateus > Total_Votos_Edgar and Total_Votos_Mateus > Total_Votos_Leticia and Total_Votos_Mateus > Total_Votos_Marilia and Total_Votos_Mateus > Total_Votos_Felipe and Total_Votos_Mateus > Total_Votos_Daniela and Total_Votos_Mateus > Total_Votos_Alan and Total_Votos_Mateus > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Mateus venceu com {Total_Votos_Mateus} votos|                                                    *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Daniela > Total_Votos_Marcio and Total_Votos_Daniela > Total_Votos_Joao and Total_Votos_Daniela > Total_Votos_Fabio and Total_Votos_Daniela > Total_Votos_Edgar and Total_Votos_Daniela > Total_Votos_Leticia and Total_Votos_Daniela > Total_Votos_Marilia and Total_Votos_Daniela > Total_Votos_Felipe and Total_Votos_Daniela > Total_Votos_Mateus and Total_Votos_Daniela > Total_Votos_Alan and Total_Votos_Daniela > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Daniela venceu com {Total_Votos_Daniela} votos|                                                   *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Total_Votos_Alan > Total_Votos_Marcio and Total_Votos_Alan > Total_Votos_Joao and Total_Votos_Alan > Total_Votos_Fabio and Total_Votos_Alan > Total_Votos_Edgar and Total_Votos_Alan > Total_Votos_Leticia and Total_Votos_Alan > Total_Votos_Marilia and Total_Votos_Alan > Total_Votos_Felipe and Total_Votos_Alan > Total_Votos_Mateus and Total_Votos_Alan > Total_Votos_Daniela and Total_Votos_Alan > Votos_Nulo_Vereador:

                                print('                                                                               *')
                                print('----------------------------------------------------------------------         *')
                                print(f'|Alan venceu com {Total_Votos_Alan} votos|                                                      *')
                                print('----------------------------------------------------------------------         *')
                                print('                                                                               *')
                                print('*' * 80)

                        elif Votos_Nulo_Vereador > Total_Votos_Marcio and Votos_Nulo_Vereador > Total_Votos_Joao and Votos_Nulo_Vereador > Total_Votos_Fabio and Votos_Nulo_Vereador > Total_Votos_Edgar and Votos_Nulo_Vereador > Total_Votos_Leticia and Votos_Nulo_Vereador > Total_Votos_Marilia and Votos_Nulo_Vereador > Total_Votos_Felipe and Votos_Nulo_Vereador > Total_Votos_Mateus and Votos_Nulo_Vereador > Total_Votos_Daniela and Votos_Nulo_Vereador > Total_Votos_Alan:

                                print('                                                                               *')
                                print('-'*80)
                                print(f'|A quantidade de nulos foi maior que as dos candidatos a candidatos com {Votos_Nulo_Vereador} votos|')
                                print('-'*80)
                                print('                                                                               *')
                                print('*' * 80)
                        else:

                                print('                                                                               *')
                                print('-------------------------------------------------------------------------      *')
                                print('|houve um empate e deverá ser feito um segundo turno entre os vereadores|      *')
                                print('-------------------------------------------------------------------------      *')
                                print('                                                                               *')
                                print('*' * 80)
                break
