import base64
import sys

def convert(image):
  with open(image, 'rb') as f:
    data = f.read()

  string = base64.b16encode(data)
  convert = base64.b16decode(string)

  print(string)

  with open('example_16.png', 'w+') as t:
    t.write(convert)

if __name__ == "__main__":
  convert(sys.argv[1])
