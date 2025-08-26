import heapq
from collections import Counter
import random
from collections import deque
import sys

INFINITO = sys.maxsize


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
            f"Troca de piloto! Novo piloto: {self.pilotos[self.piloto_atual]}")

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
            f"Piloto a frente: {frente.nome_equipe} ({frente.piloto_stint()}) - {formatar_tempo(distancia)} à frente")

    if minha_posicao < len(todas_equipes) - 1:
        atras = todas_equipes[minha_posicao + 1]
        distancia = atras.tempo_total - minha_scuderia.tempo_total
        print(
            f"Piloto Atras: {atras.nome_equipe} ({atras.piloto_stint()}) - {formatar_tempo(distancia)} atrás")
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


class NoHuffman:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.esq = None
        self.dir = None

    def __lt__(self, outro):
        return self.freq < outro.freq


def construir_arvore(frequencias):
    heap = [NoHuffman(char, freq) for char, freq in frequencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        no1 = heapq.heappop(heap)
        no2 = heapq.heappop(heap)
        novo = NoHuffman(None, no1.freq + no2.freq)
        novo.esq = no1
        novo.dir = no2
        heapq.heappush(heap, novo)

    return heap[0]


def gerar_codigo(raiz, prefixo="", codigos={}):
    if raiz is None:
        return
    if raiz.char is not None:
        codigos[raiz.char] = prefixo
    gerar_codigo(raiz.esq, prefixo + "0", codigos)
    gerar_codigo(raiz.dir, prefixo + "1", codigos)
    return codigos


def codificar(texto, codigos):
    return "".join(codigos[char] for char in texto)


def descomprimir(texto_codificado, raiz):
    resultado = ""
    no = raiz
    for bit in texto_codificado:
        no = no.esq if bit == "0" else no.dir
        if no.char:
            resultado += no.char
            no = raiz
    return resultado


def comprimir_alertas(alertas):
    texto = "\n".join(alertas)
    frequencias = Counter(texto)
    raiz = construir_arvore(frequencias)
    codigos = gerar_codigo(raiz)
    texto_codificado = codificar(texto, codigos)
    return texto, texto_codificado, raiz


tabela_hash_mul = [None] * 20
tabela_hash_mei = [None] * 20


def hash_multiplicacao(k, m):
    A = 0.6180339887
    k_num = sum(ord(c) for c in k)
    return int(m * ((k_num * A) % 1))


def hash_meio_quadrado(k, m):
    k_num = sum(ord(c) for c in k)
    quadrado = k_num ** 2
    meio = str(quadrado).zfill(8)
    inicio = len(meio) // 2 - 1
    fim = inicio + 2
    extrato = int(meio[inicio:fim])
    return extrato % m


def inserir_em_ambas_tabelas(chave, valor):
    m = len(tabela_hash_mul)

    pos1 = hash_multiplicacao(chave, m)
    if tabela_hash_mul[pos1] is None:
        tabela_hash_mul[pos1] = []
        tabela_hash_mul[pos1].append((chave, valor))

    pos2 = hash_meio_quadrado(chave, m)
    if tabela_hash_mei[pos2] is None:
        tabela_hash_mei[pos2] = []
    tabela_hash_mei[pos2].append((chave, valor))


def buscar_hash_padrão(chave):
    m = len(tabela_hash_mul)
    pos = hash_multiplicacao(chave, m)
    if tabela_hash_mul[pos]:
        for k, v in tabela_hash_mul[pos]:
            if k == chave:
                return v
    return None


class GrafoCorrida:
    def __init__(self, setores):
        self.setores = setores
        self.num_setores = len(setores)
        self.nomes_setores = [s.nome for s in setores]

        self.matriz_adj = self._gerar_matriz_adj()
        self.lista_adj = self._gerar_lista_adj()

    def _gerar_matriz_adj(self):
        matriz = [[0] * self.num_setores for _ in range(self.num_setores)]
        for i in range(self.num_setores):
            proximo_setor = (i + 1) % self.num_setores
            matriz[i][proximo_setor] = 1
        return matriz

    def _gerar_lista_adj(self):
        lista = {setor.nome: [] for setor in self.setores}
        for i, setor in enumerate(self.setores):
            proximo_setor_idx = (i + 1) % self.num_setores
            proximo_setor = self.setores[proximo_setor_idx]
            peso = setor.distancia
            lista[setor.nome].append((proximo_setor.nome, peso))
        return lista

    def adicionar_rota(self, setor_a, setor_b, peso=1):
        if setor_a in self.nomes_setores and setor_b in self.nomes_setores:
            idx_a = self.nomes_setores.index(setor_a)
            idx_b = self.nomes_setores.index(setor_b)

            self.matriz_adj[idx_a][idx_b] = peso
            self.lista_adj[setor_a].append((setor_b, peso))
            print(f"Rota de {setor_a} para {setor_b} adicionada.")
        else:
            print("Setor(es) não encontrado(s).")

    def remover_rota(self, setor_a, setor_b):
        if setor_a in self.nomes_setores and setor_b in self.nomes_setores:
            idx_a = self.nomes_setores.index(setor_a)
            idx_b = self.nomes_setores.index(setor_b)

            self.matriz_adj[idx_a][idx_b] = 0

            self.lista_adj[setor_a] = [
                (s, p) for s, p in self.lista_adj[setor_a] if s != setor_b
            ]
            print(f"Rota de {setor_a} para {setor_b} removida.")
        else:
            print("Setor(es) não encontrado(s).")

    def visualizar_representacoes(self):
        print("=====MATRIZ DE ADJACÊNCIA=====")
        cabecalho = " " * 15 + \
            " ".join([f"{s[:10]:<10}" for s in self.nomes_setores])
        print(cabecalho)
        for i, nome_setor in enumerate(self.nomes_setores):
            linha = f"{nome_setor[:10]:<15}" + \
                " ".join([f"{val:<10}" for val in self.matriz_adj[i]])
            print(linha)

        print("\n--- LISTA DE ADJACÊNCIAS ---")
        for setor, vizinhos in self.lista_adj.items():
            vizinhos_str = ", ".join(
                [f"({v}, peso: {p})" for v, p in vizinhos])
            print(f"{setor}: {vizinhos_str}")

    def dfs(self, inicio):
        visitados = set()
        caminho = []
        stack = [inicio]

        while stack:
            vertice = stack.pop()
            if vertice not in visitados:
                caminho.append(vertice)
                visitados.add(vertice)
                for vizinho, _ in sorted(self.lista_adj.get(vertice, []), reverse=True):
                    if vizinho not in visitados:
                        stack.append(vizinho)
        return caminho

    def bfs(self, inicio):
        visitados = set()
        caminho = []
        fila = deque([inicio])
        visitados.add(inicio)

        while fila:
            vertice = fila.popleft()
            caminho.append(vertice)
            for vizinho, _ in sorted(self.lista_adj.get(vertice, [])):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
        return caminho

    def dijkstra(self, inicio):
        distancias = {setor: INFINITO for setor in self.nomes_setores}
        distancias[inicio] = 0
        caminho = {setor: None for setor in self.nomes_setores}
        heap = [(0, inicio)]

        while heap:
            dist_atual, vertice_atual = heapq.heappop(heap)

            if dist_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.lista_adj.get(vertice_atual, []):
                distancia = dist_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    caminho[vizinho] = vertice_atual
                    heapq.heappush(heap, (distancia, vizinho))
        return distancias, caminho

    def welch_powell_coloracao(self):
        num_vertices = self.num_setores
        graus = {v: len(self.lista_adj[v]) for v in self.nomes_setores}
        vertices_ordenados = sorted(
            graus, key=graus.get, reverse=True)
        cores = {}
        disponibilidade_cores = set(range(num_vertices))

        for vertice in vertices_ordenados:
            cores_vizinhos = set()
            for vizinho, _ in self.lista_adj.get(vertice, []):
                if vizinho in cores:
                    cores_vizinhos.add(cores[vizinho])

            cor_disponivel = min(
                disponibilidade_cores - cores_vizinhos)
            cores[vertice] = cor_disponivel
        return cores

    def ordenacao_topologica_kahn(self):
        graus_entrada = {v: 0 for v in self.nomes_setores}
        for v in self.lista_adj:
            for vizinho, _ in self.lista_adj[v]:
                graus_entrada[vizinho] += 1

        fila = deque([v for v in self.nomes_setores if graus_entrada[v] == 0])
        ordenacao = []

        while fila:
            u = fila.popleft()
            ordenacao.append(u)

            for v, _ in self.lista_adj[u]:
                graus_entrada[v] -= 1
                if graus_entrada[v] == 0:
                    fila.append(v)

        if len(ordenacao) == self.num_setores:
            return ordenacao
        else:
            return None


def menu():
    grafo_corrida = GrafoCorrida(Setores)
    op = 0
    while op != 10:
        print("=====24H NURBURGRING NORDSCHLEIFE=====")
        print("[1]-Simular Volta.(BS)")
        print("[2]-Opções de Estrategia.")
        print("[3]-Opções de Pilotos.")
        print("[4]-Acompanhar Alertas(RK).")
        print("[5]-Estado do carro.")
        print("[6]-Situação atual da corrida(BB).")
        print("[7]-Codificar Dados(HFM)")
        print("[8]-Informações")
        print("[9]-Mapeamento(Grafos).")
        print("[10]-Sair")
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
                op = int(input("Selecione uma opção: "))

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
            print("\n===ALERTAS===\n")
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
                    print(linha)

        # Deve mostrar alertas graves (Alto desgaste de pneus, tempo muito lento em uma setor, problema critico no carro)
        # Alertas normais (Bandeira amerela, tempo amarelo em setor,etc..)
        elif op == 5:
            print("===Estado do carro===")
        # Atraves de alertas pode analisar se o motor ta com superaquecimento, se tem alguma asa danificada, pneus, gasolina

        elif op == 6:
            print("\n===Situação Atual===\n")
            situação_atual(todas_equipes, "ROWE RACING")

    # Mostrar P1;P2;P3 a nossa posição atual, (Caso nao estejamos no top3, mostrar carro a frente e a carro atras como tempo

        elif op == 7:
            print("\n===CODIFICAR DADOS===\n")

            texto, codificado, raiz = comprimir_alertas(alertas)
            print(f"Dados Originiais: {len(texto)} caracteres")
            print(f"Dados Comprimidos: {len(codificado)} bits")

            recuperado = descomprimir(codificado, raiz)
            if texto == recuperado:
                print("Descompressão verificada com sucesso.")
            else:
                print("Erro ao descomprimir!")

        elif op == 8:
            print("\n===INFORMAÇÕES===")
            print("[1]-Guardar Informações")
            print("[2]-Buscar Informações")
            op = int(input("Selecione uma opção: "))
            if op == 1:
                chave = input(
                    "Digite a chave (ex: V4S7): ").strip().upper()
                valor = input("Digite o Informação: ").strip()
                inserir_em_ambas_tabelas(chave, valor)
            elif op == 2:
                chave = input("Digite a chave para buscar: ").strip().upper()
                resultado = buscar_hash_padrão(chave)
                if resultado:
                    print(f"Informação {chave}: {resultado}")
                else:
                    print("Informação nao encontrada.")

        elif op == 9:
            print("\n===MAPEAMENTO===\n")
            print("[1] - Visualizar o Mapa (Matriz e Lista)")
            print("[2] - Explorar a Pista (DFS)")
            print("[3] - Propagar um Alerta (BFS)")
            print("[4] - Calcular a Rota de Menor Desgaste (Dijkstra)")
            print("[5] - Otimização utilizando Coloração (Welch-Powell)")
            op = int(input("Selecione uma opção: "))

            if op == 1:
                grafo_corrida.visualizar_representacoes()

            elif op == 2:
                print("\n===EXPLORANDO A PISTA (DFS)===\n")
                inicio = input("Setor de partida: ").strip()
                if inicio in grafo_corrida.nomes_setores:
                    caminho = grafo_corrida.dfs(inicio)
                    print("Caminho de exploração (DFS):")
                    print(" -> ".join(caminho))

            elif op == 3:
                print("\n===PROPAGAÇÃO DE ALERTA (BFS)===\n")
                inicio = input("Setor onde o alerta foi detectado: ").strip()
                if inicio in grafo_corrida.nomes_setores:
                    caminho_propagacao = grafo_corrida.bfs(inicio)
                    print(" -> ".join(caminho_propagacao))

            elif op == 4:
                print("\n===CALCULANDO A MELHOR ROTA DE PNEUS (DIJKSTRA)===\n")
                inicio = input("Setor de partida: ").strip()
                if inicio in grafo_corrida.nomes_setores:
                    distancias, caminho = grafo_corrida.dijkstra(inicio)
                    for setor, dist in distancias.items():
                        print(
                            f"  - Setor {setor}: {dist:.2f}")

            elif op == 5:
                print("\n===OTIMIZAÇÃO DE PNEUS E ESTRATEGIA (WELCH-POWELL)===\n")
                cores_setores = grafo_corrida.welch_powell_coloracao()
                for setor, cor in cores_setores.items():
                    print(f"  - Setor {setor}: Cor {cor}")


if __name__ == "__main__":
    menu()


# COMENTARIOS EM GERAL

# Adicionar o desgaste de pneus por setor(Caso um setor apresente um grande desgaste gera um alerta: ("Alto Desgaste de Pneu no setor: xxxxxxxx"))
# Adicionar o aumento no tempo de volta dependendo do pneu escolhido (Pneu Vermelho: mais rapido , Amarelo: Mais lento, Branco: Mais lento ainda)
# Adicionar a opção de consultar a volta mais rapida(Busca Binaria)
# Adicionar a opção de consultar alertas(Busca por texto)(Sera necessario salvar os alertas e certos dados(Volta,Piloto,Setor, Stint, Estrategia (Ataque/Defesa)))
# Revisao os quistios para definir o tempo de volta de cada equipe, e o desgaste do pneu
# Revisar a forma de mostrar
