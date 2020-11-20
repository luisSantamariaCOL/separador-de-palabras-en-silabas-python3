# Separador de Palabras en Sílabas, Python 3

def main():
    palabras = ["transgresor", "123", "monstruo", "murcielago", "abecedario", "palabras", "sol",
                "dia", "luna", "idea", "consejo", "enciclopedia", "genio", "mariscal#"]
    for palabra in palabras:
        print(esPalabra(palabra))


# Separa una palabra en silabas
def separarPalabraEnSilabas(palabra):
    return None


# Retorna True si un texto es enteramente una palabra
def esPalabra(texto):
    # EXCEPCIÓN TIPO DE TEXTO INT
    letras_del_texto = list(texto)
    es_palabra = True
    abecedario = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    for i in letras_del_texto:
        if i not in abecedario:
            es_palabra = False
    return es_palabra

# determina si un pedazo de string es una consonante
def esConsonante(texto):
    return True

# Determina si un pedazo de string es una vocal
def esVocal(texto):
    return True

# Determina si dos letras unidas forman un grupo consonantico
def esGrupoConsonantico(consonante1, consonante2):
    return True

# Determina si una letra es una vocal
def esVocalFuerte(vocal):
    return True

if __name__ == "__main__":
    main()