# import math
print(50 * '_')
print('NIVELMANSKI OBRAZEC')
print('AVTOR: MATEVŽ LEDINEK')
print(50 * '_')

stevilo_razdelb = input('VNESITE ŠTEVILO RAZDELB NA LATI [1 ALI 2]: ')

if int(stevilo_razdelb) == 1:
        
    print (50 * '_')
    visinske_razlike = []
    razdalja_zab     = []
    i = 1
    zanka = True
    while zanka is True:
        zanka1 = True
        while zanka1 is True:
            zanka2 = True
            while zanka2 is True:
                print('STOJIŠČE ŠTEVILKA {:g}'.format(i))
                print('\nMERITEV ZADAJ')
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
