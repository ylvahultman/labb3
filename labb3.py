import csv

class Support:
    def __init__(self, id, kund, kategori, prioritet, status):
        self.id = id
        self.kund = kund
        self.kategori = kategori
        self.prioritet = prioritet
        self.status = status

    def high_priority(self):
        return self.prioritet.lower() == "hög"

    def __repr__(self):
        return f"Högprioärende: id={self.id}, kund={self.kund}, kategori={self.kategori}, status={self.status}"


with open("supportarenden.csv", "r", encoding="utf-8") as file:

    reader = csv.reader(file)
    headers = next(reader, None)

    support = {}
    for h in headers:
        support[h] = []

    for row in reader:
        for h, v in zip(headers, row):
            support[h].append(v)


support_objects = []

for i in range(len(support["id"])):
    obj = Support(
        id=support["id"][i],
        kund=support["kund"][i],
        kategori=support["kategori"][i],
        prioritet=support["prioritet"][i],
        status=support["status"][i]
    )
    support_objects.append(obj)

hog_prioritet = [obj for obj in support_objects if obj.high_priority()]

for customer in hog_prioritet:
    print(customer)