
import csv

file_name = "resources/spambase.data"

#load the data file
def load_data(fname):
    file = open(fname, 'r')
    train_set = []
    test_set = []
    count = 1
    # total_lines = len(file.readlines()) #4601
    for line in file:
        count +=1
        if count > 3:
            test_set.append(line)
            count = 0
        else:
            train_set.append(line)

    return train_set,test_set

def main():
    print "Running Spam classifier !!!"
    train_set, test_set  = load_data(file_name)
    print "train_set : ",len(train_set)," test_set: ",len(test_set)


main()