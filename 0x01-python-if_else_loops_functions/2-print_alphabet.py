for alpha_letters in range(ord('a'), ord('z')+1):
    if alpha_letters == 'e' or alpha_letters == 'q':
       continue
    print("{:s}".format(alpha_letters), end="")
