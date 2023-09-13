# Loop para receber e calcular as informações
for i in range (0,10):
  nome = input("Digite o nome do produto: ")
  quantidade = int(input("Digite a quantidade do produto: "))
  preco = float(input("Digite o preço do produto: "))

  total = quantidade * preco

  if quantidade <= 5:
    desconto = 2
  elif quantidade > 5 and quantidade <= 10:
    desconto = 3
  else:
    desconto = 5

  total_pagar = total - (total * (desconto/100))

  # Exibir os resultados
  print ("")
  print("Total: R$", total)
  print("Desconto: {}%".format(desconto))
  print("Total a pagar: R$", total_pagar)