from datetime import datetime

def dias_entre_datas(data1, data2):
    data1 = datetime.strptime(data1, "%d/%m/%Y")
    data2 = datetime.strptime(data2, "%d/%m/%Y")
    return (data2 - data1).days
