#Ætla byrja á því að gera for lykkju sem keyrir eins oft i gegn og slegið er inn. Inní lykkjuni á hún að prenta út i sem byrjar í 1 sem lengi sem i er minna en 4. Svo þegar það skilyrði er mætt þá fer formulan í gang. Formulan er sú að síðustu 3 tölustafir eru summaðir til þess að mynda töluna sem prentuð er út. Geri temp breytu sem mun halda utan um þa tölu sem er verid að færa svo hun týnist ekki þegar fremsta talan verður að næstu tölu t.d. Prenta tölu út þegar búið er að reikna.
n = int(input("Enter the length of the sequence: ")) # Do not change this line
fyrsta = 1
midja = 2
seinasta = 3
for i in range(1,n+1): #lykkjan fer i gang eins oft og slegið er inn í byrjun, byrjar frá 1.
    if i < 4: #Ef i er minni en 4 þá fer for lykkjan i það að prenta út i
        print(i)
    else: #Ef ekki þá fer það í formúluna + bumpar út fremstu töluna og setur nýju "3 síðustu" í færibreytur til þess að hefja reikninginn uppá nýtt.
        prenta = fyrsta + midja + seinasta
        fyrsta = midja
        midja = seinasta
        seinasta = prenta
        print(prenta)