#Class for creating certificateholder objects.
class certHolder(object):
    #Class for testing purposes: creates objects of cert. holders.

    def __init__(self,name,amount_of_guests):
        self.name = name
        self.amount_of_guests = amount_of_guests

    def __repr__(self):
        return "(%s, %d)" %(self.name,self.amount_of_guests)

class wally_box(object):
    #Class for making seating planning
    CH_sorted = []

    def __init__(self,CH):
        self.CH = CH

    def print_input(self): #Prints input (TEST)
        print (self.CH)
        print ("")

    def getSeatings(self):
        '''
        Performs seat configuration algorithm.
        '''
        import random

        #Re-organise the list of object based on groupsize:
 #===============================================================================================================================
        guests = []
        for holder in self.CH:
            guests.append((holder.amount_of_guests)+1)

        gmi = [] #guest_max_index
        count_to = (len(guests))-1
        v = 0
        while v <= count_to:
            if max(guests) > 1:
                gmi.append(guests.index((max(guests))))
                guests[guests.index((max(guests)))] = 0
            if max(guests) == 1:
                gmi.append(guests.index((max(guests))))
                guests[guests.index((max(guests)))] = 0
            v += 1

        for m in gmi:
            self.CH_sorted.append(self.CH[m])

        #print (self.CH_sorted)
        #print (self.CH_sorted[3].amount_of_guests)
#=================================================================================================================================
        """BEGIN algorithm placing certificateholders (CH) in their seats
        ##in such a manner that :
        ##A: they are not in the same seats as last week
        ##B: if a certificateholder comes with a group they will all be in adjacent seats"""
        try_again = 1
        number_of_tries = 0
        while try_again == 1: #It will remake a planning untill a possible one is found."""
            try_again = 0     #To make sure it runs again ONLY if it fails. """
            number_of_tries += 1 #keeps count of how many plannings were made.(can be removed)"""

            #BEGIN creating empty grid
            sections = 3
            rows = 3
            seats_in_row = 8

            schema = []
            for x in range(sections):
                schema.append(x)
                section_rows=[]
                for j in range(rows):
                    section_rows.append([0]*seats_in_row)
                schema[x] = section_rows

            #END creating empty grid

            guests_total = 0
            for holder in self.CH:
                guests_total += holder.amount_of_guests+1

            if guests_total > rows*seats_in_row*sections:
                print ("There are more guests than there are seats")
                break

            for holder in self.CH_sorted:

                if holder.amount_of_guests+1 > rows*seats_in_row:
                    guests_left = holder.amount_of_guests + 1 # + the CH
                    cnt = 0
                    for section in schema:
                        for row in section:
                            for seat in row:
                                if guests_left > 0:
                                    if row[cnt] == 0:
                                        row[cnt] = holder.name
                                        cnt += 1
                                        guests_left -= 1
                                        if cnt == len(row):
                                            cnt = 0




                elif holder.amount_of_guests > 0 :  #places the CH's WITH guests in the seating planning."""
                    i = 0
                    guests_left = holder.amount_of_guests #important counter when placing guests around CH."""
                    while i == 0 :
                        in_section = (random.randint(0,(sections-1)))
                        x = (random.randint(0,(seats_in_row-1)))
                        y = (random.randint(0,(rows-1)))
                        if schema[in_section][y][x] == 0:
                            schema[in_section][y][x] = holder.name  #The CH has now been placed.In the following code
                            #his guests will be placed around him where seats are available""""BEGIN"""

                            ri = 1  #r(ight)i(ndex) and l(eft)i(ndex) keep track of which
                            li = 1  #seats have already been assigned to a guest and where to place the next.
                            ui = 1  #u(p)i(ndex)
                            di = 1  #d(own)i(ndex)

                            while guests_left > 0: #This loop will check if a seat adjacent to the CH or
                                #guest is free, and if so it places another guest there, until there are no more guests."""
                                if schema[in_section][y][x] == 0:
                                    schema[in_section][y][x] = holder.name
                                    guests_left -= 1
                                    ri = 1
                                    li = 1
                                    ui = 1
                                    di = 1
                                elif x+ri <= (seats_in_row-1) and schema[in_section][y][x+ri] == 0 :
                                    schema[in_section][y][x+ri] = holder.name
                                    guests_left -= 1
                                    ri += 1
                                elif x-li >= 0 and schema[in_section][y][x-li] == 0 and guests_left>0:
                                    schema[in_section][y][x-li] = holder.name
                                    guests_left -= 1
                                    li += 1
                                elif y+di <=(rows-1) and schema[in_section][y+di][x] == 0 :
                                    y = y + di  #Placement is done in the first IF statement
                                elif y-ui >=0 and schema[in_section][y-ui][x] == 0 :
                                    y = y - ui  #Placement is done in the first IF statement
                                else:
                                    try_again = 1    #apparently the current planning doesn't work, so a new planning will be made.
                                    guests_left = 0 #is set to 0 to end the current loop and restart the whole planning.

                            i = 1
                        else:
                            i = 0

                elif holder.amount_of_guests == 0 :#This loop randomly places the CH's that don't bring guests"""
                    i = 0
                    while i == 0:
                        in_section = (random.randint(0,(sections-1)))
                        x = (random.randint(0,(seats_in_row-1)))
                        y = (random.randint(0,(rows-1)))
                        if schema[in_section][y][x] == 0:
                            schema[in_section][y][x] = holder.name
                            i = 1
                        else:
                            i = 0

        #print result
        for x in schema:
            for j in x:
                print (j)
            print ("",)

        #Counts and prints the amount of free seats left:
        free_spots = 0
        for x in schema:
            for j in x:
                for z in j:
                    if z == 0:
                        free_spots +=1
        print("Aantal vrije plaatsen:",free_spots)





#Things outside the class
camille = certHolder("Camille",24)
eshua = certHolder("Eshua",3)
john = certHolder("John",2)
sjaak = certHolder("Sjaak", 0)
#berta = certHolder("Berta",0)
##hans = certHolder("Hans",4)
##ingrid = certHolder("Ingrid",0)
##jake = certHolder("Jake",3)
##bastiaan = certHolder("Bastiaan",3)
##hank = certHolder("Hank",2)
##connie = certHolder("Connie", 2)
##maria = certHolder("Maria", 1)
##ariana = certHolder("Ariana", 1)
##maximus = certHolder("Maxima",3)

CertificaatHouders = [camille, eshua,john,sjaak]#test list

WBox = wally_box(CertificaatHouders)
WBox.print_input()
WBox.getSeatings()
