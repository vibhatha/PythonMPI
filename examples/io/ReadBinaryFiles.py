import struct
filename = '/home/vibhatha/github/dsc-spidal-forks/applications/fungi-gene-sequence/data/distance-matrix.bin'
decoded = []
with open(filename,"rb") as f:
     while True:
          try:
             decoded.append(struct.unpack_from("<Q",f.read(1)))
             # `<` means little endian; `Q` means unsigned long long (8 bytes)
          except struct.error:
             break

print decoded
