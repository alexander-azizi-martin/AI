import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    # if len(sys.argv) != 2:
    #     sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    #files = load_files(sys.argv[1])
    files = load_files("corpus")
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
    files = {}

    for document_name in os.listdir(directory):
        if document_name.endswith(".txt"):
            with open(os.path.join(directory, document_name), encoding="utf8") as document:
                files[document_name] = document.read()

    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = []

    for token in nltk.word_tokenize(document):
        if token not in string.punctuation:
            words.append(token.lower())

    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    words_count = {}

    # Counts the number of documents a word is in
    for document_name in documents:
        words_seen = set()
        for word in documents[document_name]:
            # Only adds to the count if the word has not been seen in the document
            if word not in words_seen:
                words_count[word] = words_count.get(word, 0) + 1
                words_seen.add(word)

    # Calculates and returns IDF of each word
    return {word: math.log(len(documents) / words_count[word]) for word in words_count}


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    documents_score = {}

    # Calculates each document score
    for document in files:
        documents_score[document] = 0
        for word in query:
            term_frequency = files[document].count(word)
            if term_frequency > 0:
                documents_score[document] += idfs[word] * term_frequency
    
    # Gets the top n documents
    top_documents = []
    for (document, score) in sorted(documents_score.items(), key=lambda item: item[1], reverse=True):
        if n > 0:
            top_documents.append(document)
            n -= 1
        else:
            break
    
    return top_documents


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sentences_score = {}

    # Calculates each sentence score
    for sentence in sentences:
        sentences_score[sentence] = 0
        for word in query :
            if word in sentences[sentence]:
                sentences_score[sentence] += idfs[word]
            
    # Gets the top n sentence
    top_sentences = []
    sorted_sentences = sorted(sentences_score.items(), key=lambda item: item[1], reverse=True)
    for i in range(n):
        top_sentence, next_sentence = sorted_sentences[i], None
        if i < len(sorted_sentences) - 1: 
            next_sentence = sorted_sentences[i + 1]

        while top_sentence[1] == next_sentence[1]:
            query_term_density_top, query_term_density_next = 0, 0

            for word in query:
                if word in top_sentence[0]:
                    query_term_density_top += (1 / len(sentences[top_sentence[0]]))
                if word in next_sentence[0]:
                    query_term_density_next += (1 / len(sentences[next_sentence[0]]))
            
            if query_term_density_top < query_term_density_next:
                top_sentence = next_sentence

            i += 1
            if i < len(sorted_sentences) - 1: 
                next_sentence = sorted_sentences[i + 1]
            else:
                break

        top_sentences.append(top_sentence[0])
    
    return top_sentences


if __name__ == "__main__":
    main()
