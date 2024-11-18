from datetime import datetime, timedelta

def adiciona_dias(data, n):
    data = datetime.strptime(data, "%d/%m/%Y")
    nova_data = data + timedelta(days=n)
    return nova_data.strftime("%d/%m/%Y")
