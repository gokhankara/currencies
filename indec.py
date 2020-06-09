def Kur(pasteURL, kurAdi, aciklama):
    data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
    parse = BeautifulSoup(data)
    for dolar in parse.find_all('span', id="last_last"):
        liste = list(dolar)
        print(kurAdi + " Kuru: " + str(liste) + " " + aciklama)        

Kur("https://tr.investing.com/currencies/eur-try", "Euro/TL", " " )
Kur("https://tr.investing.com/currencies/usd-try", "Dolar/TL", " ")
Kur("https://tr.investing.com/currencies/gau-try", "Altın(gram)/TL", " ")
Kur("https://tr.investing.com/currencies/xagg-try", "Gümüş(gram)/TL"," ")
Kur("https://tr.investing.com/currencies/xau-xag", "Altın(ratio)/Gümüş(ratio)", "(Bunun 12 olması gerekiyor...)")
Kur("https://tr.investing.com/currencies/eur-usd", "Euro/Dolar", "(Bu en son 1.11 orandaydı)")
