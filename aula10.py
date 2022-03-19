from datetime import date, time , datetime , timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    #pego só oq quero
    print(data_atual.strftime('%H: %M : %S'))
    print(data_atual.strftime('%c'))

    #so o dia ou ano, data
    print(data_atual.day)
    print(data_atual.year)
    #trazendo o dia da semana
    print(data_atual.weekday())
    tupla = ('Segunda' ,'Terca','Quarta','Quinta','Sexta','Sabado','Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2018, 6, 20 , 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019'
    
    ##possoacresentar hora data_string = '01/01/2019 12:20:57'
    #converter data_convertida = datetime.strptime(data_string,'%d/%m/%Y %H:%M:%S')
    data_convertida = datetime.strptime(data_string,'%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))
    print(data_convertida.day)
    #substracao e soma de data com time delta
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)
    ##posso tira o horario
    nova_data = data_convertida - timedelta(days=365, hours= 5)
    print(nova_data)
    #posso tirar o minuto
    nova_data = data_convertida - timedelta(days=365, hours = 6 , minutes = 30)
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = (data_atual.strftime('%A %B %Y'))
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))
def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    #print(type(horario))
    #print(horario.strftime('%H:%M:%S'))
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()