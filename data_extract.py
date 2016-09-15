def data_extract( file ):
    data = []
    all_the_text = file.readlines()
    for i in range(16,len(all_the_text)):
        data.append(all_the_text[i])
    row0 = []; row1 = []; row2 = []; row3 = [];
    signal = [row0, row1, row2, row3]
    # Dividing Strings
    for i in range(len(data)):
        data[i] = data[i].replace('\n','')
        data[i] = data[i].split('\t')
    # Make data rows
    for i in range(len(signal)):
        for j in range(len(data)):
            signal[i].append(data[j][i])
    return signal
file = open('example_file.txt')
try:
    data = data_extract(file)
    print(data[2])
finally:
    file.close()
