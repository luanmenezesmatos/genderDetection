class selectOption:
    def __init__(self, question, options):
        self.question = question
        self.options = options

    def show(self):
        print(self.question)
        for i in range(len(self.options)):
            print(f"{i+1} - {self.options[i]}")
        print()

    def choose(self):
        try:
            self.show()
            return int(input("Escolha uma opção: "))
        except:
            print("Opção inválida! Tente novamente.")
            exit()