import pyperclip as pc

text = input("Enter text: ")

words = text.split(" ")
newWords = []

i = 0
for word in words:
    newWord = ""
    for letter in word:
        if i % 2 == 0:
            newWord += letter.upper()
        else:
            newWord += letter.lower()
        if letter.isalpha():
          i += 1
    newWords.append(newWord)

pc.copy(" ".join(newWords))

print("""
      .--..--..--..--..--..--.
    .' \  (`._   (_)     _   \\
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |   {quote}
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\\
             ||       ||
    LGB      ||_.-.   ||_.-.
            (_.--__) (_.--__)
    """.format(quote=" ".join(newWords)))

print('Copied "{quote}" to clipboard'.format(quote=" ".join(newWords)))