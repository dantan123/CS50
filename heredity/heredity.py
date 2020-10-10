import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])
    
    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    # powerset includes all subsets of a set
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        # any returns true if any one element is true
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)
                
    # Ensure probabilities sum to 1
    # print(probabilities)
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")
    

def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data

def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]

def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    
    sum_prob = 1

    for person in people:
        prob_gene = 0
        prob_trait = 0
        person_prob = 0

        num_gene = assign_num_genes(person, one_gene, two_genes)

        if person in have_trait:
            prob_trait = PROBS["trait"][num_gene][True]
        else:
            prob_trait = PROBS["trait"][num_gene][False]

        if people[person]["mother"] == None and people[person]["father"] == None:
            # the probability of gene is independent of parents
            prob_gene = PROBS["gene"][num_gene]
        else:
            mother_num_gene = assign_num_genes(people[person]["mother"], one_gene, two_genes)
            father_num_gene = assign_num_genes(people[person]["father"], one_gene, two_genes)
            mother_prob = assign_mut_prob(mother_num_gene)
            father_prob = assign_mut_prob(father_num_gene)
            if num_gene == 2:
                # multiply the prob of from mother with the prob of from father
                # for the case of 2: one mutated gene from mother and one mutated gene from father
                prob_gene = mother_prob * father_prob
            elif num_gene == 1:
                # add together the probabilities of gene coming from mother and not father as well as
                # from father and not mother
                prob_gene = mother_prob * (1-father_prob) + (1-mother_prob) * father_prob
            else:
                # for the case of 0 gene
                # multiply the prob not getting the gene from either parent
                prob_gene = (1-mother_prob) * (1-father_prob)

        person_prob = prob_gene * prob_trait
        sum_prob *= person_prob
        
    return sum_prob
    raise NotImplementedError

def assign_num_genes(person, one_gene, two_genes):
    if person in two_genes:
        num_gene = 2
    elif person in one_gene:
        num_gene = 1
    else:
        num_gene = 0
    return num_gene

def assign_mut_prob(parent_num_gene):
    if parent_num_gene == 0:
        # this parent has no gene (1% chance of passing down)
        prob_gene = PROBS["mutation"]
    elif parent_num_gene == 1:
        prob_gene = 0.5
    else:
        # this parent has two genes (99% chance of passing down)
        prob_gene = 1 - PROBS["mutation"]
    return prob_gene

def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities.keys():
        if person in one_gene:
            num_gene = 1
        elif person in two_genes:
            num_gene = 2
        else:
            num_gene = 0
        
        probabilities[person]["gene"][num_gene] += p

        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p
    
    return
    raise NotImplementedError


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities.keys():
        gene_sum = 0
        trait_sum = 0

        for i in range(3):
            gene_sum += probabilities[person]["gene"][i]
        for i in range(3):
            if probabilities[person]["gene"][i] != 0 and gene_sum != 0:
                probabilities[person]["gene"][i] /= gene_sum
        
        trait_sum = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        if probabilities[person]["trait"][True] != 0 and trait_sum != 0:
            probabilities[person]["trait"][True] /= trait_sum
        if probabilities[person]["trait"][False] != 0 and trait_sum != 0:
            probabilities[person]["trait"][False] /= trait_sum

    return
    raise NotImplementedError

if __name__ == "__main__":
    main()
