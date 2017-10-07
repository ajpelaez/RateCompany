import ranking
import company

a = company.Company("Tesla")
a.rate("Pepe",5)
a.rate("Antonio",7)

b = company.Company("McDonals")
b.rate("Juan",3)

c = company.Company("Telecinco")
c.rate("Pepe",6)

d = company.Company("Antena 3")
d.rate("Pepe",2)

e = company.Company("TVE")
e.rate("Pepe",9)

f = company.Company("Cuatro")
f.rate("Pepe",7)

x = ranking.Ranking([a,b,c,d,e,f])
x.showRanking()
