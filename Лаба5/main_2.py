import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:

    def __init__(self, some_list_of_objects):

        self.some_list_of_objects = some_list_of_objects

    def __copy__(self):

        some_list_of_objects = copy.copy(self.some_list_of_objects)

        new = self.__class__(
            self.some_list_of_objects
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo={}):

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)

        new = self.__class__(
            self.some_list_of_objects
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    list_of_objects = ["Ivan", "pivo"]
    print(' '.join(list_of_objects))
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(list_of_objects)
    circular_ref.set_parent(component)
    print("Хотите повторить заказ? Y/N")
    if input() == "Y":
        shallow_copied_component = copy.deepcopy(component)
        print("Ваш заказ", ' '.join(shallow_copied_component.some_list_of_objects))
    else:
        print("Тогда пока!!")
