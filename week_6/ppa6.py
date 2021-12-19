def get_marks(scores_dataset, subject):
    L=[]
    for c in scores_dataset:
        L.append( (c['Name'],c[subject]) )
    return L