class Car:
    """一次模拟汽车的尝试"""
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回规范化的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        """将里程表读数更新为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """让里程表增加特定的值"""
        self.odometer_reading += miles
        
class Battery:
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条电池容量信息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        先初始化父类的属性，
        再初始化特有属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        """电动汽车没油油箱"""
        print("This car doesn't have a gas tank.")


my_model_y = ElectricCar('Tesla', 'model_y', 2024)
print(my_model_y.get_descriptive_name())
my_model_y.battery.describe_battery()        