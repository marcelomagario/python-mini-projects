# This is my spelling phonetic program where the user will enter a word that needs to be spelled.
# The program will show every code word according to NATO Phonetic Alphabetic.
# Autor: Marcelo Magario

dicionario = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
              'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
              'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
              'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
              'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
              'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
              'Y': 'Yankee', 'Z': 'Zulu', '': ''}

print('-' * 25)
print('SPELLING PHONETIC PROGRAM')
print('-' * 25)
palavra = str(input('Type the word you want to spell: '))
palavra = palavra.upper()

for i in range(len(palavra)):
    print(f"{palavra[i]} as in {dicionario[palavra[i]]}")

