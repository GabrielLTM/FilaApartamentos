class FilaEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None
        
    def remover(self):
        if self.inicio == None:
            print("Nenhum elemento")

        else:
            self.inicio = self.inicio.proximo
            if self.inicio == None:
                self.fim = None

    def imprimir(self):
        if self.inicio == None:
            print("Fila está vazia!")

        else:
            aux = self.inicio
            text = " "
            while aux:
                text += aux.torre.nome + " End: " +  aux.torre.endereco  + " N° " + aux.numero + " Vaga: " + str(aux.vaga) + " | "
                aux = aux.proximo
            print( text )
            
    def add(self,apartamento ):
        apartamento.proximo = None
        if self.inicio == None:
            self.inicio = apartamento
            self.fim = apartamento
        else: 
            self.fim.proximo = apartamento
            self.fim = apartamento
        self.imprimir()
        
        return 'Adicionado a fila'
    
    def remover(self):
        if self.inicio:
            self.inicio = self.inicio.proximo
            if self.inicio == None:
                self.fim = None
            
        self.imprimir()
