days = [1,2,3,4,5]
#d = {'a':[1], 'b':[3,4],'c':[5],'d':[2,4]}
#d = {'a':[1], 'b':[2],'c':[5],'d':[2,5]}
#d = {'a':[1,5], 'b':[3,5],'c':[5],'d':[2,5]}
#d = {'a':[1], 'b':[2],'c':[3],'d':[4]}
d = {'a':[1,2], 'b':[2,3]}
counts = {}
res=[]


if __name__ == '__main__':
    #print(counts)
    while len(d) > 0:
    #for i in range(0, 3):
        counts = {} #reset number of days found for people in d
        for day in days:
            if day not in counts:
                counts[day] = 0
            for key, value in d.items():
                if day in value:
                    counts[day]+=1 #count the number of times a day shows up for people in d
        
        for k, v in list(counts.items()):
            if v == 0:
                del counts[k] #get rid of a day where no people in d had available
                days.remove(k) #remove that day from the days array
        #print('Counts:',counts)
        maxday = max(counts, key=counts.get) #get the most common day
        #print(maxday)
        res.append(maxday) #add the most common day to answer array
        del counts[maxday] #remove maxday since we already chose it as an answer
        
        
        for k, v in list(d.items()):
            if maxday in v:
                #print('in v')
                del d[k] #remove maxday from everyone's availability from people in d
                #print("Dict:",d)


        #print(len(counts))
                
    print('Days=',res) #print solution
    
        