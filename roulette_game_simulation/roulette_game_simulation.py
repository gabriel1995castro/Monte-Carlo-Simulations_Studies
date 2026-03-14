#Bibliotecas utilizadas
import numpy as np
import random 
import matplotlib.pyplot as plt

def rolls_dice(playerMoney):
  """
  Simulates the drawing of a number in the roulette game.  
  """
  
  number = random.randint(1,100)

  if number>=1 and number <= 49:
    playerMoney = playerMoney + 1
  
  else:
    playerMoney = playerMoney - 1

  return playerMoney

def simulate_playes(playerMoney,numJogadas):
  
  """
  Simulates the players' moves starting from an initial value.
  """
  saldo_jogadas = []
  saldo_jogadas.append(playerMoney)
  for i in range(numJogadas-1):
    playerMoney = rolls_dice(playerMoney)
    saldo_jogadas.append(playerMoney)
  return saldo_jogadas

if __name__ == "__main__":
    num_jogadas = 1000
    valor_inicial = 100
    num_jogadores = 100
    saldos_finais =[]

    for _ in range(num_jogadores):
        historico = simulate_playes(valor_inicial, num_jogadas)
        saldos_finais.append(historico[-1])
        plt.plot(historico)

    plt.xlabel('Play')
    plt.ylabel('Balance')
    plt.title('Player performance simulation')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(saldos_finais, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

    media = np.mean(saldos_finais)
    plt.axvline(100, color='red', linestyle='--', label='Initial Balance (Equilibrium)')
    plt.axvline(media, color='green', linestyle='-', linewidth=2, label=f'Final Average ({media:.2f})')

    plt.title(f"Final Distribution of {num_jogadores} Players")
    plt.xlabel("Final Balance (R$)")
    plt.ylabel("Number of Players")
    plt.legend()
    plt.show()

