import math
print(50 * '_')
print('NIVELMANSKI OBRAZEC')
print('MATEVŽ LEDINEK')
print(50 * '_')
print('INŠTRUMENT: KONI Ni 007')
print(50 * '_')

stevilo_razdelb = input('VNESITE ŠTEVILO RAZDELB NA LATI [1 ALI 2]: ')

if int(stevilo_razdelb) == 1:
        
    print (50 * '_')
    visinske_razlike = []
    i = 1
    zanka = True
    while zanka is True:

        print('STOJIŠČE ŠTEVILKA {:g}'.format(i))
        print('\nMERITEV ZADAJ')
        R_1 = input('\tIME PRVEGA STOJIŠČA = ') # prvi reper zadaj
        oz_1 = input('\tODČITEK ZGORAJ = ') # odčitek zgoraj zadaj (kot string: 'm dm cm mm...' brez presledkov)
        o_1 = input('\tODČITEK V SREDINI = ') # odčitek v sredini zadaj
        os_1 = input('\tODČITEK SPODAJ = ') # odčitek spodaj zadaj 

        n_1 = len(oz_1) #spremeni odčitek v metre
        oz_1 = int(oz_1) / (10 ** (n_1 - 1))        
        n_2 = len(o_1)
        o_1 = int(o_1) / (10 ** (n_2 - 1))
        n_3 = len(os_1)
        os_1 = int(os_1) / (10 ** (n_3 - 1))

        razdalja_1 = (oz_1 - os_1) # razdalja med reperjem in lato zadaj #m
        print('\tRAZDALJA = {:.4f} m'.format(razdalja_1))

        print('\nMERITEV SPREDAJ')
        oz_2 = input('\tODČITEK ZGORAJ = ') # odčitek zgoraj spredaj
        o_2 = input('\tODČITEK V SREDINI = ') # odčitek v sredini spredaj
        os_2 = input('\tODČITEK SPODAJ = ') # odčitek spodaj spredaj 

        n_4 = len(oz_2) #spremeni odčitek v metre
        oz_2 = int(oz_2) / (10 ** (n_4 - 1))        
        n_5 = len(o_2)
        o_2 = int(o_2) / (10 ** (n_5 - 1))
        n_6 = len(os_2)
        os_2 = int(os_2) / (10 ** (n_6 - 1))

        razdalja_2 = (oz_2 - os_2) # razdalja med reperjem in lato spredaj
        print('\tRAZDALJA = {:.4f} m'.format(razdalja_2))

        vr = o_1 - o_2
        visinske_razlike.append(vr)
        print('\nVIŠINSKA RAZLIKA {0:.4f} = {1:.4f} m'.format(i, vr))
        print(50 * '_')

        izbira = int(input('\nNADALJUJEM? DA [1], NE [2]: '))
        print(50 * '_')

        if izbira == 1:
            i += 1
        elif izbira == 2:
            sprememba_visine = sum(visinske_razlike)
            print('\nSKUPNA SPREMEMBA VIŠINE = {:.4f} m'.format(sprememba_visine))
            print(50 * '_')
            zanka = False             

if int(stevilo_razdelb) == 2:
        
    print (50 * '_')
    visinske_razlike = []
    i = 1
    zanka = True
    while zanka is True:

        print('STOJIŠČE ŠTEVILKA {:g}'.format(i))
        print('\nMERITEV ZADAJ')
        R_1 = input('\tIME PRVEGA STOJIŠČA = ') # prvi reper zadaj levo
        oz_1 = input('\tODČITEK ZGORAJ LEVO = ') # odčitek zgoraj zadaj (kot string: 'm dm cm mm...' brez presledkov)
        o_1 = input('\tODČITEK V SREDINI LEVO= ') # odčitek v sredini zadaj levo
        os_1 = input('\tODČITEK SPODAJ LEVO = ') # odčitek spodaj zadaj levo
        
        oz_2 = input('\tODČITEK ZGORAJ DESNO= ') # odčitek zgoraj zadaj (kot string: 'm dm cm mm...' brez presledkov)
        o_2= input('\tODČITEK V SREDINI DESNO= ') # odčitek v sredini zadaj desno
        os_2 = input('\tODČITEK SPODAJ DESNO = ') # odčitek spodaj zadaj desno
        
        n_1 = len(oz_1) #spremeni odčitek levo v metre
        oz_1 = int(oz_1) / (10 ** (n_1 - 1))        
        n_2 = len(o_1)
        o_1 = int(o_1) / (10 ** (n_2 - 1))
        n_3 = len(os_1)
        os_1 = int(os_1) / (10 ** (n_3 - 1))
        
        n_2 = len(oz_2) #spremeni odčitek desno v metre
        oz_2 = int(oz_2) / (10 ** (n_1 - 1))        
        n_1 = len(o_2)
        o_2 = int(o_2) / (10 ** (n_2 - 1))
        n_3 = len(os_2)
        os_2 = int(os_2) / (10 ** (n_3 - 1))
        
        razdalja_2 = (oz_2 - os_2) # razdalja med reperjem in lato zadaj #m
        print('\tRAZDALJA2 = {:.1f} m'.format(razdalja_2))
        razdalja_1 = (oz_1 - os_1) # razdalja med reperjem in lato zadaj #m
        print('\tRAZDALJA1 = {:.1f} m'.format(razdalja_1))

        print('\nMERITEV SPREDAJ')
        oz_2 = input('\tODČITEK ZGORAJ = ') # odčitek zgoraj spredaj
        o_2 = input('\tODČITEK V SREDINI = ') # odčitek v sredini spredaj
        os_2 = input('\tODČITEK SPODAJ = ') # odčitek spodaj spredaj 

        n_4 = len(oz_2) #spremeni odčitek v metre
        oz_2 = int(oz_2) / (10 ** (n_4 - 1))        
        n_5 = len(o_2)
        o_2 = int(o_2) / (10 ** (n_5 - 1))
        n_6 = len(os_2)
        os_2 = int(os_2) / (10 ** (n_6 - 1))

        razdalja_2 = (oz_2 - os_2) # razdalja med reperjem in lato spredaj
        print('\tRAZDALJA = {:.1f} m'.format(razdalja_2))

        vr = o_1 - o_2
        visinske_razlike.append(vr)
        print('\nVIŠINSKA RAZLIKA {0:.4f} = {1:.4f} m'.format(i, vr))
        print(50 * '_')

        izbira = int(input('\nNADALJUJEM? DA [1], NE [2]: '))
        print(50 * '_')

        if izbira == 1:
            i += 1
        elif izbira == 2:
            sprememba_visine = sum(visinske_razlike)
            print('\nSKUPNA SPREMEMBA VIŠINE = {:.4f} m'.format(sprememba_visine))
            print(50 * '_')
            zanka = False