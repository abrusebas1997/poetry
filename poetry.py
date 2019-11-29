import random



poem = """
Because the time is ripe, the age is ready,
Because the world her woman’s help demands,
Out of the long subjection and seclusion
Come to our field of warfare and confusion
The mother's heart and hands.
Long has she stood aside, endured and waited,
While man swung forward, toiling on alone;
Now, for the weary man, so long ill-mated,
Now, for the world for which she was created,
Comes woman to her own.
Not for herself! though sweet the air of freedom;
Not for herself, though dear the new-born power;
But for the child, who needs a nobler mother,
For the whole people, needing one another,
Comes woman to her hour.
"""



lines_list = poem.split("\n")

def lines_printed_backwards(lines_list):

    """Your code should implement the lines_printed_backwards() function. This function takes in a list of strings containing the lines of your poem as arguments and will print the poem lines out in reverse with the line numbers reversed."""
    lines_list.reverse()

    # TODO: Reverse the loop
    new_list = []
    count = 0
    for lines in lines_list:
        count += 1
        new_list.append(str(count) + ". " + lines)
    # print(count)
    print(new_list)
    # TODO: use loop to print out items in list


def lines_printed_random(lines_list):
    """Your code should implement the lines_printed_random() function which will randomly select lines from a list of strings and print them out in random order. Repeats are okay and the number of lines printed should be equal to the original number of lines in the poem (line numbers don't need to be printed). Hint: try using a loop and randint()"""

    for lines in lines_list:
        print(random.choice(lines_list))


def my_costum_function(lines_list):
    """"Your code should implement a function of your choice that rearranges the poem in a unique way, be creative! Make sure that you carefully comment your custom function so it's clear what it does."""
    # IT's going to delete the last line
    for lines in lines_list:
        lines_list.pop()
    print(lines_list)

lines_printed_backwards(lines_list)
print("\n\n")
lines_printed_random(lines_list)
my_costum_function(lines_list)
