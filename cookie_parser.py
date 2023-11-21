import csv
import argparse


def main():

    parser = argparse.ArgumentParser(description='finds the most common cookie for a given date')

    # Add arguments
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('-d', '--date', help='date specified for cookie search')
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the parsed arguments
    input_file = args.input_file
    date = args.date
    
    res = most_common_cookie(input_file, date)
   
    print(res)
   
    return 0

def most_common_cookie(input_file, date) -> str:
    """
     Takes the csv input file  and the date for which 
     to search cookies, and return a string of the 
     most frequent cookies of the given date 
     sorted from the most to least recent timestamp.
     Returns an empty string if no cookies for the 
     criteria are found.
    """
    with open(input_file, "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        cookies = dict()
        most_freq_cookies = ""
        for row in reader_variable:
            # row[1][1:11] indicates the substring matching the date
            if row[1][1:11] == date:
                if row[0] in cookies:
                    cookies[row[0]] += 1
                else:
                    cookies[row[0]] = 1

        most_freq_cookies = retrieve_cookies(cookies)

        return most_freq_cookies

def retrieve_cookies(cookies_dict: dict) -> str:
    """
        Helper function for most_common_cookie.
        Returns a string of the most frequent cookies from greatest to least. 

    """
    #  print(cookies_dict)
    cookie_vals = list(cookies_dict.values())
    keys = list(cookies_dict.keys())
    cookies = ""
    max_val = max(cookie_vals)

    for i in range(len(cookie_vals) - 1, -1, -1):
        if cookie_vals[i] == max_val:
            cookies += keys[i] + "\n"
    
    return cookies
            

if __name__ == '__main__':
    main()