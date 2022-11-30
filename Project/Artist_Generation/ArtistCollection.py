import csv
from typing import Set, Dict


class ArtistCollection:
    def __init__(self):
        self.__list: Dict[str, Set[int]] = {}

    @property
    def list(self):
        return self.__list

    def append_item(self, name: str, year: int) -> None:
        if self.is_existing_artist(name):
            self.get_year_set(name).add(year)
        else:
            self.__list.update({name: {year}})

    def is_existing_artist(self, name: str) -> bool:
        if name in self.__list:
            return True
        else:
            return False

    def get_year_set(self, name: str) -> Set[int]:
        try:
            return self.__list[name]
        except KeyError:
            print("Artist name doesn't exist!")

    def write_to_csv(self, filename: str) -> None:
        with open(filename, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for name, years in self.__list.items():
                row = [name]
                row.extend(list(map(str, years)))
                writer.writerow(row)

    def read_csv_to_object(self, filename: str):

        self.__list.clear()
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                name = row.pop(0)
                years = set([int(y) for y in row])
                self.__list.update({name: years})


