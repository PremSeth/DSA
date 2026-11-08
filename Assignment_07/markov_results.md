# Markov text analysis

I used *The Tale of Peter Rabbit* from [Project Gutenberg](https://www.gutenberg.org/ebooks/14838). I kept just the story so the model wouldn't count the ebook notes and license. After making the words lowercase and removing punctuation, I got 972 words. There are 383 different words that have another word after them.

For "peter," "was" comes next 3 times and "who" comes next 2 times. For "the," "gate" comes next 5 times, while "garden," "tool," and "wood" each come next 3 times. I think the short story is enough to see the repeated pairs, though most following words only show up once.

I tried generating text from these counts too. It picks a more common next word more often, but the sentences don't always make sense since it only looks at one word at a time.

I started with "peter" and generated 30 words with seed 2026. I got: "peter began to his water cans a rake and their names were good little jacket and shed and then he was staring at him he went to the wood peter".
