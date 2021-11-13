import sys
import db_client as cl

def print_actions(cl_actions):
    print('Actions: \n')
    for act in cl_actions:
        print(f'{act}: {cl_actions[act].__name__}')


def print_commands():
    print('Available commands: \n')
    print('exec - Выполнить команду\nquit - Закончить работу')


def main():
    try:
        client = cl.db_client(sys.argv[1], sys.argv[2])
        client_actions = client.get_user_actions()
        mainloop = True
        while mainloop:
            print_commands()
            comm = input()

            if comm == 'quit':
                mainloop = False
            elif comm == 'exec':
                print_actions(client_actions)
                func = int(input())
                client_actions[int(func)]()
            else:
                print("Unknown command. Please retry")

        del client
        return 0
    except Exception as _ex:
        print(_ex)
        return -1


if __name__ == "__main__":
    main()
