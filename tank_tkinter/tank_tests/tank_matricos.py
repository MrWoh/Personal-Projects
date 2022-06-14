import numpy as np
from time import sleep


class tankas:
    def __init__(self, iksas, ygrekas, kryptis):
        self.iksas = iksas
        self.ygrekas = ygrekas
        self.kryptis = kryptis


class suvis:
    def __init__(self, siksas, sygrekas,):
        self.siksas = siksas
        self.sygrekas = sygrekas


class taikinys:
    def __init__(self,iksse, ygra):
        self.iksse = iksse
        self.ygra = ygra


def pats_tankas():
    arr[iks.ygrekas, iks.iksas] = 6
def pats_suvis():
    arr[suv.sygrekas, suv.siksas] = 2


taikiniai = []

iksse = np.random.randint(0,19)
ygra =  np.random.randint(0,19)
# taikini = taikinys(iksse, ygra)
       
def kripts():
    if iks.kryptis == 1:
        krpts = 'pasisukta link siaure'
        return print(krpts)
    elif iks.kryptis == 2:
        krpts = 'pasisukta link vakarai'
        return print(krpts)
    elif iks.kryptis == 3:
        krpts = 'pasisukta link pietus'
        return print(krpts)
    elif iks.kryptis == 4:
        krpts = 'pasisukta link rytai'
        return print(krpts)
    
  





    

       

def suviss():
    
    nepataikymas = True


    while nepataikymas:
        
        
        
        if iks.kryptis == 1:
            arr[suv.sygrekas, suv.siksas] = 0
            suv.sygrekas -= 1
            pats_tankas()
            pats_suvis()
            print("")
            print(arr)
            sleep(0.4)
            if suv.sygrekas == 0:
                arr[suv.sygrekas, suv.siksas] = 0
                suv.sygrekas = iks.ygrekas
                suv.siksas = iks.iksas 
                pats_tankas()
                print("")
                print(arr)
                kripts()
                break
            
            
            
        if iks.kryptis == 2:
            arr[suv.sygrekas, suv.siksas] = 0
            suv.siksas -= 1
            pats_tankas()
            pats_suvis()
            print("")
            print(arr)
            sleep(0.4)
            if suv.siksas == 0:
                arr[suv.sygrekas, suv.siksas] = 0
                suv.sygrekas = iks.ygrekas
                suv.siksas = iks.iksas
                pats_tankas()
                print("")
                print(arr)
                kripts()
                break
            
            
            
        if iks.kryptis == 3:
            arr[suv.sygrekas, suv.siksas] = 0
            suv.sygrekas += 1
            pats_tankas()
            pats_suvis()
            print("")
            print(arr)
            sleep(0.4)
            if suv.sygrekas == 19:
                arr[suv.sygrekas, suv.siksas] = 0
                suv.sygrekas = iks.ygrekas
                suv.siksas = iks.iksas
                pats_tankas()
                print("")
                print(arr)
                kripts()
                break
            
        if iks.kryptis == 4:
            arr[suv.sygrekas, suv.siksas] = 0
            suv.siksas += 1
            pats_tankas()
            pats_suvis()
            print("")
            print(arr)
            sleep(0.4)
            if suv.siksas == 19:
                arr[suv.sygrekas, suv.siksas] = 0
                suv.sygrekas = iks.ygrekas
                suv.siksas = iks.iksas
                pats_tankas()
                print("")
                print(arr)
                kripts()
                break
        for taikini in taikiniai:    
            if suv.siksas == taikini.ygra and suv.sygrekas == taikini.iksse:
                arr[suv.sygrekas, suv.siksas] = 0
                arr[taikini.iksse, taikini.ygra] = 0
                suv.sygrekas = iks.ygrekas
                suv.siksas = iks.iksas
                pats_tankas()
                print("")
                print(arr)
                kripts()
                nepataikymas = False
                break



def priekin():
    if iks.kryptis == 1:
        arr[iks.ygrekas, iks.iksas] = 0
        iks.ygrekas -= 1
        suv.sygrekas -= 1
        pats_tankas()
        print(arr)
        kripts()
    elif iks.kryptis == 2:
        arr[iks.ygrekas, iks.iksas] = 0
        iks.iksas -= 1
        suv.siksas -= 1
        pats_tankas()
        print(arr)
        kripts()
    elif iks.kryptis == 3:
        arr[iks.ygrekas, iks.iksas] = 0
        iks.ygrekas += 1
        suv.sygrekas += 1
        pats_tankas()
        print(arr)
        kripts()
    elif iks.kryptis == 4:
        arr[iks.ygrekas, iks.iksas] = 0
        iks.iksas += 1
        suv.siksas += 1
        pats_tankas()
        print(arr)
        kripts()


def atgal():
    if iks.kryptis == 1:
        arr[iks.ygrekas, iks.iksas] = 0
        iks.ygrekas += 1
        suv.sygrekas += 1
        pats_tankas()
        print(arr)
        kripts()
    elif iks.kryptis == 2:
        arr[iks.ygrekas, iks.iksas] = 0
        iks.iksas += 1
        suv.siksas += 1
        pats_tankas()
        print(arr)
        kripts()
    elif iks.kryptis == 3:
        arr[iks.ygrekas, iks.iksas] = 0
        iks.ygrekas -= 1
        suv.sygrekas -= 1
        pats_tankas()
        print(arr)
        kripts()
    elif iks.kryptis == 4:
        arr[iks.ygrekas, iks.iksas] = 0
        iks.iksas -= 1
        suv.siksas -= 1
        pats_tankas()
        print(arr)
        kripts()




def kairen():
    iks.kryptis += 1
    if iks.kryptis > 4:
        iks.kryptis = 1
    elif iks.kryptis < 1:
        iks.kryptis = 4
    print(arr)
    kripts()


def desinen():
    iks.kryptis -= 1
    if iks.kryptis > 4:
        iks.kryptis = 1
    elif iks.kryptis < 1:
        iks.kryptis = 4
    print(arr)
    kripts()














        
        
arr = np.zeros((20, 20))

iks = tankas(10, 10, 1)

suv = suvis(iks.iksas, iks.ygrekas)




arr[iks.ygrekas, iks.iksas]= 6
print(arr)
kripts()


def zaidimas():
    while True:
        a = int(input('''
        1: pirmyn
        2: atgal
        3: pasisukt desinen
        4: pasisukt kairen
        5: issauk
        6: prideti taikiny
        7: isjungt
        '''))
        if a == 1:
            priekin()
        if a == 2:
            atgal()
        if a == 3:
            desinen()
            
        if a == 4:
            kairen()
        
        if a == 5:
            suviss()
        if a == 6:
            # global taikini
            # arr[taikini.iksse, taikini.ygra] = 0
            global iksse
            iksse = np.random.randint(0,19)
            global ygra
            ygra =  np.random.randint(0,19)
            taikini = taikinys(iksse, ygra)
            taikiniai.append(taikini)
            arr[taikini.iksse, taikini.ygra] = 3
            print(arr)
            
        if a == 7:
            break

zaidimas()