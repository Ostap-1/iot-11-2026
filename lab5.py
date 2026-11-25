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
        print(f"{self._name} {self._votes} {self._votes / total * 100:.2f}%")


class Elections:
    def __init__(self):
        self._candidates = []

    #
    def set_candidates(self, candidates):
        self._candidates = candidates
        
    def get_candidates(self):
        return self._candidates
    
    def __del__(self):
        print("Вибори видалено")

    def add_candidate(self, candidate):
        self._candidates.append(candidate)

    def get_total(self):
        return sum(c.get_votes() for c in self._candidates)

    def winner(self):
        return max(self._candidates, key=lambda c: c.get_votes())

    def show(self):
        total = self.get_total()
        for c in self._candidates:
            c.show(total)


def main():
    elections = Elections()

    for i in range(5):
        name = input(f"Прізвище кандидата {i + 1}: ")
        votes = int(input("Кількість голосів: "))
        elections.add_candidate(Candidate(name, votes))

    print()
    elections.show()
    print("Переможець:", elections.winner().get_name())

    elections2 = Elections()
    elections2.set_candidates(elections.get_candidates()[:3])

    print()
    for i2 in elections2.get_candidates():
        print(i2.get_name(), i2.get_votes())

    print()
    del elections
    del elections2


if __name__ == "__main__":
    main()