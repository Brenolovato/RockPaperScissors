import random

def rock_paper_scissors():
  user = input("Escolha pedra, papel ou tesoura:")
  computer = random.choice(['pedra', 'papel', 'tesoura'])
  print(f"computer escolheu {computer}")

  if user == computer:
    return "Empate!"
  elif(user == "pedra" and computer == "tesoura") or (user == "papel" and computer == "pedra") or (user == "tesoura" and computer == "papel"):
    return "você ganhou!"
  else:
    return "você perdeu!"
   
print (rock_paper_scissors())