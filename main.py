from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('csv\cardbase.png'))
for i in range (14):
  hash1 = imagehash.average_hash(Image.open(f'csv\card{i}.png'))
  cutoff = 20  # maximum bits that could be different between the hashes.

  if hash0 - hash1 < cutoff:
    print(f"imagem{i}", hash1,'imagem é similar')
  else:
    print(f"imagem{i}", hash1,'imagem não é similar')