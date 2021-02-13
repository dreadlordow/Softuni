from methods_and_attributes.document_managment.project.category import Category
from methods_and_attributes.document_managment.project.document import Document
from methods_and_attributes.document_managment.project.storage import Storage
from methods_and_attributes.document_managment.project.topic import Topic


if __name__ == '__main__':
    c1 = Category(1, "work")
    t1 = Topic(1, "daily tasks", "C:\\work_documents")
    d1 = Document(1, 1, 1, "finilize project2")

    d1.add_tag('tagche')
    print(d1)
    d1.remove_tag('tagche')
    d1.remove_tag('tagche')
    d1.remove_tag('mest')
    d2 = Document.from_instances(1, c1, t1, 'tema')
    d2.edit('nova_tema')

    print(d2)