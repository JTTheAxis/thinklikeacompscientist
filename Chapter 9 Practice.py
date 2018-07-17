"ONE"
def function(tup):
    tup=tup[:1] + ("meme",) + tup[2:]
    return tup
print(function(("Paris Hilton", "Best Actress", 1987, 1981)))
#1. We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function. Construct a small Python example to test whether this is possible, and write up your findings.
#A: In response to the first question, it is certainly possible to pass tuples as arguments to a function. One can also return parts of the tuple through slicing in the function, and even assign values to it. 

"TWO"
#Is a pair a generalization of a tuple, or is a tuple a generalization of a pair?
#A tuple is a generalization of a pair. This is because while a pair can only be a tuple, a tuple doesn't have to be a pair. It can be a triplet, quintuplet, and can contain any number of items. Consequently, a tuple would be a generalization of a pair.

"THREE"
#Is a pair a kind of tuple, or is a tuple a kind of pair?
#As stated above, all pairs are tuples, but not all tuples are pairs. Therefore, one could also say that a pair is a kind of tuple, but a tuple is not a kind of pair. 