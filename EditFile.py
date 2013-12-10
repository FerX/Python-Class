#!/usr/bin/python

#############################
# Classe per editare un file testo  
##############################

class EditFile:
    """ Classe realizzata da Fernando Figaroli - FerX
        consente di modificare le righe di un file
        es.
        import EditFile
        edita=EditFile.EditFile("nomefile") // se non esiste lo crea lui
        edita.countLine()
        edita.readLine()
        edita.replaceLine()
        edita.addLine()
        edita.deleteLine()

    """
    
    def __init__(self,nomefile):
        self.nomefile=nomefile
        #testare esistenza se non ce lo creaa
        testopen=open(nomefile,'a+')
   
    def countLine(self):
        """conta il numero di righe di un file """
        lines = open(self.nomefile, 'r').readlines()
        return len(lines)
    
    def readLine(self,numlinea=":"):
        """legge linee da un file, posso specificare una singola riga o piu righe, 
        es. readLine(0) --> torna la prima riga
            readline([1,3,5]) ---> torna la seconda, quarta e sesta riga
            readline() --> torna l'interno file in una lista divisa per righe
            readline(0:5) --> torna le prime 5 righe
            readline(3:5) --> torna la quarta e quinta riga"""
        lines = open(self.nomefile, 'r').readlines()
        #verifico che tipo di argomento ha passato
        if type(numlinea) ==int or type(numlinea) ==str:
            # se intero o str --> slice
            listarighe= eval("lines[%s]" % numlinea) 
        elif type(numlinea) == list:
            # se lista
            listarighe="" 
            for x in nunlinea:
                listarighe+= lines[x] 
        
        return listarighe
    
    def replaceLine(self,numlinea,text):
        """ Sostituisce una riga specifica con un altro testo
        es. replaceLine(15,"nuovo testo \n")
            attenzione ad inserire il ritorno a capo
        """
        lines = open(self.nomefile, 'r').readlines()
        lines[numlinea] = text
        out = open(self.nomefile,'w')
        out.writelines(lines)
        out.close()

    def addLine(self,text):
        """ aggiunge del testo in fondo al file"""
        
        lines = open(self.nomefile, 'a')
        lines.write(text)
        lines.close()

    def deleteLine(self,numlinea):
        """ cancella una riga"""
        self.replaceLine(self.nomefile,numlinea,"")


