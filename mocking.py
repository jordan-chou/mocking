import os

text = input("Enter text: ")

# copy text to clipboard
# https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard
def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

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

addToClipBoard(" ".join(newWords))

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