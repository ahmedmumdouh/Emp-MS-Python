
import re
import json
import numbers





class person:
    moods = ('happy','tired','Lazy')
    def __init__(self,name,money,mood,healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        if(self.checkHealthRate(healthRate)) :
            self.healthRate = healthRate

    def checkHealthRate(self,healthRate):
        if (isinstance(healthRate , numbers.Number) and healthRate >= 0 and healthRate <= 100) :
            return True
        else :
            print("Invalid_healthRate_Input")
            return False

    #sleep (hours): - Method in Person Class (7 hours  happy, <7 hours  tired, >7 hours  Lazy)
    def sleep(self , hours):
        if( hours == 7) :
            self.mood = self.moods[0]
        elif (hours < 7):
            self.mood = self.moods[1]
        elif (hours > 7) :
            self.mood = self.moods[2]
        else :
            print("Invalid_hours_Input")
    #Method in Person Class (3 meals  100% hth , 2 meals 75% , 1 meal  50%)
    def eat(self,meals):
        if (meals == 3):
            self.healthRate = 100
        elif (meals == 2):
            self.healthRate = 75
        elif (meals == 1) :
            self.healthRate = 50
        else :
            print("Invalid_meals_Input")

    #Method in Person Class (1 item  decrease money 10 L.E)
    def buy(self ,items):
        if (isinstance(items , numbers.Number) ) :
            self.money -= items*10
        else :
            print("Invalid_items_Input")

        


class employee(person):
    __idCounter = 0
    def __init__(self , carObj, email, salary, distanceToWork):
        employee.__idCounter += 1
        self.id = employee.__idCounter
        if(self.checkCarObj(carObj)) :
            self.car = carObj
        if(self.checkMailValid(email)):
            self.email = email
        if(self.checkSalary(salary)):
            self.salary = salary
        if(self.check_DistanceToWork(distanceToWork)) :
            self.distanceToWork = distanceToWork

    def check_DistanceToWork (self,distanceToWork):
        if(isinstance(distanceToWork,numbers.Number)) :
            return True
        else :
            return False  

    def checkCarObj (self ,carObj):
        if ( isinstance(carObj,car)) :
            return True
        else :
            print("Invalid_CarObj_Input")
            return False

    def checkMailValid(self ,email):
        if ( re.search ("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email) ) :
            return True
        else :
            print("Invalid_Email_Input")
            return False

    def checkSalary(self ,salary):   
        if (salary >= 1000 and isinstance(salary , numbers.Number)):
            return True
        else :
            print("Invalid_Salary_Input")
            return False
        
    #Method in Employee Class (8 hourshappy, >8 hours  tired,<8 hours  Lazy)    
    def work (self , hours):
        if (hours == 8):
            self.mood = super(employee,self).moods[0]
        elif (hours >8) :
            self.mood = super(employee,self).moods[1]
        elif (hours <8) :
            self.mood = super(employee,self).moods[2]
        else :
            print("Invalid_Input")
            return False

    # Method in Employee Class (Give the order to run method and give it distance and velocity).
    def drive(self ,distanceKm ):
        if (isinstance(distanceKm ,numbers.Number)) :
            self.car.run( distanceKm , self.car.velocity)
            return True
        else :
            print("Invalid_DriveFun()Para_Input")
            return False
  
    #refuel (gasAmount = 100)- Method in Employee Class (add gasAmount to fuelRate).
    def refuel(self,gasAmount=100):
        self.car.fuelRate = gasAmount

    #send_mail(to, subject, msg, receiver_name): (optional) - Create Email File like the next page specification (Email Composer)    
    def send_mail(self ,toM ,subject ,msg ,receiver_name):
        if(self.checkMailValid(toM)):
            self.file= open("Email.txt","w+")
            self.file.write("\t \t\tSubject:%s\n\t From:%s\n\t To:%s\n\t Hi,%s\n\t \t%s\n\t Thanks\n"%(str(subject),self.email,toM,str(receiver_name),str(msg)))
            self.file.close()

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)



class office:
    employeesNum = 0
    def __init__(self ,name ,employees) : 
        if(self.checkListOfEmpObjs(employees)) :
            self.employees = employees
            office.employeesNum += len(employees)
            self.name = name
            self.employeesNum = len(self.employees)
            print("true")
    
    @classmethod
    def change_emps_num(cls,num):
        if (type(num) == int ) :
            cls.employeesNum =num
        else  :
            print("Input_must_be_integer")

    def get_all_employees (self) :
        return self.employees

    def checkListOfEmpObjs(self,employees):
        if(isinstance(employees,list)):
            for i in employees :
                if (not isinstance(i,employee)) :
                    return False

            return True

    def checkEmpObj(self ,employeeObj) :
        if(isinstance(employeeObj,employee)) :
            return True

    def  get_employee(self,empId):
        if( self.check_Emp_Exist(empId)) :
            for i in self.employees :
                if (i.id == empId) :
                    return i
        else :
            print("Emp_id(%d) isn't hired " %(empId))

    def check_Emp_Exist(self,empId):
        if (type(empId) == int ):
            for i in self.employees :
                if (i.id == empId) :
                    return True
        else :
            print ("Input(Id)_must_be_Integer")


    def hire(self,employee) :
        #search exist
        #check Obj
        if( (not self.check_Emp_Exist(employee.id)) and (self.checkEmpObj(employee) ) ) :
            self.employees.append(employee)
            self.employeesNum = len(self.employees)
            office.employeesNum += 1
        else :
            print("Emp_id(%d) is already hired " %(employee.id))

    def fire(self,empId):
        if( self.check_Emp_Exist(empId)) :
            self.employees.remove(self.get_employee(empId))
            self.employeesNum = len(self.employees)
            office.employeesNum -= 1
        else :
            print("Emp_id(%d) isn't hired " %(empId))
     #check_lateness (empId, moveHour)
     #  (Check if employee is late or not and deduce if he is late -10 and reward if he is not late +10)   
    def checkLateness (self ,empId ,moveHour):
        if( self.check_Emp_Exist(empId)) :
            if(self.calculate_lateness(9 ,moveHour,self.get_employee(empId).distanceToWork,self.get_employee(empId).car.maxVelocity )):
                self.deduct(empId,10)
                print("Employee_id(%d) is Late and his Salary is deducted by 10" %(empId))
                return True  
            else :
                self.reward(empId,10)   
                print("Employee_id(%d) isn't Late and his Salary is rewarded by 10" %(empId))  
                return False
        else :
            print("Emp_id(%d) isn't hired" %(empId))

   

    #calculate_lateness (targetHour , moveHour, distance, velocity): 
    # Static Method in Office Class (Calculate If employee is late or not )
    @staticmethod
    def calculate_lateness (targetHour ,moveHour , distanceKm , velocityKmH) :
        if(isinstance(targetHour,numbers.Number) and isinstance(moveHour,numbers.Number) and moveHour <= 24 and moveHour >= 0) :
            reachHour = (distanceKm / velocityKmH ) + moveHour
            if (reachHour > targetHour) :
                lateness= reachHour - targetHour
                return True
            else :
                lateness = targetHour - reachHour
                return False
        else :
            print("Input_Hour_mustbe_only_numbers in 24H format xx.xx (between 00.00 and 24.00)")

    def deduct (self,empId,deduct):
        self.get_employee(empId).salary -= deduct
    def reward(self,empId ,reward):
        self.get_employee(empId).salary += reward
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)



class car :
    def __init__(self, name, fuelRate,velocity):
        self.name = name
        
        if(self.checkVelocity(velocity)):
            self.velocity = velocity
            self.maxVelocity =velocity

        if (self.checkFuelRate(fuelRate)):
            self.fuelRate =fuelRate    
    
    def checkFuelRate(self ,fuelRate):
        if(fuelRate >=0 and fuelRate <= 100 and isinstance(fuelRate,numbers.Number)) :
            return True
        else :
            print("Invalid_FuelRate_Input")
            return False

    def checkVelocity(self ,velocity):
        if (velocity >=0 and velocity <= 200 and isinstance(velocity,numbers.Number)):
            return True
        else :
            print("Invalid_Velocity_Input")
            return False

    #run (velocity, distance):    #- Method in Car Class (When invoked it decreases the fuelRate and 
    # change the velocity to the input parameter of velocity . And it invoke the stop method 
    # and give it the remain distance (It is possible to stop before arrive the destination because fuelRate become 0).
    def run(self , distanceKm ,velocity):
        if (self.fuelRate == 0) :
            self.velocity = velocity
            self.stop(distanceKm)                        # decrease 10% of full fuelRate= 100 per 10Km(10litre per 10Km)
        elif (self.fuelRate >= ( 1 * distanceKm) ):     # assume decrease 1 litre per 1 km
            self.fuelRate -= ( 1 * distanceKm)
            self.velocity = velocity
            self.stop(0)
        elif (self.fuelRate < ( 1 * distanceKm) and self.fuelRate > 0):
            self.velocity = velocity
            self.stop( ( ( (1 * distanceKm) - self.fuelRate)  ) )
            self.fuelRate = 0
        else :
            print("Invalid_RunParameters_Inputs")

    #Method in Car Class (Stop make the velocity changed to 0 
    # and print notification with the remain distance or that you arrive the destintation )
    def stop(self , remainDistance):
        self.velocity = 0
        if(remainDistance == 0) :
            print("you reach to your the destintation")
        else :
            print("The Remain Distance is %d KM " %(remainDistance)) 
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


######## Testing Cases ... ################

fiat128=car("samy'sCar" ,90,100)
samy = employee(fiat128 , "ad@asas.com",2000,20)
samy2 = employee(fiat128 , "ad@asas.com",2000,20)
samy3 = employee(fiat128 , "ad@asas.com",2000,20)
samy.drive(20)
samy.drive(80)
print(str(fiat128.fuelRate))
samy.refuel()
print(str(fiat128.fuelRate))

print(str(samy2.id))
samy.send_mail("ahmed@g.com","Topic","msg","Ali")
iti = office("ITI",[samy,samy2])
work= office("work",[samy,samy2,samy3])
iti.hire(samy3)
print(len(iti.employees))
#iti.employees.remove(iti.get_employee(3))
print(office.employeesNum)
iti.fire(3)
print(iti.employeesNum)
print(len(iti.employees))
print(office.employeesNum)


iti.deduct(2,500)
print(samy2.salary)
iti.reward(2,100)
print(samy2.salary)
print(office.employeesNum)
iti.checkLateness(1,8.1)    
iti.checkLateness(2,8.9)
print(samy.salary)
print(samy2.salary)

#Save itiData to Json file
with open("itiData.txt","w") as f:
    f.write(json.dumps(iti.toJson(), indent=4))
    
# jsonFile= open("itiData.txt","w",encoding="utf-8")
# json.dump(office,jsonFile,ensure_ascii=False)
# jsonFile.close()


