class myclass:

    __privatevar = 28

    def __privattack(self):
        print("I am in myclass")

    def hello(self):
        print("private variable value: ",myclass.__privatevar)


foo = myclass()
foo.hello()
foo.__privattack