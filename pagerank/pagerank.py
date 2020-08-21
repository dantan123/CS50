import os
import random
import re
import sys
import random

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
    out_dict = {}
    # need to iterate through a python dictionary
    for key, value in corpus.items():
        if key == page:
            connections = len(value)
            for i in value:
                out_dict[i] = damping_factor/connections
        if key in out_dict.keys():
            out_dict[key] += (1-damping_factor)/len(corpus)
        else:
            out_dict[key] = (1-damping_factor)/len(corpus)
    return out_dict
    raise NotImplementedError

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    out_dict = {}
    first_page = random.choice(list(corpus.keys()))
    #print("first page is:", first_page)
    next_page = transition_model(corpus, first_page, damping_factor)
    #print("next page is:", next_page)
    for i in range(n):
        all_keys = []
        all_probs = []
        for key, value in next_page.items():
            all_keys.append(key)
            all_probs.append(value)
        arr = random.choices(all_keys, all_probs, k = 1)
        selected = arr[0]
        if selected in out_dict.keys():
            out_dict[selected] += 1
        else:
            out_dict[selected] = 1
        next_page = transition_model(corpus, selected, damping_factor)
    for key, value in out_dict.items():
        out_dict[key] = value / n
    return out_dict
    raise NotImplementedError

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    out_dict = {}
    total_pages = len(corpus)

    #print("corpus is", corpus)
    
    for key, value in corpus.items():
        temp_value = 0
        while True:
            if key in out_dict.keys():
                temp_value = out_dict[key]
            out_dict[key] = (1-damping_factor)/total_pages
            for i in value:
                if i not in out_dict.keys():
                    out_dict[i] = 1/len(corpus)
                out_dict[key] += damping_factor*(out_dict[i]/len(value))
                #print("The key and output are", key, out_dict[key])
            if temp_value != 0 and abs(temp_value - out_dict[key]) < 0.001:
                break
    return out_dict
    raise NotImplementedError

if __name__ == "__main__":
    main()