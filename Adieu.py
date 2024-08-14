#implement a program that prompts the user for names, one per line,
#until the user inputs control-d.
#Assume that the user will input at least one name.
#Then bid adieu to those names, separating two names with one and, three names with two commas and one and, an
#n names with (n-1) commas and one and, as in the below:
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


#special case when there is only one name in the names list.
#When there is only one name, the if statement inside the comma() function is executed
# adieu_msg is assigned to the first (and only) name in the list using names[0].


import inflect


def comma(names):
    n = len(names)
    if n == 1:
        adieu_msg = names[0]
    elif n == 2:
        adieu_msg = ' and '.join(names)
    else:
        adieu_msg = ', '.join(names[:-1]) + ', and ' + names[-1]

    return f"Adieu, adieu, to {adieu_msg}"


def main():
    names = [] #initialize empty list
    try:
        while True:
            name = input()
            names.append(name) #adds the value of name to the end of the names list.

    except EOFError:
        pass

    print(comma(names))

if __name__ == '__main__':
    main()
#implement a program that prompts the user for names, one per line,
#until the user inputs control-d.
#Assume that the user will input at least one name.
#Then bid adieu to those names, separating two names with one and, three names with two commas and one and, an
#n names with (n-1) commas and one and, as in the below:
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


#special case when there is only one name in the names list.
#When there is only one name, the if statement inside the comma() function is executed
# adieu_msg is assigned to the first (and only) name in the list using names[0].


import inflect


def comma(names):
    n = len(names)
    if n == 1:
        adieu_msg = names[0]
    elif n == 2:
        adieu_msg = ' and '.join(names)
    else:
        adieu_msg = ', '.join(names[:-1]) + ', and ' + names[-1]

    return f"Adieu, adieu, to {adieu_msg}"


def main():
    names = [] #initialize empty list
    try:
        while True:
            name = input()
            names.append(name) #adds the value of name to the end of the names list.

    except EOFError:
        pass

    print(comma(names))

if __name__ == '__main__':
    main()
