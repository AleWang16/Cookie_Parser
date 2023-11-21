from cookie_parser import most_common_cookie
import csv

def empty_sheet():
    s = most_common_cookie(empty.csv)
    assert(s == "")

def empty_string():
    s = most_common_cookie()

def one_cookie():
    pass 

def various_cookies():
    pass

def various_dates():
    pass



def main():
    empty_sheet()
    empty_string()
    one_cookie()
    various_cookies()
    various_dates()


if __name__ == '__main__':
    main()