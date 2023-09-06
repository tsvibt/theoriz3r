def Write(file, text):
    with open(file, 'w') as f:
        f.write(text)

def Read(file):
   with open(file, 'r') as f:
      t = f.read()
   return t


