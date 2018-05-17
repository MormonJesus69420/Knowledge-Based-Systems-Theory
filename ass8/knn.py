from typing import List, Tuple, Dict
from entry import Entry
import operator


class KNN:
    """Uses KNN algorithm to classify Entry elements.

    Using KNN algorithm and other entries provided to the init methods finds
    which class a specific entry belongs to.
    """

    def __init__(self, entries: List[Entry], k: int = 3):
        """Initialize KNN with entries and number of neighbors to consider.

        Arguments:
            entries (List[Entry]): List of predefined and labeled entries.

        Keyword Arguments:
            k (int, optional): Number of neighbors to consider, defaults to 3.
        """
        self._entries = entries
        self._k = k

    @property
    def entries(self) -> List[Entry]:
        """Get and set list of entries used in KNN algorithm"""
        return self._entries

    @entries.setter
    def entries(self, entries: List[Entry]) -> None:
        self._entries = entries

    @property
    def k(self) -> int:
        """Get and set number of neighbors for consideration"""
        return self._k

    @k.setter
    def k(self, k: int) -> None:
        self._k = k

    def classify(self, entry: Entry) -> None:
        """Assigns label to entry based on KNN algorithm.

        Uses functions get_distances, get_neighbors and get_label to assign
        appropriate label to entry.

        Arguments:
            entry (Entry): Entry for classification
        """
        if len(self.entries) < self.k:
            print(f"Len of entries is {len(self.entries)} while k is {self.k}")
            return

        distances = self.get_distances(entry)

        neighbors = self.get_neighbors(distances)

        entry.label = self.get_label(neighbors)

    def get_label(self, neighbors: List[Entry]) -> str:
        """Returns label shared by most of entries in list.

        Going through the list of neighbors it builds up votes for labels and
        the label with most votes wins and is returned.

        Arguments:
            neighbors (List[Entry]): List of entries.

        Returns:
            str: Label shared by most entries.
        """
        votes = {}

        for ent in neighbors:
            label = ent.label
            if label in votes:
                votes[label] += 1
            else:
                votes[label] = 1

        lbls = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
        return lbls[0][0]

    def get_neighbors(self,
                      distances: List[Tuple[Entry, float]]) -> List[Entry]:
        """Returns k nearest entries from list of tuples.

        Goes through list of tuples with entries and their distances and finds
        k nearest neighbors.

        Arguments:
            distances (List[Tuple[Entry, float]]): List of tuples ordered by
            distance.

        Returns:
            List[Entry]: List of k nearest entries.
        """
        neighbors = list()

        for x in range(self.k):
            neighbors.append(distances[x][0])

        return neighbors

    def get_distances(self, entry: Entry) -> List[Tuple[Entry, float]]:
        """Returns list of tuples(Entry, float) ordered by distance from entry.

        Finds distance from entry to entries and puts them in ordered list or
        tuples.

        Arguments:
            entry (Entry): Entry to calculate distances to.

        Returns:
            List[Tuple[Entry, float]]: List of tuples(Entry, distance).
        """
        distances = list()

        for ent in self.entries:
            distance = self.get_distance(entry, ent)
            distances.append((ent, distance))

        distances.sort(key=operator.itemgetter(1))

        return distances

    def get_distance(self, entry1: Entry, entry2: Entry) -> float:
        """Returns euclidean distance between two entries.

        Arguments:
            entry1 (Entry): First entry.
            entry2 (Entry): Second entry.

        Returns:
            float: Euclidean distance between entries.
        """
        distance = 0.0
        for key, value in entry1.properties.items():
            distance += pow(value - entry2.properties.get(key, None), 2)

        return distance


entry1 = Entry("Tom", {"Math": 6, "English": 6, "Civics": 6,
                       "Science": 6, "PE": 6, "History": 6}, "Excellent")
entry2 = Entry("Peter", {"Math": 1, "English": 1, "Civics": 1,
                         "Science": 1, "PE": 1, "History": 1}, "Poor")
entry3 = Entry("Jane", {"Math": 3, "English": 6, "Civics": 4,
                        "Science": 4, "PE": 4, "History": 4}, "Good")
entry4 = Entry("Jack", {"Math": 6, "English": 2, "Civics": 2,
                        "Science": 5, "PE": 3, "History": 3}, "Good")
entry5 = Entry("Mary", {"Math": 4, "English": 4, "Civics": 5,
                        "Science": 4, "PE": 3, "History": 5}, "Good")
entry6 = Entry("Phyllis", {"Math": 4, "English": 2, "Civics": 2,
                           "Science": 6, "PE": 2, "History": 3}, "Good")
entry7 = Entry("Ron", {"Math": 2, "English": 4, "Civics": 3,
                       "Science": 2, "PE": 1, "History": 2}, "Poor")
entry8 = Entry("Diane", {"Math": 5, "English": 4, "Civics": 6,
                         "Science": 6, "PE": 4, "History": 6}, "Excellent")
entry9 = Entry("Fiona", {"Math": 5, "English": 5, "Civics": 5,
                         "Science": 5, "PE": 3, "History": 5}, "Excellent")
entry10 = Entry("Peter", {"Math": 2, "English": 2, "Civics": 2,
                          "Science": 3, "PE": 2, "History": 1}, "Poor")

entries = [entry1, entry2, entry3, entry4, entry5,
           entry6, entry7, entry8, entry9, entry10]


entry = Entry("Bob", {"Math": 6, "English": 5, "Civics": 6,
                      "Science": 5, "PE": 6, "History": 5})

knn = KNN(entries)
knn.classify(entry)
print(entry)
