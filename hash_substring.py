# python3
# 221RDB386 Mārtiņš Nikiforovs 11.grupa
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    usrInpt = input();
    if 'I' in usrInpt:
        #inpt1 = input().strip();
        #inpt2 = input().strip();
        return (input().rstrip(), input().rstrip());
    # after input type choice
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern

    elif 'F' in usrInpt:
        with open('./tests/' + '06', 'r') as file:
     # return both lines in one return

    # this is the sample return, notice the rstrip function
           # return (input().rstrip(), input().rstrip());
            return (file.readline().rstrip(), file.readline().rstrip());


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    tHash = [];
    lenPattern = len(pattern);
    patHash = hash(pattern);
    lenText = len(text);

    for i in range(lenText - lenPattern + 1):
        iterVarOutpt = [];
        subStr = text[i:i + lenPattern];
        hashVal = hash(subStr);
        tHash.append(hashVal);
        tHashLen = len(tHash);

    if lenText < lenPattern:
        return iterVarOutpt;

    for i in range(tHashLen):
         #if i < (lenText-lenPattern):
            #tHash = (256*(tHash-ord('text[i])-(pow(lenPattern))')+ord(inpt1*[i+lenPattern]));
        if patHash == tHash[i] and text[i:i + lenPattern] == pattern:
            iterVarOutpt.append(i);

    # and return an iterable variable
    return iterVarOutpt;


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
