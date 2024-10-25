import modules.converters

print('### Test converters')
print(f'Three meters is {modules.converters.m_to_cm(3)} inches')
print(f'Three centimeters is {modules.converters.cm_to_inches(3)} inches')
print(f'5 feet and 9 inches is {modules.converters.feet_and_inches_to_cm(5,9)} cm')


