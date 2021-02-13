class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document):
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        [cat for cat in self.categories if cat.id == category_id][0].edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        [top for top in self.topics if top.id == topic_id][0].edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        [d for d in self.documents if d.id == document_id][0].edit(new_file_name)

    def delete_category(self, category_id):
        self.categories.remove([cat for cat in self.categories if cat.id == category_id][0])

    def delete_topic(self, topic_id):
        self.topics.remove([top for top in self.topics if top.id == topic_id][0])

    def delete_document(self, document_id):
        self.documents.remove([doc for doc in self.documents if doc.id == document_id][0])

    def get_document(self, document_id):
        return [doc for doc in self.documents if doc.id == document_id][0]

    def __repr__(self):
        return '\n'.join(repr(d) for d in self.documents)