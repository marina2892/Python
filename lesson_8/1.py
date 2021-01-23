class Data:
    def __init__(self,data_str):
        self.data_str = data_str
        
    @classmethod
    def data_str_in_int(cls,d1):
        list1 = d1.data_str.split("-")
        d1.day = int(list1[0])
        d1.month = int(list1[1])
        d1.year = int(list1[2])
        
    @staticmethod
    def valid_data(d1):
        Data.data_str_in_int(d1)
        fl = True
        if not(d1.day >= 1 and d1.day <= 31 and d1.month >= 1 and d1.month <= 12 and d1.year >= 1970 and d1.year <= 2030):
            fl = False
        return fl
        
        
data1 = Data('21-06-2020')
data2 = Data('21-13-2020')
print(Data.valid_data(data1))
print(Data.valid_data(data2))
        
       