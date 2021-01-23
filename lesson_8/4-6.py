from abc import ABC, abstractmethod

class WarehouseOffice_equipment:
	
	dict_all = {'printers':{},'scaners':{},'xeroxes':{}}
	dict_departments = {'accounting':{'printers':{},'scaners':{},'xeroxes':{}},'staff_department':{'printers':{},'scaners':{},'xeroxes':{}},'office':{'printers':{},'scaners':{},'xeroxes':{}}}
	inv_nums_list = [el for el in range(44587, 88990, 2)]
	t = iter(inv_nums_list)
	
	@classmethod
	def warehouse_to_department(cls, department, office_equipment, quantity):
		if list(cls.dict_departments.keys()).count(department) != 0:
			if list(cls.dict_departments[department].keys()).count(office_equipment) != 0:
				a = cls.dict_all.get(office_equipment)
				list1 = list(a.values())
				cnt = len(list1)
				if cnt < int(quantity):
					print(f'Количество техники {office_equipment} на складе {cnt}')
				else:
					i = 0
					while i < quantity:
						a = cls.dict_all[office_equipment].popitem()
						cls.dict_departments[department][office_equipment].update({a[0]:a[1]})
						i+=1
			else:
				print(f"Офисная техника {office_equipment} не предназначена для отдела {department}")
		else:
			print(f"Отдела {department} не существует")
	
	
class Office_equipment(ABC):
	def __init__(self, model, category, speed, monochrome):
		self.model = model
		self.category = category
		self.speed = speed
		self.monochrome = monochrome
		
	@abstractmethod
	def go_to_warehouse(self,quantity):
		pass
		
		
class Printer(Office_equipment):
	def __init__(self, model, category, speed, monochrome, cartridge_resourсe, paper_thickness):
		super().__init__(model, category, speed, monochrome)
		self.cartridge_resourсe = cartridge_resourсe
		self.paper_thickness = paper_thickness
		
	def go_to_warehouse(self,quantity):
		i = 0
		while i < quantity:
			inv_num = next(WarehouseOffice_equipment.t) 
			WarehouseOffice_equipment.dict_all['printers'].update({inv_num:self.model})
			i += 1
		

class Scaner(Office_equipment):
	def __init__(self, model, category, speed, monochrome, resolution, format_paper):
		super().__init__(model, category, speed, monochrome)
		self.resolution = resolution
		self.format_paper = format_paper
		
	def go_to_warehouse(self,quantity):
		i = 0
		while i < quantity:
			inv_num = next(WarehouseOffice_equipment.t)
			WarehouseOffice_equipment.dict_all['scaners'].update({inv_num:self.model})
			i += 1
		

class Xserox(Office_equipment):
	def __init__(self, model, category, speed, monochrome, volume_photo_drum):
		super().__init__(model, category, speed, monochrome)
		self.volume_photo_drum = volume_photo_drum
		
	def go_to_warehouse(self,quantity):
		i = 0
		while i < quantity:
			inv_num = next(WarehouseOffice_equipment.t)
			WarehouseOffice_equipment.dict_all['xeroxes'].update({inv_num:self.model})
			i += 1


printer1 = Printer('P2200', 'laser', 20, True, 3000, 150)
printer2 = Printer('P2201', 'laser', 20, True, 3000, 150)
scaner1 = Scaner('Sc56-88', 'tablet', 30, True, '600x1200', 'A4')
xerox1 = Xserox('XR-055', 'analog', 20, False, 60000)

printer1.go_to_warehouse(4)
printer2.go_to_warehouse(2)
scaner1.go_to_warehouse(1)
xerox1.go_to_warehouse(2)


WarehouseOffice_equipment.warehouse_to_department('accounting', 'printers', 3)
WarehouseOffice_equipment.warehouse_to_department('staff_department', 'xeroxes', 1)
WarehouseOffice_equipment.warehouse_to_department('office', 'scaners', 2)
print(WarehouseOffice_equipment.dict_departments)	
WarehouseOffice_equipment.warehouse_to_department('officee', 'scaners', 2)
WarehouseOffice_equipment.warehouse_to_department('accounting', 'scanerss', 2)