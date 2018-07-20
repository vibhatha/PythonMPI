import sys
sys.path.append('/home/vibhatha/github/bio/PythonMPI')
from api import Constant
from api import FileRead

class ReadBinFile:

    def read(self):
        filepath = Constant.Constant().DISTANCE_MATRIX_PATH
        fileReader = FileRead.FileRead()
        content = fileReader.read(filepath=filepath)
        length = fileReader.lenth(filepath=filepath)
        arr = fileReader.get_array_from_csv(filepath=filepath)
        return content, length, arr




readBinFile = ReadBinFile()
content, length, arr = readBinFile.read()
print(length)
print(arr.shape)

