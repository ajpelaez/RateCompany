import company

class Ranking:
    def __init__(self,companies):
        self.companies = companies

    def showRanking(self):
        companies_ranked = sorted(self.companies, key=lambda x: x.average, reverse=True)
        for company in companies_ranked:
            print ("Company: " + company.name + " - Average: " + str(company.average))
