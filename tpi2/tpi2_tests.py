

from tpi2 import *

z = MySN()
z.insert(Declaration('bosch',Depends('illumination','battery')))
z.insert(Declaration('bosch',Subtype('turn signal','illumination')))
z.insert(Declaration('bosch',Subtype('driving lights','illumination')))
z.insert(Declaration('bosch',Subtype('fog lights','illumination')))
z.insert(Declaration('bosch',Depends('starter','battery')))
z.insert(Declaration('bosch',Depends('spark plug','battery')))
z.insert(Declaration('bosch',Depends('fuel pump',  'battery')))
z.insert(Declaration('bosch',Association('ignition','starts','starter')))
z.insert(Declaration('bosch',Association('ignition','starts','spark plug')))
z.insert(Declaration('bosch',Association('ignition','starts','fuel pump')))
z.insert(Declaration('bosch',Depends('engine','spark plug')))

z.insert(Declaration('delfi',Association('dashboard','starts', 'illumination')))

z.insert(Declaration('bmw', Depends('combustion engine',  'starter')))
z.insert(Declaration('bmw', Depends('combustion engine',  'fuel pump')))
z.insert(Declaration('mercedes', Depends('diesel engine',  'fuel pump')))

z.insert(Declaration('karl benz', Subtype('starter', 'engine')))
z.insert(Declaration('karl benz', Subtype('combustion engine', 'engine')))
z.insert(Declaration('karl benz', Subtype('diesel engine', 'engine')))

z.insert(Declaration('shell', Subtype('gasoline', 'petrol')))
z.insert(Declaration('bp', Subtype('gasoline', 'petrol')))
z.insert(Declaration('bp', Subtype('diesel fuel', 'petrol')))
z.insert(Declaration('bp', Subtype('lubricant', 'petrol')))
z.insert(Declaration('bp', Subtype('petrol', 'energy')))
z.insert(Declaration('bp', Subtype('battery', 'energy')))
z.insert(Declaration('bp', Subtype('hidrogen', 'energy')))
z.insert(Declaration('castrol', Subtype('lubricant', 'petrol')))

z.insert(Declaration('renault', Depends('gearbox',  'lubricant')))
z.insert(Declaration('renault', Depends('clutch',  'lubricant')))

z.insert(Declaration('hamilton', Depends('driving',  'combustion engine')))
z.insert(Declaration('lamy', Depends('driving',  'diesel engine')))
z.insert(Declaration('hamilton', Depends('driving',  'gearbox')))
z.insert(Declaration('hamilton', Depends('driving',  'clutch')))
z.insert(Declaration('hamilton', Depends('driving',  'steering')))
z.insert(Declaration('hamilton', Depends('driving',  'wheels')))

z.insert(Declaration('peugeot', Association('wheels', 'connect', 'transmission')))
z.insert(Declaration('peugeot', Association('wheels', 'connect', 'steering')))
z.insert(Declaration('peugeot', Association('transmission', 'connect', 'clutch')))
z.insert(Declaration('peugeot', Association('clutch', 'connect', 'gearbox')))
z.insert(Declaration('peugeot', Association('gearbox', 'connect', 'engine')))

z.insert(Declaration('ferrari', Association('throttle', 'connect', 'fuel pump')))

z.insert(Declaration('fiat', Association('dashboard', 'connect', 'illumination')))
z.insert(Declaration('fiat', Association('dashboard', 'connect', 'ignition')))
z.insert(Declaration('fiat', Association('dashboard', 'connect', 'steering')))
z.insert(Declaration('fiat', Association('dashboard', 'connect', 'gearbox')))

z.insert(Declaration('bmw', Association('fuel pump', 'debug_time', 60)))
z.insert(Declaration('bmw', Association('battery', 'debug_time', 10)))
z.insert(Declaration('bmw', Association('clutch', 'debug_time', 180)))
z.insert(Declaration('bmw', Association('transmission', 'debug_time', 30)))
z.insert(Declaration('bmw', Association('combustion engine', 'debug_time', 240)))
z.insert(Declaration('bmw', Association('diesel engine', 'debug_time', 240)))
z.insert(Declaration('bmw', Association('spark plug', 'debug_time', 60)))
z.insert(Declaration('bmw', Association('lubricant', 'debug_time', 10)))
z.insert(Declaration('bmw', Association('wheels', 'debug_time', 1)))
z.insert(Declaration('bmw', Association('gearbox', 'debug_time', 180)))

z.insert(Declaration('seat', Association('clutch', 'debug_time', 200)))
z.insert(Declaration('seat', Association('transmission', 'debug_time', 50)))
z.insert(Declaration('seat', Association('combustion engine', 'debug_time', 250)))
z.insert(Declaration('seat', Association('diesel engine', 'debug_time', 300)))
z.insert(Declaration('seat', Association('spark plug', 'debug_time', 50)))
z.insert(Declaration('seat', Association('lubricant', 'debug_time', 10)))
z.insert(Declaration('seat', Association('wheels', 'debug_time', 1)))
z.insert(Declaration('seat', Association('gearbox', 'debug_time', 200)))
z.insert(Declaration('seat', Association('steering', 'debug_time', 50)))
z.insert(Declaration('seat', Association('starter', 'debug_time', 50)))

z.insert(Declaration('honda', Association('spark plug', 'debug_time', 300)))
z.insert(Declaration('honda', Association('lubricant', 'debug_time', 30)))
z.insert(Declaration('honda', Association('wheels', 'debug_time', 1)))
z.insert(Declaration('honda', Association('gearbox', 'debug_time', 230)))
z.insert(Declaration('honda', Association('steering', 'debug_time', 80)))
z.insert(Declaration('honda', Association('starter', 'debug_time', 80)))


print("-------------------------------------------")
print("dependents of 'battery':", z.query_dependents('battery'))
print("-------------------------------------------")
print("dependents of 'illumination':", z.query_dependents('illumination'))
print("-------------------------------------------")
print("dependents of 'engine':", z.query_dependents('engine'))
print("-------------------------------------------")
print("dependents of 'spark plug':", z.query_dependents('spark plug'))
print("-------------------------------------------")
print("dependents of 'energy':", z.query_dependents('energy'))
print("-------------------------------------------")

print("causes of 'driving':",z.query_causes('driving'))
print("-------------------------------------------")
print("causes of 'fog lights':",z.query_causes('fog lights'))
print("-------------------------------------------")
print("causes of 'gasoline':",z.query_causes('gasoline'))
print("-------------------------------------------")

print("sorted causes of 'driving':",z.query_causes_sorted('driving'))
print("------------------------------------------")


# -------------------------------------------------------------
# Rede de Bayes para testar o método markov_blanket()
# -------------------------------------------------------------

bn = MyBN()

bn.add('a',[],0.003)
bn.add('b_a',[],0.002)
bn.add('c_s',[('a',True )],0.48)
bn.add('c_s',[('a',False)],0.08)

bn.add('d',[],0.01)
bn.add('m_f',[],0.01)
bn.add('b_v',[('c_s',True ),('b_a',True )],0.18)
bn.add('b_v',[('c_s',True ),('b_a',False)],0.02)
bn.add('b_v',[('c_s',False),('b_a',True )],0.90)
bn.add('b_v',[('c_s',False),('b_a',False)],0.68)
bn.add('s_m',[],0.05)

bn.add('s_p',[],0.3)
bn.add('v_p',[('m_f',True),('d',True ),('b_v',True )],0.003)
bn.add('v_p',[('m_f',True),('d',True ),('b_v',False )],0.12)
bn.add('v_p',[('m_f',True),('d',False ),('b_v',True)],0.08)
bn.add('v_p',[('m_f',True),('d',False),('b_v',False )],0.01)
bn.add('v_p',[('m_f',False),('d',True),('b_v',True)],0.04)
bn.add('v_p',[('m_f',False),('d',True ),('b_v',False)],0.07)
bn.add('v_p',[('m_f',False),('d',False),('b_v',True )],0.13)
bn.add('v_p',[('m_f',False),('d',False),('b_v',False)],0.09)
bn.add('h',[('b_v',True )],0.44)
bn.add('h',[('b_v',False)],0.89)
bn.add('s_s',[('s_m',True),('m_f',True ),('b_v',True )],0.3)
bn.add('s_s',[('s_m',True),('m_f',True ),('b_v',False )],0.21)
bn.add('s_s',[('s_m',True),('m_f',False ),('b_v',True)],0.34)
bn.add('s_s',[('s_m',True),('m_f',False),('b_v',False )],0.12)
bn.add('s_s',[('s_m',False),('m_f',True),('b_v',True)],0.15)
bn.add('s_s',[('s_m',False),('m_f',True ),('b_v',False)],0.14)
bn.add('s_s',[('s_m',False),('m_f',False),('b_v',True )],0.132)
bn.add('s_s',[('s_m',False),('m_f',False),('b_v',False)],0.44)

bn.add('s_t',[('d',True )],0.08)
bn.add('s_t',[('d',False)],0.002)
bn.add('s_q',[('s_p',True ),('v_p',True )],0.008)
bn.add('s_q',[('s_p',True ),('v_p',False)],0.4)
bn.add('s_q',[('s_p',False),('v_p',True )],0.51)
bn.add('s_q',[('s_p',False),('v_p',False)],0.13)
bn.add('f_s',[],0.1)
bn.add('c_c',[('s_s',True )],0.49)
bn.add('c_c',[('s_s',False)],0.023)

bn.add('car_s',[('c_c',True),('s_t',True),('s_q',True ),('f_s',True )],0.091)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',True ),('f_s',False )],0.081)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',False ),('f_s',True )],0.045)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',False ),('f_s',False )],0.065)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',True ),('f_s',True)],0.087)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',True),('f_s',False )],0.043)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',False ),('f_s',True)],0.035)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',False),('f_s',False )],0.067)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',True),('f_s',True)],0.052)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',True),('f_s',False)],0.054)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',False),('f_s',True)],0.056)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',False),('f_s',False)],0.078)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',True),('f_s',True )],0.045)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',True),('f_s',False)],0.031)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',False),('f_s',True )],0.034)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',False),('f_s',False)],0.023)

print("-------------------------------------------")
print("Markov blanket of 's_t'")
print(bn.markov_blanket('s_t'))
print("-------------------------------------------")
print("Markov blanket of 'c_s'")
print(bn.markov_blanket('c_s'))
print("-------------------------------------------")




