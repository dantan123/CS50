import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1

def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])

    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }

    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)

def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    path = os.walk(directory)
    word_map = dict()

    for root, subdirs, files in path:
        for file in files:
            fname = file[0:-4] # truncate .txt
            file_path = os.path.join(root, file)
            with open (file_path) as f:
                data = f.read()
                word_map[fname] = data
    return word_map
    raise NotImplementedError

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    word_list = []
    stop_words = set(nltk.corpus.stopwords.words("english"))
    words = nltk.word_tokenize(document)

    for word in words:
        if word in string.punctuation or word in stop_words:
            continue
        else:
            word_list.append(word.lower())
    return word_list
    raise NotImplementedError

def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    # how rare a word shows up in a particular corpus
    idf_dict = dict()
    num_doc = 0

    for document, words in documents.items():
        for word in words:
            if word not in idf_dict:
                idf_dict[word] = [document]
            else:
                if document not in idf_dict[word]:
                    idf_dict[word].append(document)
        num_doc += 1
    
    # reshape idf dict
    for word, values in idf_dict.items():
        idf_dict[word] = math.log10(num_doc/len(values))
    
    # print(idf_dict)
    return idf_dict
    raise NotImplementedError


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    sum_freq = dict()
    tfidf = dict()
    fnames = list()

    # find the frequency of words eppearing in both the query and files
    for file, words in files.items():
        freq = dict()
        for word in words:
            if word not in query:
                continue
            else:
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
        sum_freq[file] = freq
    
    # rank files based on tf-idf values
    for file, results in sum_freq.items():
        for word, freq in results.items():
            if file not in tfidf:
                tfidf[file] = freq * idfs[word]
            else:
                tfidf[file] += freq * idfs[word]

    # sort a dictionary by its value
    fnames = [k for k,v in sorted(tfidf.items(), key = lambda item:item[1], reverse = True)]

    # return the top n files
    top_files = fnames[:n]
    return top_files
    raise NotImplementedError


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    top_sentences = dict()
    sentence_list = dict()

    for sentence, words in sentences.items():
        visited = []
        for word in words:
            if word in query:
                if sentence not in top_sentences:
                    top_sentences[sentence] = [idfs[word], 1]
                else:
                    if word not in visited:
                        top_sentences[sentence][0] += idfs[word]
                        top_sentences[sentence][1] += 1
                visited.append(word)
        if sentence in top_sentences:
            top_sentences[sentence][1] /= len(sentence)
    
    sentence_list = [k for k,v in sorted(top_sentences.items(), key = lambda item: (item[1][0], item[1][1]), reverse = True)]
    top_sentences = sentence_list[:n]
    return top_sentences
    raise NotImplementedError


if __name__ == "__main__":
    main()
