fin = open("elements.in", "r")
lines = fin.read().splitlines()
print ("Welcome! Here you can enter the atomic number of a element and we can give you information on the element")
print ("Information are from Wikipedia and ptable.com")
print (" ")
def main():
    element = 200
    while True:
        try:
            print("What is the atomic number of the element you wish to know? ")
            element = int(input())
            user_line = 2*(element - 1)
            if (element < 1):
                print ("Atomic numebr can't be negative or zero ")
                return ("again")
            try:
                info = lines[user_line]
            except(IndexError):
                print("There's only 118 elements... ")
                print (" ")
                return ("again")
        except(ValueError):
            print("Integer plz ")
            print(" ")
            return ("again")
        print (info)
        print(" ")
        user_more_info = ""
        print("Do you want more information? ")
        while user_more_info != ("yes") and user_more_info != ("no"):
            print("Enter yes or no ")
            user_more_info = input()
            user_more_info = "".join(user_more_info.split())
            user_more_info = user_more_info.lower()
        if (user_more_info == "yes"):
            info_line = 2*(element-1) + 1
            more_info = lines[info_line]
            print (more_info)
            print ("")
        print("Do you want info on another element? ")
        again = input()
        again = "".join(again.split())
        again = again.lower()
        if (again == "no"):
            return ("done")
        else:
            print ("")
            None
result = ""
while result != "done":
    result = main()
print ("Thank you for using this program! ")