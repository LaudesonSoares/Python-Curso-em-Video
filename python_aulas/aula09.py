frase='Curso em Vídeo Python'
print(frase[::2])

print(frase.upper().count('O'))

print("""We're going to learn operations with strings in Python in this class. 
    The main operations that we're going to see are Slicing, len() analysis, count(), find(), ' \
    transformation using replace(), upper(), lower(), capitalize(), title(), strip(), merging with join().""")

print(len(frase))

print(len(frase.strip()))

print(frase.replace('Python', 'Android'))

frase=frase.replace('Python', 'Android')
print(frase)

print(frase.find('em'))

print(frase.lower().find('curso'))

dividido=frase.split()
print(dividido)
print(dividido[2][3])

print(frase.capitalize())

print(frase.title())