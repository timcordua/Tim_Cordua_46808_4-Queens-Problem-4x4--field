class Schachbrett:

    #Schachbrett mit 4 Zeilen(rows) und 4 Spalten(cols) wird erstellt

    def __init__(self, rows, cols):
      self.rows_sb=rows #Festlegung der Anzahl der Reihen
      self.cols_sb=cols #Festlegung der Anzahl der Spalten
      self.felder = [[0 for _ in range(rows)] for _ in range(cols)] #gesamtes Schachbrett ist mit 0 (keine platzierte Dame) gefüllt


    #Gibt das aktuelle Schachbrett in der Konsole aus
    #in der Form (Beispiel):
    # 0 0 0 0
    # 1 0 0 0
    # 0 0 0 0
    # 0 1 0 0

    def SchachbrettErstellen(self):
     for i in range(self.rows_sb): #Durchläuft die alle Reihen
        for j in range(self.cols_sb): #Durchläuft alle Spalten
            print(self.felder[i][j], end=" ") #Schreibt das Schachbrett in die Konsole
        print()

    
    #Gibt das aktuelle Schachbrett zurück, damit es von anderen Klassen verarbeitet werden kann

    def SchachbrettWiedergeben(self):
        return self.felder


class VierDamenProblemLoesung:
  
    #Die Größe des Schachbrettes (4) wird als globale Variable gespeichert 

    def __init__(self, n):
        global Schachbrett_length
        Schachbrett_length = n


    

    #Prüft ob auf dem ausgewählten Feld eine Dame plaziert werden kann nach 3 Kriterien:

    #1. Guckt ob in der selben Zeile, in den Spalten die Links vom Feld sind, eine Dame steht

    #2. Guckt ob auf Diagonale Richtung ein Dame links über dem aktuellen Feld steht

    #3. Guckt ob auf Diagonale Richtung ein Dame links unter dem aktuellen Feld steht

    def PlatzPruefen(self, Schachbrett, row, col):
    
        #Prüft 1.
        for i in range(col): 
            if Schachbrett[row][i] == 1:
                return False
    
        #Prüft 2.
        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if Schachbrett[i][j] == 1:
                return False
    
        #Prüft 3.
        for i, j in zip(range(row, Schachbrett_length, 1),
                        range(col, -1, -1)):
            if Schachbrett[i][j] == 1:
                return False
    
        return True
    




    #Löst das 4 Damen Problem in dem es versucht in den Spalten, von links nach rechts, in jeder Zeile eine Dame zu platzieren

    #Wenn in einer Spalte keine Dame platziert werden kann, dann wird die Dame gelöscht und anders platziert
    
    def DamenSetzen(self, Schachbrett, col):
    
        
        if col >= Schachbrett_length: #Prüft ob bereits alle Damen plaziert wurden
            return True

        for i in range(Schachbrett_length): #Iteration über alle Zeilen einer Spalte
    
            if self.PlatzPruefen(Schachbrett, i, col):
    
                Schachbrett[i][col] = 1
    
                if self.DamenSetzen(Schachbrett, col + 1) == True: #Ruft die Überprüfung der nächsten Spalte Rekursiv auf
                    return True
    
                
                Schachbrett[i][col] = 0 #Wenn es für die nächste Spalte keine Lösung gibt wird die zuvor platzierte Dame wieder entfernt
    
        
        return False
    
    


    #Ruft die funktion DamenSetzen auf und startet die Lösung des Problems

    #Gibt "Leine Lösung gefunden!" in der Konsole aus und false zurück wenn es keine möglichkeit gibt die Damen erfolgreich nach den Kriterien zu platzieren

    #Wenn es eine Lösung gibt wird diese als Schachbrett in der Konsole ausgegeben

    def VierDamenProblemLoesen(self,Schachbrett):
        
        # Gibt "Keine Kösung gefunden!" aus wenn keine Lösung gefunden wurde
        if self.DamenSetzen(Schachbrett.SchachbrettWiedergeben(), 0) == False:
            print("Keine Lösung gefunden!")
            return False
    
        Schachbrett.SchachbrettErstellen() #Gibt die Lösung aus wenn eine Lösung gefunden wurde
        return True
  


Schachbrett = Schachbrett(4,4)
Loesung = VierDamenProblemLoesung(4)
Loesung.VierDamenProblemLoesen(Schachbrett)
