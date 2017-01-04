# import math
print(50 * '_')
print('NIVELMANSKI OBRAZEC')
print('AVTOR: MATEVŽ LEDINEK')
print(50 * '_')


def izpis(ime, oz_z, os_z, s_z, dol_z, oz_s, os_s, s_s, dol_s, raz, file):
    """
    Funkcija, ki izpiše meritve in rezultate v poljubno datoteko.
    
    ime: ime stojišča
    oz_z: odčitek zgoraj zadaj v m
    os_z: odčitek spodaj zadaj v m
    s_z: odcitek v sredini zadaj v m
    dol_z: dolžina do žabe v m
    oz_s: odčitek zgoraj spredaj v m
    os_s: odčitek spodaj spredaj v m
    s_s: odčitek sredina spredaj v m
    dol_s: dolžina do žabe v m
    raz:  višinska razlika v m
    file: pot in ime datoteke, v katero želimo zapisovati (\\pot\\ime_datoteke.txt)
    """
    sir_1 = max([len(i) for i in ime])
    sir_2 = max([len(str(i)) for i in oz_z + os_z])
    sir_3 = max([len(str(i)) for i in s_z])
    sir_4 = max([len(str(i)) for i in dol_z])
    sir_5 = max([len(str(i)) for i in oz_s + os_s])
    sir_6 = max([len(str(i)) for i in s_s])
    sir_7 = max([len(str(i)) for i in dol_s])
    sir_8 = max([len(str(i)) for i in raz])
    
    for i in range(len(ime)):
        print('{0:{width}}'.format(ime[i], width=sir_1), '{0:{width}}'.format(oz_z[i], width=sir_2), '{:{width}}'.format(' ',width=sir_3),'{:{width}}'.format(' ',width=sir_4), '{0:{width}}'.format(oz_s[i], width=sir_5), file=file)
        print('{:{width}}'.format(' ',width=sir_1), '{:{width}}'.format(' ',width=sir_2), '{0:{width}}'.format(s_z[i], width=sir_3), '{0:{width}.2f}'.format(dol_z[i], width=sir_4), '{:{width}}'.format(' ',width=sir_5), '{0:{width}}'.format(s_s[i], width=sir_6), '{0:{width}.2f}'.format(dol_s[i], width=sir_7), '{0:{width}.3f}'.format(raz[i], width=sir_8), file=file)
        print('{:{width}}'.format(' ',width=sir_1), '{0:{width}}'.format(os_z[i], width=sir_2), '{:{width}}'.format(' ',width=sir_3),'{:{width}}'.format(' ',width=sir_4), '{0:{width}}'.format(os_s[i], width=sir_5), file=file)
        print((sir_1 + sir_2 + sir_3 + sir_4 + sir_5 + sir_6 + sir_7 + sir_8 + 7)*'_', file=file)

stevilo_razdelb = input('VNESITE ŠTEVILO RAZDELB NA LATI [1 ALI 2]: ')


if int(stevilo_razdelb) == 1:
    
    print (50 * '_')
    razdalja_zab = []
    visinske_razlike = []
    razdalja_1zzz = []
    razdalja_2zzz = []
    R_1zzz = []
    oz_1zzz = []
    os_1zzz = []
    o_1zzz = []
    oz_2zzz = []
    o_2zzz =  []
    os_2zzz = []
    
    i = 1
    zanka = True
    while zanka is True:
        zanka1 = True
        while zanka1 is True:
            zanka2 = True
            while zanka2 is True:
                print('STOJIŠČE ŠTEVILKA {:g}'.format(i))
                print('\nMERITEV ZADAJ')
                print('\nPREDLAGANO IME STOJIŠČA : {:g}'.format(i))
                R_1 = input('\tIME PRVEGA STOJIŠČA = ') # prvi reper zadaj
                oz_1 = input('\tODČITEK ZGORAJ = ') # odčitek zgoraj zadaj (kot string: 'm dm cm mm...' brez presledkov)
                o_1 = input('\tODČITEK V SREDINI = ') # odčitek v sredini zadaj
                os_1 = input('\tODČITEK SPODAJ = ') # odčitek spodaj zadaj 

                povprecje1 = (int(oz_1) + int(os_1)) / 2
                razlika1 = abs(int(povprecje1) - int(o_1))

                if razlika1 > 2: # Opozirilo na napačen odčitek - razlika med sredino in povprečjem
                    print('PONOVNO ODČITAJ RAZDELBO ----> STORIL SI GROB POGREŠEK')
                    zanka1 = True

                else: 
                    zanka1 = False

                    n_1 = len(oz_1) #spremeni odčitek v metre
                    oz_1 = int(oz_1) / (10 ** (n_1 - 1))        
                    n_2 = len(o_1)
                    o_1 = int(o_1) / (10 ** (n_2 - 1))
                    n_3 = len(os_1)
                    os_1 = int(os_1) / (10 ** (n_3 - 1))

                    razdalja_1 = (oz_1 - os_1)*100 # razdalja med reperjem in lato zadaj #m
                    print('\tRAZDALJA = {:.0f} m'.format(razdalja_1))

                    print('\nMERITEV SPREDAJ')
                    oz_2 = input('\tODČITEK ZGORAJ = ') # odčitek zgoraj spredaj
                    o_2 = input('\tODČITEK V SREDINI = ') # odčitek v sredini spredaj
                    os_2 = input('\tODČITEK SPODAJ = ') # odčitek spodaj spredaj 

                    povprecje2 = (int(oz_2) + int(os_2)) / 2
                    razlika2 = abs(int(povprecje2) - int(o_2))
                    
                    if razlika2 > 2: # Opozirilo na napačen odčitek - razlika med sredino in povprečjem
                        print('PONOVNO ODČITAJ RAZDELBO ----> STORIL SI GROB POGREŠEK')
                        zanka2 = True

                    else: 
                        zanka2 = False

                        n_4 = len(oz_2) #spremeni odčitek v metre
                        oz_2 = int(oz_2) / (10 ** (n_4 - 1))        
                        n_5 = len(o_2)
                        o_2 = int(o_2) / (10 ** (n_5 - 1))
                        n_6 = len(os_2)
                        os_2 = int(os_2) / (10 ** (n_6 - 1))

                        razdalja_2 = (oz_2 - os_2)*100 # razdalja med reperjem in lato spredaj
                        print('\tRAZDALJA = {:.0f} m'.format(razdalja_2))

                        vr = o_1 - o_2
                        visinske_razlike.append(vr)
                        nv = razdalja_1 + razdalja_2
                        razdalja_zab.append(nv)
                        razdalja_1zzz.append(razdalja_1)
                        razdalja_2zzz.append(razdalja_2)
                        R_1zzz.append(R_1)
                        oz_1zzz.append(oz_1)
                        os_1zzz.append(os_1)
                        o_1zzz.append(o_1)
                        oz_2zzz.append(oz_2)
                        o_2zzz.append(o_2)
                        os_2zzz.append(os_2)
                        
                        

                        print('\nVIŠINSKA RAZLIKA {0:.0f} = {1:.4f} m'.format(i, vr))
                        print(50 * '_')

                        izbira = int(input('\nNADALJUJEM? DA [1], NE [2]: '))
                        print(50 * '_')

                        if izbira == 1:
                                i += 1
                        elif izbira == 2:
                            sprememba_visine = sum(visinske_razlike)
                            print('\nSKUPNA SPREMEMBA VIŠINE = {:.4f} m'.format(sprememba_visine))
                            dolzina_vlaka = sum(razdalja_zab)
                            print('\nDOLZINA NIVELMANSKEGA VLAKA = {:.1f} m'.format(dolzina_vlaka))
                            print(50 * '_')
                            
                            zanka = False   
                            

if int(stevilo_razdelb) == 2:       
    print (50 * '_')
    visinske_razlike1 = []
    visinske_razlike2 = []
    razdalja_zab1     = [] 
    i = 1
    zanka = True
    while zanka is True:
        
        zanka1 = True
        while zanka1 is True:
            zanka2 = True
            while zanka2 is True:
            
                print('STOJIŠČE ŠTEVILKA {:g}'.format(i))
                print('\nMERITEV ZADAJ')
                print('\nPREDLAGANO IME STOJIŠČA : {:g}'.format(i))
                
                R_1 = input('\tIME PRVEGA STOJIŠČA = ') # prvi reper zadaj levo
                oz_1 = input('\tODČITEK ZGORAJ LEVO = ') # odčitek zgoraj zadaj (kot string: 'm dm cm mm...' brez presledkov)
                o_1 = input('\tODČITEK V SREDINI LEVO= ') # odčitek v sredini zadaj levo
                os_1 = input('\tODČITEK SPODAJ LEVO = ') # odčitek spodaj zadaj levo

                oz_2 = input('\tODČITEK ZGORAJ DESNO= ') # odčitek zgoraj zadaj (kot string: 'm dm cm mm...' brez presledkov)
                o_2= input('\tODČITEK V SREDINI DESNO= ') # odčitek v sredini zadaj desno
                os_2 = input('\tODČITEK SPODAJ DESNO = ') # odčitek spodaj zadaj desno

                povprecje1 = (int(oz_1) + int(os_1)) / 2
                razlika1 = abs(int(povprecje1) - int(o_1))

                povprecje2 = (int(oz_2) + int(os_2)) / 2
                razlika2 = abs(int(povprecje2) - int(o_2))

                if razlika1 or razlika2 > 2: #Opozirilo na napačen odčitek - razlika med sredino in povprečjem v enem izmed
                    print('PONOVNO ODČITAJ RAZDELBO ----> STORIL SI GROB POGREŠEK')
                    zanka1 = True

                else: 
                    zanka1 = False

                    n_1 = len(oz_1) #spremeni odčitek 1
                    oz_1 = int(oz_1) / (10 ** (n_1 - 1))        
                    n_2 = len(o_1)
                    o_1 = int(o_1) / (10 ** (n_2 - 1))
                    n_3 = len(os_1)
                    os_1 = int(os_1) / (10 ** (n_3 - 1))

                    n_1 = len(oz_2) #spremeni odčitek 2
                    oz_2 = int(oz_2) / (10 ** (n_1 - 1))        
                    n_2 = len(o_2)
                    o_2 = int(o_2) / (10 ** (n_2 - 1))
                    n_3 = len(os_2)
                    os_2 = int(os_2) / (10 ** (n_3 - 1))


                    razdalja_1 = (oz_1 - os_1)*100 # razdalja med reperjem in lato zadaj #m
                    print('\tRAZDALJA 1 = {:.1f} m'.format(razdalja_1))

                    print('\nMERITEV SPREDAJ')
                    oz_3 = input('\tODČITEK ZGORAJ LEVO = ') # odčitek zgoraj zadaj (kot string: 'm dm cm mm...' brez presledkov)
                    o_3  = input('\tODČITEK V SREDINI LEVO= ') # odčitek v sredini zadaj levo
                    os_3 = input('\tODČITEK SPODAJ LEVO = ') # odčitek spodaj zadaj levo

                    oz_4 = input('\tODČITEK ZGORAJ DESNO= ') # odčitek zgoraj zadaj (kot string: 'm dm cm mm...' brez presledkov)
                    o_4  = input('\tODČITEK V SREDINI DESNO= ') # odčitek v sredini zadaj desno
                    os_4 = input('\tODČITEK SPODAJ DESNO = ') # odčitek spodaj zadaj desno

                    povprecje3 = (int(oz_3) + int(os_3)) / 2
                    razlika3 = abs(int(povprecje3) - int(o_3))

                    povprecje4 = (int(oz_4) + int(os_4)) / 2
                    razlika4 = abs(int(povprecje4) - int(o_4))

                    if razlika3 or razlika4 > 2: #Opozirilo na napačen odčitek - razlika med sredino in povprečjem v enem izmed
                        print('PONOVNO ODČITAJ RAZDELBO ----> STORIL SI GROB POGREŠEK')
                        zanka2 = True

                    else: 
                        zanka2 = False

                        n_1 = len(oz_3) #spremeni 1
                        oz_3 = int(oz_3) / (10 ** (n_1 - 1))        
                        n_2 = len(o_3)
                        o_3 = int(o_3) / (10 ** (n_2 - 1))
                        n_3 = len(os_3)
                        os_3 = int(os_3) / (10 ** (n_3 - 1))

                        n_1 = len(oz_4) #spremeni 2
                        oz_4 = int(oz_4) / (10 ** (n_1 - 1))        
                        n_2 = len(o_4)
                        o_4 = int(o_4) / (10 ** (n_2 - 1))
                        n_3 = len(os_4)
                        os_4 = int(os_4) / (10 ** (n_3 - 1))


                        razdalja_2 = (oz_3 - os_3)*100 # razdalja med reperjem in lato zadaj #m
                        print('\tRAZDALJA 2 = {:.1f} m'.format(razdalja_2))

                        vr1 = o_1 - o_3
                        visinske_razlike1.append(vr1)
                        vr2 = o_2 - o_4
                        visinske_razlike2.append(vr2)
                        nv1 = razdalja_1 + razdalja_2
                        razdalja_zab1.append(nv1)

                        print('\nVIŠINSKA RAZLIKA RAZDELBA LEVO {0:.0f} = {1:.4f} m'.format(i, vr1))
                        print('\nVIŠINSKA RAZLIKA RAZDELBA DESNO{0:.0f} = {1:.4f} m'.format(i, vr2))
                        print(50 * '_')

                        izbira = int(input('\nNADALJUJEM? DA [1], NE [2]: '))
                        print(50 * '_')

                        if izbira == 1:
                            i += 1
                        elif izbira == 2:
                            sprememba_visine1 = sum(visinske_razlike1)
                            print('\nSKUPNA SPREMEMBA VIŠINE RAZDELBA LEVO = {:.4f} m'.format(sprememba_visine1))
                            sprememba_visine2 = sum(visinske_razlike2)
                            print('\nSKUPNA SPREMEMBA VIŠINE RAZDELBA LEVO = {:.4f} m'.format(sprememba_visine1))
                            dolzina_vlaka = sum(razdalja_zab1)
                            print('\nDOLZINA NIVELMANSKEGA VLAKA = {:.1f} m'.format(dolzina_vlaka))
                            print(50 * '_')
                            zanka = False

with open('Rezultati.txt', mode='w') as datoteka:
    izpis(R_1zzz, oz_1zzz, os_1zzz, o_1zzz, razdalja_1zzz, oz_2zzz, os_2zzz, o_2zzz, razdalja_2zzz, visinske_razlike, datoteka)
    print('Dolžina vlaka: {:.2f}'.format(dolzina_vlaka), file = datoteka )
    print('Skupna višinska sprememba: {:.3f}'.format(sprememba_visine), file = datoteka )