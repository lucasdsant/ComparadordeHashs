from PIL import Image
import imagehash
hashbase = imagehash.average_hash(Image.open('csv\cardbase.png'))
for i in range (14):
  hashdosUsers = imagehash.average_hash(Image.open(f'csv\card{i}.png'))
  Tolerancia = 20  #  quantidade maxima de bits que podem ser diferentes entre os hashes.

  if hashbase - hashdosUsers < Tolerancia:
    print(f"imagem{i}", hashdosUsers,'esta imagem é similar, portanto foi aprovada!')
  else:
    print(f"imagem{i}", hashdosUsers,'imagem não é similar, portanto não foi aprovada!')