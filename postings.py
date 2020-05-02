class Posting:

    def __init__(self, doc_id: int, count: int):
        self.doc_id = doc_id
        self.term_freq = count
        self.inverse_doc_freq = 1

    