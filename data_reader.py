import json

class DataReader:
    
    def run(self, sourceFile="data_1.json", destinationFile="schema_1.json"):
        data = self.fileToJson("data/"+sourceFile)
        output = self.processData(data)
        self.writeTofile("schema/"+destinationFile, output)
        return 1
        


    def fileToJson(self, path):
        f = open(path)
        data = json.load(f)
        return data

    def processData(self, data):
        final_output = {}
        for item in data['message']:
            output = {}
            data_type = ''
            
            match self.getDataType(data['message'][item]):
                case 'dict':
                    data_type = 'enum'
                case 'list':
                    data_type = 'array'
                case 'str':
                    data_type = 'string'
                case 'int' | 'float':
                    data_type = 'integer'
                
            if (data_type != ''):
                output = {item:{"type": data_type, "tag": "", "description": "","required": False}}
                final_output.update(output)
        return final_output
                    
        
    def getDataType(self,item):
        ss = str(type(item))
        d = ss.split("'")[1]
        print(d, item)
        return d.strip()
        
    def writeTofile(self, path, data):
        f = open(path, "w")
        #f.write(json.dumps(data))
        json.dump(data, f, indent = 4)

