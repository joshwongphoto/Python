"""
File: searchengine.py
---------------------
CODE IN PLACE | FINAL PROJECT: Spring 2021
BBCNews Search Engine
This was an attempt to build a search engine using a reverse dictionary
AUTHOR: Josh Wong
"""


import os
import sys
import string

def common(list1, list2):  #MILESTONE 1
    """
    PRE: list1 and list 2 are a list
    POST: returns new_list
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    """
    new_list = []
    list1_length = len(list1)
    list2_length = len(list2)
    for i in range (list1_length):
        for j in range (list2_length):
            if list1[i] == list2[j]:
                new_list_length = len(new_list)
                new_list.append(format(list1[i]))
                for x in range(new_list_length):
                    if new_list[x] == list1[i]:
                        new_list.pop()
    return new_list


def create_index(filenames, index, file_titles):  #MILESTONE 2
    """
    This function is passed:
        filenames:      a list of file names (strings)

        index:          a dictionary mapping from terms to file names (i.e., inverted index)
                        (term -> list of file names that contain that term)

        file_titles:    a dictionary mapping from a file names to the title of the article
                        in a given file
                        (file name -> title of article in that file)

    The function will update the index passed in to include the terms in the files
    in the list filenames.  Also, the file_titles dictionary will be updated to
    include files in the list of filenames.

    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title'}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test2.txt'], index, file_titles)
    >>> index
    {'file': ['test2.txt'], '2': ['test2.txt'], 'title': ['test2.txt'], 'ball': ['test2.txt'], 'carrot': ['test2.txt'], 'dog': ['test2.txt']}
    >>> file_titles
    {'test2.txt': 'File 2 Title'}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt', 'test2.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt', 'test2.txt'], '1': ['test1.txt'], 'title': ['test1.txt', 'test2.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt', 'test2.txt'], 'carrot': ['test1.txt', 'test2.txt'], '2': ['test2.txt'], 'dog': ['test2.txt']}
    >>> index = {}
    >>> file_titles = {}
    >>> create_index(['test1.txt', 'test2.txt', 'test2.txt'], index, file_titles)
    >>> index
    {'file': ['test1.txt', 'test2.txt'], '1': ['test1.txt'], 'title': ['test1.txt', 'test2.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt', 'test2.txt'], 'carrot': ['test1.txt', 'test2.txt'], '2': ['test2.txt'], 'dog': ['test2.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title', 'test2.txt': 'File 2 Title'}
    >>> index = {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles = {'test1.txt': 'File 1 Title'}
    >>> create_index([], index, file_titles)
    >>> index
    {'file': ['test1.txt'], '1': ['test1.txt'], 'title': ['test1.txt'], 'apple': ['test1.txt'], 'ball': ['test1.txt'], 'carrot': ['test1.txt']}
    >>> file_titles
    {'test1.txt': 'File 1 Title'}
    """
    #print ("Filenames:", filenames)
    length = len(filenames)
    print(length, "Filenames detected in the directory")
    #get filenames and open and read
    #loop through each file and open and read the contents of the file.
    #Process the contents and store in to the index
    # Build the index

    for i in range(length):  #Loop through the number of files in the directory
        name_of_file = filenames[i]
        file_titles_names = filenames[i]
        filename_list = []  # initialize and create the empty list
        # Build the index

        with open(name_of_file) as f:
            #clean_filename = strip_directory_name(name_of_file)
            clean_filename = name_of_file
            filename_list = [clean_filename]
            #print("PROCESSING FILE: ", count+1)
            for line in f:
                new_line = format_clean_string(line)
                new_line = new_line.lower()
                new_line_list = new_line.split()  #convert the line into list.
                new_line_list_length = len(new_line_list)  # get the length of the new created list of the line

                for each_element in range (new_line_list_length):
                    filename_list = [clean_filename]
                    key = index.get(new_line_list[each_element])
                    value = index.get(new_line_list[each_element])
                    #print ("KEY = ",new_line_list[each_element]," CURRENT VALUE: ", value)
                    if key != None:
                        #print ("key", new_line_list[each_element] , "already exist: Appending filename!" , value )
                        getlist = index.get(new_line_list[each_element])
                        getlist.append(clean_filename)
                        #print("GETLIST AFTER APPEND:", getlist, "GETLIST LENGTH:", len(getlist) )
                        #put the appended list back in the key value
                        key = new_line_list[each_element]
                        #print("Inserting:",getlist , "into: ", key)
                        index[key] = getlist

                        # use that length and process each element in the list
                        #each element in the new_line_list becomes a key. The file name becomes the value
                        #index[new_line_list[each_element]]=filename_list  #each put the key and key value into  the index:
                    else:
                        #print("Adding:", filename_list, "to index key: ", new_line_list[each_element])
                        index[new_line_list[each_element]] = filename_list

                    # clear out the list.
                    getlist = []
                    filename_list = []

        #Build the Dictionary for File_Titles
        with open(file_titles_names) as dictionary_f:
            first_line = dictionary_f.readline()
            #file_titles_names = strip_directory_name(file_titles_names)
            first_line = format_clean_string(first_line)
            file_titles[file_titles_names] = first_line.rstrip()

    #print("INDEX BUILD COMPLETE", index)
    #print("FILE_TITLE BUILD COMPLETE", file_titles)

def search(index, query):   # MILESTONE 3
    """
    This function is passed:
        index:      a dictionary mapping from terms to file names (inverted index)
                    (term -> list of file names that contain that term)

        query  :    a query (string), where any letters will be lowercase

    The function returns a list of the names of all the files that contain *all* of the
    terms in the query (using the index passed in).

    >>> index = {}
    >>> create_index(['test1.txt', 'test2.txt'], index, {})
    >>> search(index, 'apple')
    ['test1.txt']
    >>> search(index, 'ball')
    ['test1.txt', 'test2.txt']
    >>> search(index, 'file')
    ['test1.txt', 'test2.txt']
    >>> search(index, '2')
    ['test2.txt']
    >>> search(index, 'carrot')
    ['test1.txt', 'test2.txt']
    >>> search(index, 'dog')
    ['test2.txt']
    >>> search(index, 'nope')
    []
    >>> search(index, 'apple carrot')
    ['test1.txt']
    >>> search(index, 'apple ball file')
    ['test1.txt']
    >>> search(index, 'apple ball nope')
    []
    """
    query = query.strip(string.punctuation)
    #convert the query into a list
    make_list_from_query = query.split()
    #print("Result of turning the query in a list = ", make_list_from_query)
    index_keys_as_list = list(index.keys())
    #print ("Result of turning index to a list:",index_keys_as_list)
    common_result = common(make_list_from_query, index_keys_as_list)
    #print("The items in common =", common_result)

    common_list_length = len(common_result)
    #print ("common_list_length =", common_list_length)
    result_list = []
    for i in range(common_list_length):
        key = index.get(common_result[i])
        key_name = common_result[i]
        key_value = key
        #print("KEY = ", key_name, "CONTAINS THE VALUE = ", key_value, "KEY:", key)
        if len(result_list) == 0: #if empty just append to the list.
            #print ("EMPTY LIST --> APPENDING KEY VALUE= ", key_value)

            result_list.extend(key_value)
            #print("APPEND TO EMPTY LIST ---> result_list = ", result_list)
        else: # it is not empty so we use the common function again to get a new list with just the common items.
            #print("LIST NOT EMPTY NEED TO COMPARE KEY VALUES= ", key_value, "WITH: ", result_list)
            new_list = common(result_list,key_value)  #overwrite the result_list with a new result_list
            #print("new list result_list = ", new_list)
            result_list = new_list
    #print(result_list)
    #exit(1)
    return result_list


def format_clean_string(my_string):

    my_string = my_string.strip()
    my_string = ''.join([i for i in my_string if i not in string.punctuation])
    #my_string = my_string.lower()
    return my_string

def strip_directory_name(name_of_file):
    compare = '\\'  #Windows
    compare2 = '/'  #Mac/Unix OS
    if name_of_file.find(compare) or name_of_file.find(compare2):
        mark_string_position = name_of_file.find(compare)
        back_part = name_of_file[mark_string_position + 1:]
        #print("Fixed Name:", back_part)
        return back_part



##### YOU SHOULD NOT NEED TO MODIFY ANY CODE BELOW THIS LINE (UNLESS YOU'RE ADDING EXTENSIONS) #####

def do_searches(index, file_titles):
    """
    This function is given an inverted index and a dictionary mapping from
    file names to the titles of articles in those files.  It allows the user
    to run searches against the data in that index.
    """
    while True:
        query = input("Query (empty query to stop): ")
        query = query.lower()                   # convert query to lowercase
        if query == '':
            break
        results = search(index, query)


        # display query results
        print("Results for query '" + query + "':")
        if results:                             # check for non-empty results list
            for i in range(len(results)):
                title = file_titles[results[i]]
                print(str(i + 1) + ".  Title: " + title + ",  File: " + results[i])
        else:
            print("No results match that query.")

def textfiles_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a valid directory, returns a list of the .txt
    file names within it.

    Input:
        directory (string): name of directory
    Returns:
        list of (string) names of .txt files in directory
    """
    filenames = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))

    return filenames


def main():
    """
    Usage: searchengine.py <file directory> -s
    The first argument specified should be the directory of text files that
    will be indexed/searched.  If the parameter -s is provided, then the
    user can interactively search (using the index).  Otherwise (if -s is
    not included), the index and the dictionary mapping file names to article
    titles are just printed on the console.
    """
    # Get command line arguments
    args = sys.argv[1:]

    num_args = len(args)
    if num_args < 1:
        print('Please specify directory of files to index as first argument.')
    else:
        # args[0] should be the folder containing all the files to index/search.
        directory = args[0]
        if os.path.exists(directory):
            # Build index from files in the given directory
            files = textfiles_in_dir(directory)
            index = {}          # index is empty to start
            file_titles = {}    # mapping of file names to article titles is empty to start
            create_index(files, index, file_titles)

            """
            print('Index:')
            print(index)
            print('File names -> document titles:')
            print(file_titles)
            """
        else:
            print('Directory "' + directory + '" does not exist.')


    query = input("Query (empty query to stop):")

    while query != "":
        print("Results for query", query)

        #result list contains the list of the file names that contain the query
        result_list = search(index, query)
        #print (result_list, "Length = ", len(result_list))
        result_list_length = len(result_list)
        if result_list_length == 0: #Empty list
            print("No results match that query.")
        else:
            #Matches FOUND
            #Loop through all the matched instances and print the result
            stored_dictionary = {}
            for i in range(result_list_length):
                retrieved_titles = file_titles[result_list[i]]
                print (str(i+1) + ". Title: " + str(retrieved_titles) +", File:",result_list[i])
                stored_dictionary[i] = str(result_list[i])
        #Go again or read the articles?
            read_articles(stored_dictionary)
        query = input("Query (empty query to stop): ")



"""
FUNCTION: read_articles
Passed Argument is a dictionary
Read the news articles after the search
"""
def read_articles(stored_dictionary):
    selection = input("Do you want to read the found articles? (Y/N)")
    if (selection == "Y" or selection=="y"):
        default = True
        length = len(stored_dictionary)
        while default:
            menu_number = int(input("Select the Article Number: (0: to Quit) "))

            if menu_number > 0 and menu_number <= length:
                #process the menu and open file for reading
                file_key_select = menu_number-1 #the menu number is 1 off so we need to subtract 1
                filename2 = stored_dictionary.get(file_key_select)
                with open(filename2) as f:
                    for line in f:
                        line = line.strip()
                        print(line)
            elif menu_number == 0: #invalid selection
                default = False
            else:
                print("Invalid Selection! ")

    else:
        pass


if __name__ == '__main__':
    main()