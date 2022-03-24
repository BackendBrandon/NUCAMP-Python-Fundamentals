def linear_search_dictionary(dict, target):
    for key in dict:
        if dict[key] == target:
            print("Success! Found at key", key)
        return key

    print("Failed to find value") 
    return None


my_dictionary = {"red":5,"blue":3,"yellow":12, "green":7}
linear_search_dictionary(my_dictionary,5)
linear_search_dictionary(my_dictionary,3)
linear_search_dictionary(my_dictionary,8)
