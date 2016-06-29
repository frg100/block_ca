# block_ca
Python module for evolving a block cellular automata

"A block cellular automaton or partitioning cellular automaton is a special kind of cellular automaton in which the lattice of cells is divided into non-overlapping blocks (with different partitions at different time steps) and the transition rule is applied to a whole block at a time rather than a single cell"         -[Wikipedia](https://en.wikipedia.org/wiki/Block_cellular_automaton)

One of the more famous examples of a block cellular automata that uses the margolus neighborhood is the [__Critters Rule](https://en.wikipedia.org/wiki/Critters_(block_cellular_automaton))


Functions and docstrings:

```
def open_file(file_name):

    Opens a file and creates a dish of all the bits of the file
    --------------
    file_name : string
        The file name specifies which file to open, assuming it is in the same directory as the program.
    Returns
    --------------
    dish : list
        A 2D nested array. This dish now contains all the information in the file with each bit reading like an english sentence. The first bits start at the top and move right and once the end of the line is reached, the bit order continues on the next line


def rule_list_reversal(forward_rule_list):

    Reverses a rule for use in the reverse evolution.
    --------------
    forward_rule_list : list
      A list with 16 items. To figure out what configuration turns into what new configuration, evaluate the value at the index of the old configuration, i.e. to find what configuration 5 turns into, evaluate rule_list[5]
    Returns
    --------------
    reverse_rule_list : list
      A list with 16 items. It is also a rule_list, but using this new list, you can reverse the evolution to recover the original information

  
def forward_evolution(generations, rule_list, dish):

    Performs the forward evolution of the block cellular automata given the forward rule list and the starting dish for the specified number of generations.
    --------------
    generations : int
      The number of times to evolve the automata, i.e. the number generations of cells to evolve
    rule_list : list
      A list with 16 items. To figure out what configuration turns into what new configuration, evaluate the value at the index of the old configuration, i.e. to find what configuration 5 turns into, evaluate rule_list[5]
    dish : list
      A 2D nested array, i.e. a dish with height of 4 and width of 3 would be a list of 4 lists with 3 items each. Only supports ints 0 or 1 as values. Easily created using the numpy module.
    Returns
    --------------
    dish : list
      A 2D nested array. This new dish is evolved using the specified rule list for the specified number of generations

    
def reverse_evolution(generations, rule_list, dish):

    Performs the reverse evolution of the block cellular automata given the forward rule list and the starting dish for the specified number of generations.
    --------------
    generations : int
      The number of times to evolve the automata, i.e. the number generations of cells to evolve
    rule_list : list
      A list with 16 items. To figure out what configuration turns into what new configuration, evaluate the value at the index of the old configuration, i.e. to find what configuration 5 turns into, evaluate rule_list[5]. This forward rule list is automatically converted to the reverse rule list.
    dish : list
      A 2D nested array, i.e. a dish with height of 4 and width of 3 would be a list of 4 lists with 3 items each. Only supports ints 0 or 1 as values. Easily created using the numpy module.
    Returns
    --------------
    dish : list
      A 2D nested array. This new dish is evolved using the specified rule list for the specified number of generations.

  
def calculate_entropy_of_dish(dish):

    Calculates the Shannon entropy of the dish.
    --------------
    dish : list
      A 2D nested array. Easily created using the numpy module.
    Returns
    --------------
    entropy : int
      The Shannon entropy of the information in the dish


def write_dish_to_file(file_name,dish):

    Writes the dish back into a file.
    --------------
    file_name : string
      The file name specifies what to name the file you're writing the indormation to, writes file to the same directory as the program
    dish : list
      A 2D nested array. This dish contains bit information that is processed back into bytes and into whatever file information is specified by the file_name prefix
    Returns
    --------------
    None, creates the file but doesn't return anything specifically
```
    
    """
