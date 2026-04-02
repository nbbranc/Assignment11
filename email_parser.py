'''
    Walker Yturbides
    CS5001, Fall 2025
    Practice Exam

    Exam Review - Practice Problems.
    Email Parser sampling.
'''

# 1) Pure .split() version (simple & idiomatic)
def email_process(email: str):
    """
    Expects 'lastname.firstname@northeastern.edu'
    Returns [[lastname, firstname], [northeastern, edu]]
    """
    local, domain = email.strip().lower().split('@')
    last, first = local.split('.', 1)
    host, tld   = domain.split('.', 1)
    return [[last, first], [host, tld]]


def email_process2(email: str) -> list:
    # Hard Code Approach.
    return_list: list = []
 
    # [lastname, firstname@northeastern, edu]
    list_split_by_dot: list = email.split(".")
 
    # [firstname, northeastern]
    list_split_by_mouse: list = list_split_by_dot[1].split("@")
 
    name_list: list = [list_split_by_dot[0],list_split_by_mouse[0]]
    email_list: list = [list_split_by_mouse[1],list_split_by_dot[2]]
 
    return_list = [name_list,email_list]
    return return_list

def main():
    lst= "last.first@nu.edu"
    actual_lst = email_process(lst)
    print(actual_lst)
    # print(help(str))

if __name__ == "__main__":
    main()