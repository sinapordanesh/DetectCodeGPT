
def main():

    A,B,C =map(int,input().split())
    
    if (A-C)*(B-C)>0:
        print("No")
    else:
        print("Yes")




if __name__ == "__main__":
    main()
