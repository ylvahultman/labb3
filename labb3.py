import csv

class Support:

    def __init__(self, id, kund, kategori, prioritet, status):
        self.id = id
        self.kund = kund
        self.kategori = kategori
        self.prioritet = prioritet
        self.status = status

    def beskriv(self):
    
        return (
            f"ID: {self.id} | "
            f"Kund: {self.kund} | "
            f"Kategori: {self.kategori} | "
            f"Prioritet: {self.prioritet} | "
            f"Status: {self.status}"
        )

tickets = []

with open("supportarenden.csv", mode="r", encoding="utf-8", newline="") as csvfile:

    reader = csv.DictReader(csvfile)
    
    for row in reader:
        ticket = Support(
            id=row["id"],
            kund=row["kund"],
            kategori=row["kategori"],
            prioritet=row["prioritet"],
            status=row["status"]
        )
 
        tickets.append(ticket)


    for ticket in tickets:
        print(ticket.beskriv())







# supporttickets = []


    # def beskrivning(self):
    #     return(
    #         f'
    #     )


# with open("supportarenden.csv", newline='', encoding="utf-8") as csvfile:

#     reader = csv.DictReader(csvfile) 

#     for row in reader:
#        ticket = {
#             "id": row["id"],
#             "kund": row["kund"],
#             "kategori": row["kategori"],
#             "prioritet": row["prioritet"],
#             "status": row["status"]}
#        supporttickets.append(ticket)

# print(supporttickets)


#     for row in reader:

#         print(row['id'], row['kund'], row['kategori'], row['prioritet'], row['status'])
 
# print(row)

#  id,kund,kategori,prioritet,status