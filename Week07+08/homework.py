from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
# class Animal(object):
    @abstractmethod
    def __init__(self, type, shape, character, if_risk):
        self.type = type
        self.shape = shape
        self.character = character
        self.if_risk = if_risk
    
    @classmethod
    def judge_risk(cls, type, shape, character):
        if type == '食肉' and shape in ['中等', '大型', '超大型'] and character == '凶猛':
            return cls(type, shape, character, '凶猛动物')
            # self.if_risk = '凶猛动物'
        else:
            # self.if_risk = '非凶猛动物'
            return cls(type, shape, character, '非凶猛动物')

class Zoo(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        try:
            self.__getattribute__(item)
        except Exception:
            return None
        self.__getattribute__(item)

    def add_animal(self, animal_name):
        if not self.__getattr__(animal_name.__class__.__name__):
            self.__setattr__(animal_name.__class__.__name__, animal_name)

class Cat(Animal):
    call = '喵'
    def __init__(self, name, type, shape, character):
        self.name = name
        self.type = type
        self.shape = shape
        self.character = character

    @property
    def judge_pets(self):
        if self.type == '食肉' and self.shape in ['中等', '大型', '超大型'] and self.character == '凶猛':
            return '不适合作为宠物'
        else:
            return '适合作为宠物'

class Dog(Animal):
    call = '汪'
    def __init__(self, name, type, shape, character):
        self.name = name
        self.type = type
        self.shape = shape
        self.character = character

    @property
    def judge_pets(self):
        if self.type == '食肉' and self.shape in ['中等', '大型', '超大型'] and self.character == '凶猛':
            return '不适合作为宠物'
        else:
            return '适合作为宠物'

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    # 猫叫
    cat1.call
    # 猫是否可以做宠物
    cat1.judge_pets