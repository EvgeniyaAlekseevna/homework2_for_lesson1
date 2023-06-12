from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for i in self.dates:
            item = i[0]
            while item != i[1]:
                for elem in range((i[1] - i[0]).days + 1):
                    item = i[0] + timedelta(elem)
                    yield item


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7)),
])

for d in m.schedule():
    print(d)
