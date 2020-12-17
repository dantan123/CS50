import os
import random
import re
import sys
import random
import math

DAMPING = 0.85
SAMPLES = 10000

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )
    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = {}

    # need to iterate through a python dictionary
    for corpus_page, corpus_links in corpus.items():
        if corpus_page == page:
            number_links = len(corpus_links) # the current page's link
            for corpus_link in corpus_links:
                # the probability that the page would be linked its connections
                distribution[corpus_link] = damping_factor / number_links
        if corpus_page in distribution.keys():
            # the probability at random of all pages
            distribution[corpus_page] += (1 - damping_factor) / len(corpus)
        else:
            distribution[corpus_page] = (1 - damping_factor) / len(corpus)
    
    return distribution

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = {}

    # first sample is selected at random
    first_page = random.choice(list(corpus.keys()))

    # find the distribution of next page
    next_page = transition_model(corpus, first_page, damping_factor)

    for _ in range(n):
        pages = []
        probabilities = []
        for page, probability in next_page.items():
            pages.append(page)
            probabilities.append(probability)
    
        # return a k-sized list of elements chosen from the population 
        # with replacement where the weights are specified
        selected = random.choices(pages, probabilities, k = 1)[0]
        if selected in page_ranks.keys():
            page_ranks[selected] += 1
        else:
            page_ranks[selected] = 1

        # the next sample's distribution is generated from the selected sample
        next_page = transition_model(corpus, selected, damping_factor)
    
    for page, rank in page_ranks.items():
        page_ranks[page] = rank / n
    return page_ranks

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # initialize dictionaries
    updated_ranks = {}
    current_ranks = {}

    # initialize each key in corpus
    for page in corpus:
        updated_ranks[page] = 1 / len(corpus)

    while True:
        current_ranks = updated_ranks.copy()
        page_count = 0

        # update each page in the updated_ranks
        for page in updated_ranks:
            summation = 0
            for corpus_page, corpus_links in corpus.items():
                if page in corpus_links:
                    # the probability of going page i (link) to page p
                    summation += updated_ranks[corpus_page] / len(corpus_links)

            updated_ranks[page] = (1 - damping_factor) / len(corpus) + damping_factor * summation

            if abs(updated_ranks[page] - current_ranks[page]) < 0.001:
                page_count += 1

        if page_count == len(corpus):
            return updated_ranks

if __name__ == "__main__":
    main()