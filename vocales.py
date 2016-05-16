#!usr/bin/env python
def vocales(string):
    if ("A" or "a" or "E" or "e" or "I" or "i" or "O" or "o" or "U" or "u") in string:
        nvocalesami = (string.count("a"))
        nvocalesama = (string.count("A"))
        nvocalesemi = (string.count("e"))
        nvocalesema = (string.count("E"))
        nvocalesimi = (string.count("i"))
        nvocalesima = (string.count("I"))
        nvocalesomi = (string.count("o"))
        nvocalesoma = (string.count("O"))
        nvocalesumi = (string.count("u"))
        nvocalesuma = (string.count("U"))
        part1 = (nvocalesami + nvocalesama + nvocalesemi + nvocalesema + nvocalesimi + nvocalesima)
        part2 = (nvocalesomi + nvocalesoma + nvocalesumi + nvocalesuma)
        todo = (part1 + part2)
        return ("Hay",todo,"vocales en la frase")
    else:
        return("No hay vocales en la frase")
        
print "vocales"

print vocales("7")
