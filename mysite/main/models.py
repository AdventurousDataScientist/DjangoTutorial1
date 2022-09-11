from django.db import models

class ToDoList(models.Model): # database object
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # delete all items on todolist, when todolist is deleted
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    """
    Creating to do list, and saving it
    
    t = ToDoList(name="Nikhil's List")
    t.save()
    ToDoList.objects.all()
    ToDoList.objects.get(id=1) # get by any field
    t.item_set.all() # gives a query set
    t.item_set.create(text = "go to the mall", complete=False) # do not need to use item constructor
    t = ToDoList.objects
    t.filter(name__startswith="Tim"
    t.delete(
    """

