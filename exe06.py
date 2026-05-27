def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    print(contador)


contar_vogais("Você achou que fosse outra pessoa… MAS ERA EU, DIO!")