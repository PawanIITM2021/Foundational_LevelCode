'''scores_dataset={'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 
 'Mathematics': 94, 'Physics': 84, 'Chemistry': 79, 'Biology': 99, 
 'Computer Science': 88, 'History': 63, 'Civics': 88, 'Philosophy': 85}'''

def get_toppers(scores_dataset, subject, gender):
    max=0
    for x in scores_dataset:
        if gender in x.values():
             if subject in x.keys():
                if x[subject]>max:
                    max=x[subject]
    name_L=[]
    name=''
    for x in scores_dataset:
        if gender in x.values():
             if subject in x.keys():
                if x[subject]==max:
                    name=x['Name']
                    name_L.append(name)
    return name_L


             
      

          




           

