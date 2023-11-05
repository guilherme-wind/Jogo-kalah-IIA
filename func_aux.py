from kalah import *

# ______________________________________________________________________________
# Metodos Auxiliares

class Jogador():
    def __init__(self, nome, fun):
        self.nome = nome
        self.fun = fun
    def display(self):
        print(self.nome+" ")

class JogadorAlfaBeta(Jogador):
    def __init__(self, nome, depth,fun_eval):
        self.nome = nome
        self.fun = lambda game, state: alphabeta_cutoff_search_new(state,game,depth,eval_fn=fun_eval)

def joga11(game, jog1, jog2,verbose=False):
    ### jog1 e jog2 são jogadores com funções que dado um estado do jogo devolvem a jogada que escolheram
    ### devolve o par de jogadores, a lista de jogadas e o resultado
    estado=game.initial
    proxjog = jog1
    lista_jogadas=[]
    lance = 0
    while not game.terminal_test(estado):
        if verbose:
            print('----------   LANCE:',lance)
            game.display(estado)
        jogada = proxjog.fun(game, estado)
        if verbose:
            print('JOGADA=',jogada)
        estado=game.result(estado,jogada)
        lista_jogadas.append(jogada)
        proxjog = jog2 if proxjog == jog1 else jog1
        lance+=1
    #p jogou e ganhou
    util=game.utility(estado,0)
    if util == 1:
        resultado=jog1.nome
    elif util== -1:
        resultado = jog2.nome
    else:
        resultado='Empate'
    return ((jog1.nome,jog2.nome),lista_jogadas,resultado)

scores={'Vitoria': 3, 'Empate': 1}

def traduzPontos(tabela):
    tabelaScore={}
    empates=tabela['Empate']
    for x in tabela:
        if x != 'Empate':
            tabelaScore[x]=scores['Vitoria']*tabela[x]+empates
    return tabelaScore

def jogaNpares(jogo,n,jog1,jog2):
    tabelaPrim={jog1.nome:0, jog2.nome:0, 'Empate':0}
    tabelaSeg={jog1.nome:0, jog2.nome:0, 'Empate':0}
    tabela={}
    for _ in range(n):
        _,_,vencedor=joga11(jogo,jog1,jog2)
        tabelaPrim[vencedor]+=1
        _,_,vencedor=joga11(jogo,jog2,jog1)
        tabelaSeg[vencedor]+=1
    for x in tabelaPrim:
        tabela[x]=tabelaPrim[x]+tabelaSeg[x]
    return tabelaPrim,tabelaSeg,tabela,traduzPontos(tabela)
