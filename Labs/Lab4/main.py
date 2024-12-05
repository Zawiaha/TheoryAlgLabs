import generatorFun

def main():
    choice = int(input("Номер задания(1-3)?: "))
    if choice == 1:
        generatorFun.printDigitCombination()
    elif choice == 2:
        generatorFun.printFunctionValues()
    else:
        generatorFun.printSortedDict()

if __name__ == "__main__":
    main()
