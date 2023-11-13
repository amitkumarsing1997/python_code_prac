#169
#Generators vs Normal Collections wrt Performance
import random
import time
names=["Sunny",'Bunny',"Chinny","Vinny"]
subjects=["Python","Java","Blockchain"]

def people_list(num_people):
    results=[]
    for i in range(num_people):
        person={
            "id":i,
            "name":random.choice(names),
            "subject":random.choice(subjects)
        }
        results.append(person)
    return results

def people_generator(num_people):
    for i in range(num_people):
        person={
            "id":i,
            "name":random.choice(names),
            "subject":random.choice(subjects)
        }
        yield person


t1=time.process_time()
people=people_list(10000000)
t2=time.process_time()

# t1=time.process_time()
# people=people_generator(10000000)
# t2=time.process_time()

print("Took {}".format(t2-t1))



##Generator vs Normal Collections wrt Memory Utilization  