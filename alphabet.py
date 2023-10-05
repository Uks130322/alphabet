import enum


class Status(enum.Enum):
    BLACK = 0
    WHITE = 1


def extract_alphabet(
        graph: dict
        ) -> list:
    """
    Extract alphabet from graph
    :param graph: graph with partial order
    :return: alphabet
    """
    if graph == {}:
        return []

    alphabet: list = [None] * len(graph)
    color = {}
    index = len(alphabet) - 1

    for key in graph.keys():
        color[key] = Status.WHITE

    while alphabet[0] is None:

        for key, value in graph.items():
            if color[key] != Status.BLACK and (value == set() or sum([color[letter].value for letter in value]) == 0):
                alphabet[index] = key
                index -= 1
                color[key] = Status.BLACK

    return alphabet


def build_graph(
        words: list
        ) -> dict:
    """
    Build graph from ordered words. Graph should contain all letters from words
    :param words: ordered words
    :return: graph
    """
    graph = {}

    for ind in range(len(words)):
        letter = 0
        first_difference = True
        while letter < len(words[ind]):
            graph.setdefault(words[ind][letter], set())
            if (ind != len(words) - 1 and first_difference and letter < len(words[ind + 1])
                    and words[ind][letter] != words[ind + 1][letter]):
                graph[words[ind][letter]].add(words[ind + 1][letter])
                first_difference = False
            letter += 1
    return graph


def get_alphabet(
        words: list
        ) -> list:
    """
    Extract alphabet from sorted words
    :param words: sorted words
    :return: alphabet
    """
    graph = build_graph(words)
    return extract_alphabet(graph)
