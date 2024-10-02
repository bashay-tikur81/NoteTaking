import pytest
from employee_raise import Employee

@pytest.fixture
def salary_raise():
    ''' This creates an instance variable that can be used by all test functions '''
    employee = Employee("Alice", "Bob", 10000)
    return employee
    
def test_give_default_raise(salary_raise):
    ''' Raising by default amount'''
    new_salary = salary_raise.give_raise()
    assert new_salary == 15000

def test_give_custom_raise(salary_raise):
    new_salary = salary_raise.give_raise(8000)
    assert new_salary == 18000

    
