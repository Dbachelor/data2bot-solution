import unittest

from tests import *

from data_reader import DataReader

class TestDataReader(unittest.TestCase):
    obj = DataReader()
    def test_dir_exist(self):
        self.assertTrue(True, isDirectoryCreated("data"))
        
    def test_file_dir_empty(self):
        self.assertTrue(True, isDirectoryEmpty('data'))
        
    def isOutputDictionary(self):
        self.assertTrue(True, isDict(self.obj.fileToJson('data/data_1.json')))
        
    def isOutputList(self):
        sample_list = self.obj.fileToJson('data/data_1.json')
        self.assertTrue(True, isList(self.obj.processData(sample_list)))
        

if __name__ == '__main__':
    unittest.main()