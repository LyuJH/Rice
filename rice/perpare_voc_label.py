labels = ['disease']
with open('dataset/voc/label_list.txt', 'w') as f:
    for lbl in labels:
        f.write(lbl + '\n')
