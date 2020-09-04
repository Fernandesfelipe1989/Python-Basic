from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)


def trabalhando_com_time():
    horario= time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))
    print(type(horario))
    pass


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    tupla = ('Segunda', 'Terça', 'Quarta', "Quinta", 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string,'%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(timedelta(days=365, hours=2)+1))
    pass


if __name__ =='__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()