# Markov-P
*A basic Markov chain generator written in Python.*

This is a program that will analyse the contents of a given corpus (any large body of text), and attempt to randomly generate text that is similar. The process behind this is known as a [Markov Process](https://en.wikipedia.org/wiki/Pig_(dice_game)](https://en.wikipedia.org/wiki/Markov_chain))

## How to Run?
Simply run *markov-p.py* and follow the on-screen prompts.
A plaintext file *sherlock.txt* has been included in this repo as a sample testing file [(Source)](https://sherlock-holm.es/stories/plain-text/advs.txt). 
After execution, please note the creation of a new output file with the name you provided. This contains the program output.

## How does it work?
When it comes to text, Markov Chains generate the next word in the sentence based *only* on what is most likely to follow the current word. This is based on an analysis of some source text. As described on Wikipedia, "What happens next depends only on the state of affairs now".

When this program is pointed at a plaintext file (the corpus), it iterates over every single word in the corpus. Each word is an object with an attached list, and every time the word is found in the text, the word after it is saved onto the original word's list. Thus we end up with a list of every unique word, and each unique word has its own list of words that occur after it. Duplicates are allowed in these lists, which we use to lazily represent the statistical side of it (more occurrences of a following word means it is represented more times in the associated list, meaning a higher chance it is chosen during generation).

To analyse large texts quickly, a hashtable with quadratic probing is used to store word information.

This corpus data is then used for generation. A random word from the lexicon is chosen as the starter word ("seed") for our generated text. From the list of words following it, we pick one at random and add it to our output. This newest word is then the current word, and from the list of words following it, we pick one at random. This repeats until the desired output length (default: 500 words) has been reached.

The result is a completely artificial, randomly-generated text that follows the statistical tendencies of the source text. It may appear to be grammatically correct, but it will largely be lackluster and incoherent (this isn't GPT, after all!). It can be something mildly amusing to toy with. Try it for yourself!

Sherlock Holmes remains the intellectual property of The Conan Doyle Estate Ltd.
