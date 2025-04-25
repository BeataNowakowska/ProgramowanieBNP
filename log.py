class Logger:

    def __init__(self, filename="log.txt"):
        self.logs = []
        self.filename = filename

    def log(self, message):
        self.logs.append(message)
        print(f"LOG: {message}")
        with open(self.filename, "a") as file:
            file.write(message + "\n")

    def show_logs(self):
        for entry in self.logs:
            print(entry)


if __name__ == "__main__":
    logger = Logger()
    logger.log("Program started.")
    logger.log("User clicked a button.")
    logger.show_logs()
