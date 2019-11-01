class Finder:
    def __init__(self, string_array):
        self.string_array = string_array
        self.map_of_string_array = {}

        # Create map of the string array. The map contains the characters and the occurrences of the character
        for string in string_array:
            if isinstance(string, str):
                content_count = {}
                for char in string:
                    if char not in content_count:
                        content_count[char] = 1
                    else:
                        content_count[char] = content_count[char] + 1
                self.map_of_string_array[string] = content_count

    def find(self, string):
        # returns an array of the strings that have the right contents
        solutions = []

        # Make map of input string
        content_count = {}
        for char in string:
            if char not in content_count:
                content_count[char] = 1
            else:
                content_count[char] = content_count[char] + 1

        # Compare map of input string to the maps in string_array
        for key, item in self.map_of_string_array.items():
            if len(item) == len(content_count):
                # match will be changed to False if the map is not the same
                match = True
                for char_key, char_count in content_count.items():
                    # if the character total is not the same in both strings
                    if char_key in item.keys():
                        if item[char_key] != char_count:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    # Add the string with the right characters to the solutions
                    solutions.append(key)
        return solutions
