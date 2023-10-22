'''
***Functional Prompt***
I used a recursive function while adhering to Functional Programming concepts to solve the flatten_sort challenge.

This solution ensures immutability in a couple of different ways - for one, the function does not rely on any data
or variables that are located outside the scope of the function. Also, the function does not alter the value of the
function's parameters. I accomplished this by immediately assigning the final_list variable, which leaves the new_list
unchanged.

This solution is considered a "pure function" because it will always return the same result if provided the same input.
It also does not modify any global or mutable state. Lastly, it has no side-effects, meaning it does not rely on any
external parameters to execute it's operations.

My solution would not be considered a "higher order function." The reason is because it does not accept a callback function
as a parameter. However, my solution could easily be modified to become a higher order function. For example - I could allow
add a paremeter for a callback function that would manipulate a list (such as sort, count, or reverse). That callback function
could then be used on the final_list instead of the "sort()" method that's there now.

I do believe there are more simple methods to solving this problem. For example, I could have used iteration methods to solve
the problem, but instead chose recursion. I also could have defined my list outside the scope of the function, so I wouldn't
have to continuously push it through the parameters. However, functional progamming was still simple and made a lot of sense when
compared to other methods such as using OOP.

For this challenge we were trying to solve a very specific problem, using a list of data. I saw no use for using an Object
Oriented approach, which would add a lot of complexity to the code, yet still require the same type of logic. Functional
programming made sense because the function can perform the same task many times over and over again. Additionally, the
function will be extremely reliable and reusable because it is pure and cannot be effected by external factors.
'''


def flatten_sort(data, new_list=[]):
  final_list = new_list

  if data == []:
    final_list.sort()
    return final_list
  else:
    if type(data[0]) == int:
      final_list.append(data[0])
    else:
      flatten_sort(data[0], final_list)

    return flatten_sort(data[1:], final_list)


print(flatten_sort([1, 2, 3, [9, 7, 4], [2, 8, 1], 12]))
'''
***Object Oriented Prompt***
This solution uses these aspects of Object Oriented Programming:

Encapsulation - Podracer attributes and methods are created and modified within the class objects. This means
the code is easily readable, reusable, and secure. For example - to alter the condition of a Podracer, I
cannot directly change the value like "anakinPod.condition = 'trashed'". Instead I must use one of the methods
in that class like this, "anakinPod.trash()"

Abstraction - This exercise is a good example of abstraction. Users are able to interact with the objects
without understanding their implementation. For example, a user may increase the speed by using the "boost()"
method, and the speed is increased in the background of the object.

Inheritance - the excercise is a good example of inheritance. To create both AnakinPod and Subulbas pod, we
inherit from the Podracer class. With this approach our children classes are able to use attributes and methods
from the parent class. For example, instances of AnakinsPod are still able to use the "repair()" method from the
Podracer class.

Polymorphism - This exercise is not a great example of polymorphism.

It would be possible to program this behavior using a different coding style, which would likely require assigning
a lot more variables and it would be difficult to maintain as the size of the program increased. However, OOP is
the ideal solution for this problem.

In this exercise we can easily equate our real objects (Podracers) to our class objects. We are then able to
interact with those objects like real objects through our methods. This makes the code very readable and reusable.
'''


class Podracer:

  def __init__(self, name, max_speed, condition, price):
    self.name = name
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"
    print(f"{self.name} repaired!")

  def trash(self):
    self.condition = "trashed"


class AnakinsPod(Podracer):

  def __init__(self, name, max_speed, condition, price):
    super().__init__(name, max_speed, condition, price)

  def boost(self):
    self.max_speed *= 2
    print(f"{self.name} max speed increased to {self.max_speed} MPH!")


class SebulbasPod(Podracer):

  def __init__(self, name, max_speed, condition, price):
    super().__init__(name, max_speed, condition, price)

  def flame_jet(self, flamed_jet):
    flamed_jet.trash()
    print(f"{flamed_jet.name} Flamed!")


pod = Podracer("FirstPod", 2, "perfect", 30)
pod.repair()

new_pod = AnakinsPod("AnakinPod", 2, "perfect", 50)
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod("SebulbaPod", 10, "repaired", 20)
third_pod.flame_jet(new_pod)
print(new_pod.condition)
"""
***Reflection***
I would not say that either of these coding paradigms is better than the other. Each paradigm has has it's owns strengths
and capabilities - meaning that use of each paradigm should be specific to the project's specific needs.

I personally would like to complete more projects using object oriented programming. It's easy to see how this approach
can make applications very scalable and interactive. The code is also very readable, which makes it very appealing.

I feel that functional programming absolutely has it's purposes though. This approach is great for very repetitive operations
and can be used to solve complex problems. Meanwhile OOP is better for we are trying manupulate multiple different objects
throughout the use of the program.

In learning, OOP is a tricky concept to understand. It takes a little time to understand constructor methods, the "self" keyword,
and the pillars of OOP. However, once these concepts are understood, the power of OOP is very easy to recognize.
"""
