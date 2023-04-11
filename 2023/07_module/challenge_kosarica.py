# naredimo nakupovalni seznam.
# nakupovalni seznam za povrstjo sprejema izdelke, ki jih pišemo v input ter jih nato shrani v seznam.
# iz nakupovalnega seznama lahko izdelke tudi odstranjujemo


# Nakupovalni seznam traja, dokler uporabnik v input ne napiše besede "checkout" -> ko napise to besedo
# izračunaj vrednost seznama ter jo izpiši skupaj s seznamom
# Izračun in izpis v funkciji


# dodajanje v seznam
# uporabnik zažene dodajanje v seznam tako, da v input napiše besedo "add"
# uporabnik nato v input napiše vse elemente ki jih naenkrat želi dodati v seznam.
# primerr vnosa:
# kruh-2, zelenjava-4, mleko-1
# input ter dodajanje na seznam v funkciji


# odstrenjevanje iz seznama:
# odstranjevanje se začne tako, da uporabnik v input napiše ukaz "remove"
# poteka na isti način kot dodajanje samo da namesto dodajnja odstranjujemo.
# input ter odstranjevanje iz seznama v funckiji


# v seznamu imamo lahko naenkrat več istih elementov samo če imajo drugačne cene


# prostor za funkcije

### BONUS ###
# Pred-definiraj slovar izdelkov, ki bo vseboval cene za vse izdelke.
# Uporabnik lahko tako dodaja samo izdelke, ki se nahajajo v tem slovarju - končno ceno pa izračunajte iz slovarja.
### BONUS ###


def checkout():
    pass


def dodajanjeIzdelkov():
    pass


def odstranjevanjeIzdelkov():
    pass


# prostor za program
nakupovaniSeznam = []

while True:
    komanda = input("Vnesi komando; add, remove, checkout:   ")
