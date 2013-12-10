#!/usr/bin/python

######################################################################
#Classe ModConf per manipolare un file di configurazione
######################################################################

class ModConf:
    """questa classe personale di FerX serve per leggere, scrivere e manipolare variabili in file di configurazione
    utilizzo:
    nomevar=ModConf("nomefile")
    nomevar.getVar("nomevariabile")
    nomevar.delVar("nomevariabile")
    nomevar.setVar("nomevariabile","valore",[separatore])

    """
    import os
    import sys

    def __init__(self,nomefile):
        #memorizzo nome file ma non lo apro
        self.nomefile=nomefile
        from EditFile import EditFile 
        self.editfile=EditFile(nomefile)
        return None
    
    def getVar(self,nomevariabile,delimitatore="="):
        #metto tutto il file in una variabile
        contenuto=self.editfile.readLine()
        trovati=[]
        nlinea=0
        for line in contenuto:
            #tolgo spazi iniziali e finali inutili
            line=line.strip() 
            if nomevariabile.lower() in line.lower(): 
                #verifico se prima parola == variabile che cerco eliminando spazi superflui
                if nomevariabile.lower() == line.split(delimitatore)[0].strip().lower():
                    valore=line.split(delimitatore)[1]
                    trovati.append([nlinea,line.split(delimitatore)[0],valore])
            nlinea+=1
        return trovati

    
    def delVar(self,nomevariabile,delimitatore="="):
        """Cancello variabile"""
        trovato=self.getVar(nomevariabile,delimitatore)
        for x in trovato:
            self.editfile.replaceLine(x[0],"")

    def setVar(self,nomevariabile,valore,delimitatore="="):
        """Aggiungo o modifico una variabile"""
        #leggo le esistenti
        trovato=self.getVar(nomevariabile,delimitatore)
        s=nomevariabile+delimitatore+str(valore)+"\n"
        if trovato:
            #considero solo l'ultima variabile
            linea=trovato[-1:][0][0]
            self.editfile.replaceLine(linea,s)
        else:
            #non esiste quindi devo aggiungere
            self.editfile.addLine(s) 
        return True

######################################################################
# END CLASS ModConf
######################################################################


##########
# TEST
##########
a=ModConf("fffnomefile.txt")
a.setVar("prova",1)
print "ho impostato prova = 1"
a.setVar("prova2",2)
print "ho impostato prova = 2"

