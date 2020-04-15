from heredity import joint_probability
import unittest

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

# def joint_probability(people, one_gene, two_genes, have_trait):


class TestJointProbability(unittest.TestCase):
    def tests(self):
        self.assertEqual(
            joint_probability(people, {"Harry"}, {"James"}, {"James"}),
            0.0026643247488
        )
        self.assertEqual(
            joint_probability(people, {"Lily"}, {"James"}, {"James"}),
            0.0000147162015
        )
        self.assertEqual(
            joint_probability(people, {}, {"James", "Harry", "Lily"}, {"James"}),
            0.0000147162015
        )


people = {
    'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
    'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
    'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
}

if __name__ == '__main__':
    unittest.main()
