CANDIDATES_COUNT = 5


class Candidate:
    def __init__(self, name, votes):
        self._name = name
        self._votes = votes

    def __del__(self):
        print(f"Кандидата {self._name} видалено")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_votes(self):
        return self._votes

    def set_votes(self, votes):
        self._votes = votes

    def show(self, total):
        percent = self._votes / total * 100 if total else 0
        print(f"{self._name:<15} {self._votes:>5} {percent:6.2f}%")


class Elections:
    def __init__(self):
        self._candidates = []

    def __del__(self):
        print("Вибори видалено")

    def set_candidates(self, candidates):
        self._candidates = list(candidates)

    def get_candidates(self):
        return self._candidates

    def add_candidate(self, candidate):
        self._candidates.append(candidate)

    def get_total(self):
        return sum(c.get_votes() for c in self._candidates)

    def winner(self):
        return max(self._candidates, key=lambda c: c.get_votes(), default=None)

    def show(self):
        total = self.get_total()
        for c in self._candidates:
            c.show(total)


def main():
    elections = Elections()

    for i in range(CANDIDATES_COUNT):
        name = input(f"Прізвище кандидата {i + 1}: ")
        while True:
            try:
                votes = int(input("Кількість голосів: "))
                if votes >= 0:
                    break
                print("Голосів не може бути менше 0")
            except ValueError:
                print("Введіть ціле число")
        elections.add_candidate(Candidate(name, votes))

    print()
    elections.show()
    print("Переможець:", elections.winner().get_name())

    elections2 = Elections()
    elections2.set_candidates(
        [Candidate(c.get_name(), c.get_votes())
         for c in elections.get_candidates()[:3]]
    )

    print()
    for candidate in elections2.get_candidates():
        print(candidate.get_name(), candidate.get_votes())

    print()
    del elections
    del elections2


if __name__ == "__main__":
    main()