from typing import Dict


class Entry:
    """Entry classed used in KNN algorithm.

    Uses identifier for human consumption stating the name of the entry.
    Dictionary of properties is used by KNN to identify entry or other entries.
    Label assigned either in init method or by algorithm states classification.
    """
    def __init__(self, identifier: str, properties: Dict[str, int],
                 label: str = None):
        """Initialize entry with provided identifier, properties and label.

        Arguments:
            identifier (str): Identifies entry
            properties (Dict[str,int]): Properties for entry as dictionary

        Keyword Arguments:
            label (str, optional): Label assigned to entry
        """
        self._identifier = identifier
        self._properties = properties
        self._label = label

    @property
    def identifier(self) -> str:
        """"Get and set identifier for entry."""
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: str) -> None:
        self._identifier = identifier

    @property
    def properties(self) -> Dict[str, int]:
        """Get and set dictionary of properties"""
        return self._properties

    @properties.setter
    def properties(self, properties: Dict[str, int]) -> None:
        self._properties = properties

    @property
    def label(self) -> str:
        """Get and set label for entry"""
        return self._label

    @label.setter
    def label(self, label: str) -> None:
        self._label = label

    def __str__(self):
        """Return human readable description of entry"""
        return (f"Entry: {self.identifier}, Label: {self.label}\n"
                f"Properties: {self.properties}")

    def __repr__(self):
        """Return inspect able representation of entry"""
        return (f"Entry: {self.identifier}, Label: {self.label} "
                f"Properties: {self.properties}")
