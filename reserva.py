class Hotel:
    def __init__(self, reserva, hospede):
        self.reserv = reserva
        self.hosp = hospede


    def buscarReserva:
        if numReserva in reserva:


        else:
            print("Reserva não encontrada")

class Hospede:
    def __init__(self, nome, sobrenome, email, contato, dtcheckin, dtcheckout, qtpessoas, quarto, pagamento):
        self.name = nome
        self.sn = sobrenome
        self.em = email
        self.cont = contato
        self.checkin = dtcheckin
        self.checkout = dtcheckout
        self.qtpess = qtpessoas
        self.quart = quarto
        self.pagament = pagamento


numReserva = int(input("Número da reserva"))
nomeHospede = input("Nome do cliente")
nome = input("Informe o seu nome:")
sobrenome = input("Informe o seu sobrenome:")
email = input("Informe seu email:")
contato = input("Informe o nº de contato")

hospede1 = Hotel(numReserva, nomeHospede)
hospede1 = Hospede()





