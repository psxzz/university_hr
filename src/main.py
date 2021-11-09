import sys
import db_client as cl

def main():
    try:
        client = cl.db_client(sys.argv[1], sys.argv[2])
        

    except Exception as _ex:
        print(_ex)
        return -1


if __name__ == "__main__":
    main()
