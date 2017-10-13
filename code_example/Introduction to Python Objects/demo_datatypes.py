"""
Demo representation of native data structures available in python

"""


def run():
    print("Even though Python is dynamically typed language its a strictly typed language"
          " i.e. every  object or data structure is categorized as a specific type. \n "
          "This type also decides the operations which can be performed on that object. "
          "We will be covering: int, float, str, list, boolean,dictionary, sets & tuples")

    # Preview of built-in objects in Python
    tab_space = "\t" * 4
    newline = "\n"
    table_border = "-" * 70
    header_column = "Object Type" + tab_space + "Example Literal/creation"
    header = table_border + newline + header_column + newline + table_border
    print(header)

    # \todo\ 1.Fix the formatting to correctly align the table content

    number_row = "Numbers" + tab_space + "1234, 3.145, 0b111, Decimal(), Fraction()"
    string_row = newline + "Strings" + tab_space + "'sapm', \"Bob's\" , u'sp\xc4m' "
    list_row = newline + "Lists" + tab_space + "[1,[2,'three'],4.5 ], list(range(10)) "
    dictionary_row = newline + "Dictionary" + tab_space + "{'one':1, 2:'two'} , dict(hoursinday=24)"
    sets_row = newline + "Sets" + tab_space + "set('s','p','a','a','m'), {1,2,3,4}"
    tuple_row = newline + "Tuple" + tab_space + "tuple('spam'), (1,2,3,4)"
    other_row = newline + "Other types" + tab_space + "Booleans, None, files, types"


    print(number_row,  string_row, list_row, dictionary_row, tuple_row, sets_row, other_row)







if __name__ == "__main__":
    run()

