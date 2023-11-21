from cookie_parser import most_common_cookie
import csv

def empty_sheet(capsys):
    """
    Tests empty csv, should return empty string
    """
    assert cookie_parser.main(['empty.csv', '2019-12-09'])
    
    out, err = capsys.readouterr()
    assert out == ""

def empty_string(capsys):
    """
    tests csv where cookies of a given date are not found.  
    Should return empty string.
    """
    assert cookie_parser.main(['cookies.csv', '2019-12-07'])
    out, err = capsys.readouterr()

    assert out == ""
    

def one_cookie(capsys):
    """
    Tests where there is one cookie that is the most common.
    """
    assert cookie_parser.main(['cookies.csv', '2019-12-09']) 
    out, err = capsys.readouterr()
    assert out == "D\n"

def various_cookies(capsys):
    """
    Tests where there are various cookies that are the most common. 
    """
    assert cookie_parser.main(['cookies.csv', '2019-12-08'])
    out, err = capsys.readouterr()
    assert out == "A\nC\nD\n"


def main():
    empty_sheet()
    empty_string()
    one_cookie()
    various_cookies()


if __name__ == '__main__':
    main()
