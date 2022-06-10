# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    for i in range(2):
        print(111)

    with open('all_train_so.txt', 'a+', encoding='utf-8') as fj:
        for j in range(5600):
            try:
                i = '' + str(j)
                f = open('./society/60' + i + '_society.txt', 'r', encoding='utf-8')
                print(fj.write(f.read()))
                f.close()
            except:
                print(j)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
