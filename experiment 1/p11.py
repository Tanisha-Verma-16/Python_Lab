alpha = input("Enter the alphabet : ")
if alpha.lower() in list('aeiou'):
    print(f"{alpha} is a vowel")
else:
    print(f'{alpha} is a consonent')