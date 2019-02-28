#! usr/bin/env python
"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.

The string
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1
contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.

We are interested in finding the longest (number of characters) absolute path to
a file within our file system. For example, in the second example above, the
longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is
32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to a file in the abstracted file system. If
there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.



My approach:

Using "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", I want to find the most number
of \n\t*X and back out to get the solution.

Recursion feels the best way to do this -- continuously split by \t until you
get the shortest length list.


"""
def find_shortest_fragment(s):
    """This feels _way_ too complicated"""
    # split by tabs
    list_of_fragments = [x.split('\t') for x in s.split('\n')]
    # get only file names
    list_of_fragments = filter(lambda x: len(x[-1].split('.'))>1, list_of_fragments)
    # get the deepest file by counting number of blanks -- '\t'
    deepest_file = sorted(list_of_fragments, key=len, reverse=True)[0]
    return(deepest_file[-1])

def find_deepest_fragment(s):
    """Find deepest file in O(n) time"""
    A = s.split('\t')
    longest_counter = 0
    longest_file = ''
    counter = 0
    for i in A:
        if i == '':  # catch blanks first
            counter += 1
        elif counter > longest_counter and len(i.split('.')) > 1:
            longest_counter = counter
            longest_file = i
            counter = 0

    return longest_file, len(longest_file)



def find_absolute_longest_path(s,longest_file,length_of_longest):
    """
    Assumptions:
      * they all begin with some dir (not a \n or \t)
    """
    i = s.index(longest_file);
    print(s.split('\n\t'))

    return s[s.index(longest_file):]


if __name__ == "__main__":
    #print(find_deepest_fragment("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    #print(find_deepest_fragment("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

    longest, length_of = find_deepest_fragment("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    print(find_absolute_longest_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
            longest, length_of))
    #print(find_absolute_longest_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
