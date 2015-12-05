# -*- coding: utf-8 -*-
import random

def osemStevilk():
            seznamStevilk = []
            stevecStevilk = 0
            while stevecStevilk != 8:
                nakljucnoSt = random.randint(1,50)
                if nakljucnoSt not in seznamStevilk:
                    seznamStevilk.append(nakljucnoSt)
                    stevecStevilk +=1
                else:
                    continue
            return seznamStevilk


def dodatniStevilki():
            seznamDodatnih = []
            stevecDodatnih = 0
            while stevecDodatnih != 2:
                    nakljucnoSt = random.randint(1,8)
                    if nakljucnoSt not in seznamDodatnih:
                        seznamDodatnih.append(nakljucnoSt)
                        stevecDodatnih +=1
                    else:
                        continue
            return seznamDodatnih




def igrajLoto(stevilo):
    stevec = 1
    lotoListek ={}
    while stevec != stevilo+1:
        kljuc = "EuroJackpot listek stevilka: " + str(stevec)
        lotoListek[kljuc] = (osemStevilk(),dodatniStevilki())

        stevec+=1

    for kljuc in sorted(lotoListek):
        print "%s: %s" % (kljuc, lotoListek[kljuc])


def main():
    steviloListkov = int(raw_input("Vnesi število želenih loto listkov: "))
    igrajLoto(steviloListkov)

if __name__ == '__main__':
    main()