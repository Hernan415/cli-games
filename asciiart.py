import requests
import random

data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')
font = random.choice(fontsArray)
print(font)

text = input('ASCII Art Text > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
print(r.text)

data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')

if font == "":
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
  print("Font: default")
  print(r.text)

if font == "random":
  data = requests.get('http://artii.herokuapp.com/fonts_list')
  fontsArray = data.text.split('\n')

for i in range(3):
      font = random.choice(fontsArray)
      r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
      print("Font:", font)
      print(r.text)
