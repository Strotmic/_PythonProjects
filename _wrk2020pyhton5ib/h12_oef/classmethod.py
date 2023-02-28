# Python Class Method
 
class Employee:
 
    company = 'Tutorial Gateway'
 
    @classmethod
    def message(cls):
        print('The Message is From %s Class' %cls.__name__)  #hier zeggen we wat we zullen printen de $s voegt de string samen en de cls.__name__ is de naam van de klasse
        print('The Company Name is %s' %cls.company) #hier zal je hetzlefde doen maar dit keer met de String company
 
Employee.message()
 
print('-----------')
Employee().message() # hier roep je de klasmethod aan met de naam van de klasse


