class Computer:
    processor = None
    mg = None
    memory  = None

    def __init__(self, processor, mg, memory):
        self.set_data(processor, mg, memory)
        self.get_data()

    def set_data(self, processor = None, mg = None, memory = None):
        self.processor = processor
        self.mg = mg
        self.memory = memory

    def get_data(self):
        print("Processor:", self.processor, ". MG:", self.mg, ". Memory:", self.memory, "Gb.")

comp1 = Computer("AMD", 2.5, 128)


comp2 = Computer("Intel", 3.2, 64)


