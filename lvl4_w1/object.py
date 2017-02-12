class PartyAnimal:

    x = 0

    def party(self):
        self.x += 1
        print "So far", self.x

wat = PartyAnimal()

wat.party()
wat.party()
wat.party()