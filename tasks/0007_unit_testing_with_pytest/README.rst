Test-driven development (TDD)
=============================

TDD is a software development technique, where you first **think** how
software component is going to be tested. This is a very important
part of TDD - when the architecture of a software is driven
by "it should be tested" requirements. This means less coupling,
smaller components, focused responsibility - all towards principles
of `S.O.L.I.D <https://itnext.io/solid-principles-explanation-and-examples-715b975dcad4>`_.

Then you document your mental picture of the test
- this usually implies creating an automated way of testing
the component. Finally, you start writing the component.
In this context a "component" could be as small a one-liner function.

The small components are usually called "units". Their testing
is strictly targeted and isolated from other components.

Here are some essential articles:

* `What is TDD <https://medium.com/capgemini-microsoft-team/what-is-test-driven-development-4a14bb69463a>`_
* `How to do Unit Testing in Test Driven Development(TDD)? <https://www.simform.com/unit-testing-tdd/>`_ (C#-oriented)
* `Test Desiderada <https://www.youtube.com/watch?v=5LOdKDqdWYU>`_
  - Kent Beck and Kelly Sutton go through desirable test properties one-by-one.
    Great 12 videos to watch :)

* `Coupling in Programming: What This Means and How Not to Get Burned
  <https://blog.ndepend.com/programming-coupling/>`_
* `C# Best Practices : Dangers of Violating SOLID Principles in C#
  <https://docs.microsoft.com/en-us/archive/msdn-magazine/2014/may/csharp-best-practices-dangers-of-violating-solid-principles-in-csharp>`_.

At this point you would become a little bit familiar with TDD and Unit testing.
I hope that you will practice TDD at work :)

As of learning Python  - we will apply that knowledge and use TDD while
implementing all upcoming tasks.

pytest
------

`Pytest <https://docs.pytest.org/en/stable/>`_ is a renowned Python
unit testing library.
(Note that Python standard library includes
`unittest <https://docs.python.org/3/library/unittest.html>`_
framework. I personally prefer `pytest` for its minimalist approach.

Consider that we want to write a simple `grep(line, patter)` function.
How would we test it?

.. code-block:: python

   # grep.py
   def grep(line, pattern):
       return pattern in line


.. code_block:: python

   # example/test_grep.py
   def test_line_contains_pattern():
       assert grep('hello world', 'hello')

   def test_pattern_not_found_in_line():
       assert not grep('hello world', 'abc')


Now we run `pytest` and get the following results:

.. code-block:: none


$ pytest example

====================== test session starts ======================
platform linux -- Python 3.8.5, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/zaur/projects/learnpython/tasks/0007_unit_testing_with_pytest
collected 2 items

example/test_grep.py ..                                  [100%]

====================== 2 passed in 0.01s ======================


Please note, that the example above doesn't show the flow of TDD.
With TDD, we would have first written `test_line_contains_pattern()`
then implemented `grep(...)` then
`test_pattern_not_found_in_line()` to test the negative case.


Task: TDD practice with grep
----------------------------

You have done a great job doing grep tasks! It's time to boost your
programming skills to the next level.

Let's take the `grep` task #2 as a starting point. The goal
is to do it again the TDD way.

Create virtual environment and install `pytest` package.

The `src` directory has all necessary files to start with :)
Try running

.. code-block:: python

   $ pytest src/

Pytest will search for tests in `src/` directory and run all the tests.

Don't hesitate to ask questions if anything is unclear!
