# Declarando as variáveis
mun_com_mais_eleitores = ""
eleitores_maximo = 0
eleitores_total = 0

mun_com_mais_brancos = ""
brancos_maximo = 0
brancos_total = 0

mun_com_mais_nulos = ""
nulos_maximo = 0
nulos_total = 0

mun_com_mais_validos = ""
validos_maximo = 0
validos_total = 0


# Loop recebendo as informações e calculando os resultados
for x in range (0,10):
  
  municipio = input("Digite o nome do município: ")
  total_eleitores = int(input("Digite o número total de eleitores: "))
  eleitores_total += total_eleitores
  
  votos_branco = int(input("Digite o número de votos em branco: "))
  brancos_total += votos_branco
  
  votos_nulo = int(input("Digite o número de votos nulos: "))
  nulos_total += votos_nulo
  
  votos_validos = total_eleitores - (votos_branco + votos_nulo)
  validos_total += votos_validos

  porc_branco = (votos_branco/total_eleitores) * 100
  porc_nulos = (votos_nulo/total_eleitores) * 100
  porc_validos = (votos_validos/total_eleitores) * 100

  # Exibir os resultados
  print("")
  print("Município:       ", municipio)
  print("Eleitores:       ", total_eleitores, " ---- 100.00%")
  print("Votos em branco: ", votos_branco, " ----- {:.2f}%".format(porc_branco))
  print("Votos nulos:     ", votos_nulo, " ----- {:.2f}%".format(porc_nulos))
  print("Votos válidos:   ", votos_validos, " ----- {:.2f}%".format(porc_validos))
  print("")
  
  # Calcular o município que possui os maiores dados
  if total_eleitores > eleitores_maximo:
    eleitores_maximo = total_eleitores
    mun_com_mais_eleitores = municipio

  if votos_branco > brancos_maximo:
    brancos_maximo = votos_branco
    mun_com_mais_brancos = municipio
  
  if votos_nulo > nulos_maximo:
    nulos_maximo = votos_nulo
    mun_com_mais_nulos = municipio

  if votos_validos > validos_maximo:
    validos_maximo = votos_validos
    mun_com_mais_validos = municipio

  porc_eleitores_max = (eleitores_maximo  / eleitores_total) * 100
  porc_brancos_max = (brancos_maximo  / brancos_total) * 100
  porc_nulos_max = (nulos_maximo  / nulos_total) * 100
  porc_validos_max = (validos_maximo  / validos_total) * 100

# Exibir os resultados
print("Município com mais eleitores: {} com {} e {:.2f}%".format(mun_com_mais_eleitores, eleitores_maximo, porc_eleitores_max))
print("Município com mais votos em branco: {} com {} e {:.2f}%".format(mun_com_mais_brancos, brancos_maximo, porc_brancos_max))
print("Município com mais votos em nulo: {} com {} e {:.2f}%".format(mun_com_mais_nulos, nulos_maximo, porc_nulos_max))
print("Município com mais votos válidos: {} com {} e {:.2f}%".format(mun_com_mais_validos, validos_maximo, porc_validos_max))
