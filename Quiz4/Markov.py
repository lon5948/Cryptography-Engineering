def count(reference):
    size = len(reference)
    double = {}
    triple = {}
    
    for i in range(size-2):
        string = ""
        string += reference[i]
        string += reference[i+1]
        
        if string in double:
            double[string] += 1
        else:
            double[string] = 1
            
        string += reference[i+2]
        
        if string in double:
            triple[string] += 1
        else:
            triple[string] = 1
        
    return double, triple
    

def value(cipher,m,n):

    size = len(cipher)

    list = [0]*m
    vowel = n*0.4

    for i in range(size):
        if cipher[i] == 'A' or cipher[i] == 'E' or cipher[i] == 'I' or cipher[i] == 'O' or cipher[i] == 'U':
            list[i%m] += 1

    total = 0 

    for i in range(m):
        total += abs(list[i]-vowel)

    return total


def dimension(cipher,m,n):
    
    total1 = value(cipher,m,n)
    total2 = value(cipher,n,m)
    
    if(total1<total2):
        return m , n
    else:
        return n , m


def classify(cipher,group_num,length):
    group = [0]*group_num
    
    for i in range(group_num):
        group[i] = cipher[i*length:(i+1)*length]
    
    swap(group,0,2)
    swap(group,1,5)
    
    return group


def swap(group,ind1,ind2):    
    temp = group[ind1]
    group[ind1] = group[ind2]
    group[ind2] = temp


def Markov(reference,cipher):
    
    double, triple = count(reference)
    
    length,group_num = dimension(cipher,7,11)
    
    group = classify(cipher,group_num,length)
    
    for i in range(group_num-2):
        max_prob = 0
        for j in range(i+2,group_num):
            prob = 0
            for k in range(length):
                dou = ""
                dou += group[i][k]
                dou += group[i+1][k]
                tri = ""
                tri += group[i][k]
                tri += group[i+1][k]
                tri += group[j][k]
                if dou in double and tri in triple:
                    prob += triple[tri]/double[dou]
            if prob > max_prob:
                max_prob = prob
                max_index = j
        swap(group,max_index,i+2)
        
    for i in range(length):
        for j in range(group_num):
            print(group[j][i],end = '')
        

reference = "WITHMALICETOWARDNONEWITHCHARITYFORALLWITHFIRMNESSINTHERIGHTASGODGIVESUSTOSEETHERIGHTLETUSS\
TRIVEONTOFINISHTHEWORKWEAREINTOBINDUPTHENATIONSWOUNDSTOCAREFORHIMWHOSHALLHAVEBORNETHEBATTLEANDFORHISWIDOW\
ANDHISORP ANTODOALLWHICHMAYACHIEVEANDCHERISHAJUSTANDLASTINGPEACEAMONGOURSELVESANDWITHALLNATIONSGREECEANNO\
UNCEDYESTERDAYTHEAGRAGREEMENTWITHTRUKEYENDTHECYPRUSTHATTHEGREEKANDTURKISHCONTINGENTSWHICHARETOPARTICIPATE\
INTHETRIPARTITEHEADQUARTERSSHALLCOMPRISERESPECTIVELYGREEKOFFICERSNONCOMMISSIONEDOFFICERSANDMENANDTURKISHO\
FFICERSNONCOMMISSIONEDOFFICERSANDMENTHEPRESIDENTANDVICEPRESIDENTOFTHEREPUBLICOFCYPRUSACTINGINAGREEMENTMAY\
REQUESTTHEGREEKANDTURKISHGOVERNMENTSTOINCREASEORREDUCETHEGREEKANDTURKISHCONTINGENTSITISAGREEDTHATTHESITES\
OFTHECANTONMENTSFORTHEGREEKANDTURKISHCONTINGENTSPARTICIPATINGINTHETRIPARTITEHEADQUARTERSTHEIRJURIDICALSTA\
TUSFACILITIESANDEXEMPTIONSINRESPECTOFCUSTOMSANDTAXESASWELLASOTHERIMMUNITIESANDPRIVILEGESANDANYOTHERMILITA\
RYANDTECHNICALQUESTIONSCONCERNINGTHEORGANIZATIONANDOPERATIONOFTHEHEADQUARTERSMENTIONEDABOVESHALLBEDETERMI\
NEDBYASPECIALCONVENTIONWHICHSHALLCOMEINTOFORCENOTLATERTHANTHETREATYOFALLIANCE"

cipher = 'EOEYEGTRNPSECEHHETYHSNGNDDDDETOCRAERAEMHTECSEUSIARWKDRIRNYARANUEYICNTTCEIETUS'

Markov(reference,cipher)










    
