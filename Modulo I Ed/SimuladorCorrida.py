import random
from collections import Counter
import heapq


class Setor:
    def __init__(self, nome, distancia_km, desgaste_pneu):
        self.nome = nome
        self.distancia = distancia_km
        self.desgaste = desgaste_pneu

    def gerar_desgaste(self):
        desgaste = random.uniform(
            self.desgaste * 0.8, self.desgaste * 1.2)
        return round(desgaste, 2)


Setores = [
    Setor("Hatzenbach", 2.0, 0.8),
    Setor("Hocheichen", 1.2, 1.1),
    Setor("Flugplatz", 2.1, 0.6),
    Setor("Aremberg", 2.4, 1.2),
    Setor("Fuchsröhre", 1.9, 1.3),
    Setor("Adenauer Forst", 2.0, 0.9),
    Setor("Kallenhard", 2.2, 1.4),
    Setor("Wehrseifen", 1.7, 1.6),
    Setor("Karussell", 2.3, 1.8),
    Setor("Döttinger Höhe", 2.7, 0.5)
]


class Equipe:
    def __init__(self, nome_equipe, pilotos, tempo_medio, num_equipe):
        self.nome_equipe = nome_equipe
        self.pilotos = pilotos
        self.piloto_atual = 0
        self.tempo_medio = tempo_medio
        self.num_equipe = num_equipe
        self.tempo_total = 0
        self.voltas_completas = 0
        self.tempo_piloto = 0
        self.estado_pneu = "Novo"
        self.tempo_stint = 0
        self.voltas_stint = 0

    def trocar_piloto(self):
        self.piloto_atual = (self.piloto_atual + 1) % len(self.pilotos)
        self.tempo_stint = 0
        self.voltas_stint = 0
        print(
            f"🔄 Troca de piloto! Novo piloto: {self.pilotos[self.piloto_atual]}")

    def piloto_stint(self):
        return self.pilotos[self.piloto_atual]

    def consultar_estado_pneu(self):
        if self.voltas_stint <= 5:
            self.estado_pneu = "Novo"
        elif self.voltas_stint <= 10:
            self.estado_pneu = "Gasto"
        else:
            self.estado_pneu = "Muito Gasto"

    def situação_atual(todas_equipes, minha_equipe):
        minha_posição = buscar_equipe(todas_equipes, "ROWE RACING")
        print(f"P1: {todas_equipes[0]}")
        print(f"P2: {todas_equipes[1]}")
        print(f"P3: {todas_equipes[2]}")
        print(f"Estamos em: {minha_posição}")

    def simular_volta(self, Setores):
        variacao = random.uniform(0.95, 1.05)
        tempo_volta = self.tempo_medio * variacao
        self.tempo_total += tempo_volta
        self.tempo_stint += tempo_volta
        self.tempo_piloto += tempo_volta
        self.voltas_completas += 1
        self.voltas_stint += 1
        self.consultar_estado_pneu()
        for Setor in Setores:
            desgaste = Setor.gerar_desgaste()
            aux = Setor.desgaste

            if desgaste <= aux * 0.9:
                alertas.append(
                    f"Scuderia: {self.nome_equipe} | Volta: {self.voltas_completas} | Piloto: {self.pilotos[self.piloto_atual]} | Setor: {Setor.nome} | BAIXO DESGASTE DE PNEUS")

            elif aux * 0.9 < desgaste <= aux * 1.1:
                alertas.append(
                    f"Scuderia: {self.nome_equipe} | Volta: {self.voltas_completas} | Piloto: {self.pilotos[self.piloto_atual]} | Setor: {Setor.nome} | MEDIO DESGASTE DE PNEUS")

            else:
                alertas.append(
                    f"Scuderia: {self.nome_equipe} | Volta: {self.voltas_completas} | Piloto: {self.pilotos[self.piloto_atual]} | Setor: {Setor.nome} | ALTO DESGASTE DE PNEUS")

        return round(tempo_volta, 3)


equipe1 = Equipe("ROWE RACING", ["Augusto Farfus",
                                 "Jesse Krohn", "Raffaele Marciello"], 483, 98)
equipe2 = Equipe(
    "Manthey EMA", ["Kévin Estre", "Ayhancan Güven", "Thomas Preining"], 494, 911)
equipe3 = Equipe("Dinamic GT SRL", [
                 "Buus Bastian", "Matteo Cairoli", "Loek Hartog"], 488, 54)
equipe4 = Equipe("HRT Ford Performance", ["Patrick Assenheimer",
                                          "Vincent Kolb", "Dirk Müller"], 495, 65)
equipe5 = Equipe("ABT Sportsline", ["Marco Mapelli",
                                    "Christian Engelhart", "Luca Engstler"], 502, 28)
equipe6 = Equipe("Eastalent Racing Team", ["Christian Klien",
                                           "Norbert Siedler", "Max Hofer"], 499, 84)
equipe7 = Equipe("PROsport Racing GmbH", ["Steven Palette",
                                          "Marek Böckmann", "Nico Bastian"], 492, 37)
equipe8 = Equipe("Konrad Motorsport GmbH", ["Danny Soufi",
                                            "Maximilian Paul", "Peter Elkmann"], 489, 7)
equipe9 = Equipe("Hankook Competition Europe", ["Jongkyum Kim",
                                                "Roelof Bruins", "Steven Cho"], 500, 55)
equipe10 = Equipe("Renazzo Motorsport Team", ["Christoph Breuer",
                                              "Thomas Mutsch", "Dieter Schmidtmann"], 498, 786)

todas_equipes = [equipe1, equipe2, equipe3, equipe4,
                 equipe5, equipe6, equipe7, equipe8, equipe9, equipe10]


def formatar_tempo(segundos):
    minutos = int(segundos // 60)
    segundos_restantes = segundos % 60
    return f"{minutos}:{segundos_restantes:06.3f}"


def buscar_equipe(lista, nome):
    for i in range(len(lista)):
        if lista[i].nome_equipe == nome:
            return i
    return -1


def rabin_karp_busca(texto, padrao):
    d = 256
    q = 101
    m = len(padrao)
    n = len(texto)
    hpadrao = 0
    htexto = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        hpadrao = (d * hpadrao + ord(padrao[i])) % q
        htexto = (d * htexto + ord(texto[i])) % q

    for i in range(n - m + 1):
        if hpadrao == htexto and texto[i:i + m] == padrao:
            return True
        if i < n - m:
            htexto = (d * (htexto - ord(texto[i]) * h) + ord(texto[i + m])) % q
            if htexto < 0:
                htexto += q
    return False


def simular_corrida(todas_equipes, minha_equipe):
    for equipe in todas_equipes:
        equipe.simular_volta(Setores)

    todas_equipes.sort(key=lambda x: x.tempo_total)
    minha_posicao = buscar_equipe(todas_equipes, "ROWE RACING")
    minha_scuderia = todas_equipes[minha_posicao]

    print("\n --------------------------------------------------")
    print(
        f"Volta {minha_scuderia.voltas_completas} - Equipe: {minha_scuderia.nome_equipe}")
    print(f"Piloto atual: {minha_scuderia.piloto_stint()}")
    print(
        f"Tempo de stint atual: {formatar_tempo(minha_scuderia.tempo_stint)}")
    print(f"Voltas com o mesmo pneu: {minha_scuderia.voltas_stint}")
    print(f"Estado dos pneus: {minha_scuderia.estado_pneu}")

    if minha_posicao > 0:
        frente = todas_equipes[minha_posicao - 1]
        distancia = minha_scuderia.tempo_total - frente.tempo_total
        print(
            f"Piloto à frente: {frente.nome_equipe} ({frente.piloto_stint()}) - {formatar_tempo(distancia)} à frente")

    if minha_posicao < len(todas_equipes) - 1:
        atras = todas_equipes[minha_posicao + 1]
        distancia = atras.tempo_total - minha_scuderia.tempo_total
        print(
            f"Piloto Atrás: {atras.nome_equipe} ({atras.piloto_stint()}) - {formatar_tempo(distancia)} atrás")
        print("\n --------------------------------------------------")


def situação_atual(todas_equipes, minha_equipe):
    posicao = buscar_equipe(todas_equipes, "ROWE RACING")
    print("\n --------------------------------------------------")
    print(
        f"P1: {todas_equipes[0].nome_equipe} | ({todas_equipes[0].piloto_stint()})")
    print(
        f"P2: {todas_equipes[1].nome_equipe} | ({todas_equipes[1].piloto_stint()})")
    print(
        f"P3: {todas_equipes[2].nome_equipe} | ({todas_equipes[2].piloto_stint()})")
    print(f"Estamos em: {posicao + 1}")
    print("\n --------------------------------------------------")


alertas = []
voltas = []


def menu():
    op = 0
    while op != 8:
        print("=====24H NURBURGRING NORDSCHLEIFE=====")
        print("[1]-Simular Volta.(BS)")
        print("[2]-Opções de Estrategia.")
        print("[3]-Opções de Pilotos.")
        print("[4]-Acompanhar Alertas(RK).")
        print("[5]-Estado do carro.")
        print("[6]-Situação atual da corrida(BB).")
        print("[7]-Codificar Dados(HFM)")
        print("[8]-Sair")
        op = int(input("Selecione uma opção: "))

        if op == 1:
            # OCORRE A BUSCA SEQUENCIAL PARA ACHAR MINHA EQUIPE, E PEGAR OS DADOS NECESSARIOS
            print("\n====SIMULANDO VOLTA====\n")

            simular_corrida(todas_equipes, "ROWE RACING")

            # Mostrar alertas de desgaste de pneu, alerta de pitstop, atualizar tempo de Stint, ver como ta sendo feito a questao de pilotos a frente e atras
            # mostrar tipo de pneu,(Quando o pneu for mais duro tem q durar mais tempo)
            # Acrescentar a opção de mostrar Fatest Lap (Busca Binaria)
            # OLHAR POSSIBILIDADE DE COLOCAR ALERTA NESSE MODELO (DESGASTE ALTO DE PNEUS SETOR 1 (NOME DO SETOR))
            # POSSIBILIDADE DE COLOCAR JANELA DE PITSTOP

        # Ira mostrar os dados do piloto(Nome), atual setor que o piloto esta, pilotos a frente, voltas gerais e voltas do piloto,
        # situação do carro e pneus, tempo de volta, tempo medio, distancia do carro da frente e do carro atras por volta
        # Deve gerar um alerta quando o piloto chegar a 5-7 voltas(Macio) 7-10(Medio) 10-12(Duro)
        # Deve simular de alguma forma batidas, bandeiras amarelas gerando alertas, podendo alterar a estrategio (Piloto vai
        # pro box na volta 7 porem na volta 4 deu bandeira amaerela ele vai entrar na volta 5).
        # simula tambem a situação dos outros carros.

        elif op == 2:
            print("===ESTRATEGIA===")
            op = 0
            while op != 6:
                print("[1]-Pitstop ")
                print("[2]-Pilotos ")
                print("[3]-Pneus ")
                print("[4]-Ataque ou Defesa ")
                print("[5]-Previsão do tempo ")
                print("[6]-Voltar ")
                op = input(int)("Selecione uma opção: ")

                # if op == 1:

                # Vai abrir um submenu (PitStop, Pilotos, pneus, ataque/defesa, chuva/seca)
                # PitStop: Deve analisar o tempo do piloto atras e ver se compensa fazer o pitstop ou arriscar abrir mais tempo (Tempo de pit 3:10)
                # Analisar chance da outra equipe parar.
                # Pilotos: Analisar pilotos da equipe adversaria, escolher piloto (Deve mostrar o tempo medio deles), mostrar se o piloto
                # ta liberado ou nao.
                # Pneus: Analisar quantidade de pneus, identificar melhor pneu possivel de acordo com (Se vai atacar ou defender, se
                # esta chovendo ou nao), analise de voltas(Se a equipe parou uma volta antes e colocou pneus macios, podemos tentar colocar
                # medio e ficar 2 voltas a mais na pista)
                # Ataque/Defesa: Ataque=Mais desgaste, Defesa= Desgaste medio, cosntancia=Desgaste normal.
                # Chuva/Seca: Analise do clima

        elif op == 3:
            print("===PILOTOS===")
        # Deve abrir um menu com as seguinte informações Tempo medio de volta, desgaste de pneus (Alto, Medio , Baixo),Total de
        # voltas, stints, total de horas pilotando.

        elif op == 4:
            op = 0
            # OCORRE A BUSCA POR TEXTO PARA MOSTRAR ALERTAS DE BAIXA, MEDIO OU ALTO DESGASTE
            print("===ALERTAS===")
            print("[1]-Baixo desgaste")
            print("[2]-Medio Desgaste")
            print("[3]-Alto Desgaste")
            op = int(input("Selecione uma opção: "))

            palavra_chave = " "

            if op == 1:
                palavra_chave = "BAIXO DESGASTE DE PNEUS"

            elif op == 2:
                palavra_chave = "MEDIO DESGASTE DE PNEUS"

            elif op == 3:
                palavra_chave = "ALTO DESGASTE DE PNEUS"

            for linha in alertas:
                if "ROWE RACING" in linha and rabin_karp_busca(linha, palavra_chave):
                    print({linha})

        # Deve mostrar alertas graves (Alto desgaste de pneus, tempo muito lento em uma setor, problema critico no carro)
        # Alertas normais (Bandeira amerela, tempo amarelo em setor,etc..)
        elif op == 5:
            print("===Estado do carro===")
        # Atraves de alertas pode analisar se o motor ta com superaquecimento, se tem alguma asa danificada, pneus, gasolina

        elif op == 6:
            # OOCORRE A BUSCA BINARIA PARA MOSTRAR QUEM TA EM PRIMEIRO, SEGUNDO E EM TERCEIRO.
            print("===Situação Atual===")
            situação_atual(todas_equipes, "ROWE RACING")

    # Mostrar P1;P2;P3 a nossa posição atual, (Caso nao estejamos no top3, mostrar carro a frente e a carro atras como tempo
    # pra cada um).

        elif op == 7:


if __name__ == "__main__":
    menu()


# COMENTARIOS EM GERAL

# Adicionar o desgaste de pneus por setor(Caso um setor apresente um grande desgaste gera um alerta: ("Alto Desgaste de Pneu no setor: xxxxxxxx"))
# Adicionar o aumento no tempo de volta dependendo do pneu escolhido (Pneu Vermelho: mais rapido , Amarelo: Mais lento, Branco: Mais lento ainda)
# Adicionar a opção de consultar a volta mais rapida(Busca Binaria)
# Adicionar a opção de consultar alertas(Busca por texto)(Sera necessario salvar os alertas e certos dados(Volta,Piloto,Setor, Stint, Estrategia (Ataque/Defesa)))
# Revisao os quistios para definir o tempo de volta de cada equipe, e o desgaste do pneu
# Revisar a forma de mostrar
