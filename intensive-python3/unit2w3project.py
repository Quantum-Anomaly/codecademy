#!/usr/bin/env python3
#ground shipping
# $20 flat fee
    #<=2 =      $1.5
    #>2 <=6     $3.00
    #>6 <=10    $4.00
    #>10        $4.75
#drone shipping
# $0 flat fee
    #<=2 =      $4.5
    #>2 <=6     $9.00
    #>6 <=10    $12.00
    #>10        $14.25
#premium ground shipping
# $125 flat fee

#!/usr/bin/env python3
import array
weight = 0
flat_ground = int(20)
flat_drone = int(0)
flat_prem = int(125)
cpp_ground = [1.5, 3, 4, 4.75]
cpp_drone = [4.5, 9, 12, 14.25]
shipping_list = ['Ground' , 'Drone' , 'Premium']

def shipping_cost(weight):
  if weight	<=2:
      ground_cost = float(flat_ground + (cpp_ground[0]) * weight)
      drone_cost = float(flat_drone + (cpp_drone[0]) * weight)
      prem_cost = float(flat_prem)
      lowest_cost = min(ground_cost, drone_cost, prem_cost)
      if ground_cost == lowest_cost:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[0]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
      elif drone_cost == lowest_cost:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[1]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
      else:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[2]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
  elif weight >2 and weight <=6:
      ground_cost = float(flat_ground + (cpp_ground[1]) * weight)
      drone_cost = float(flat_drone + (cpp_drone[1]) * weight)
      prem_cost = float( flat_prem )
      lowest_cost = min(ground_cost, drone_cost, prem_cost)
      if ground_cost == lowest_cost:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[0]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
      elif drone_cost == lowest_cost:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[1]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
      else:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[2]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
  elif weight >6 and weight <=10:
      ground_cost =float(flat_ground + (cpp_ground[2]) * weight)
      drone_cost =float(flat_drone + (cpp_drone[2]) * weight)
      prem_cost =float(flat_prem)
      lowest_cost =min(ground_cost, drone_cost, prem_cost)
      if ground_cost == lowest_cost:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[0]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
      elif drone_cost == lowest_cost:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[1]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
      else:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[2]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
  else:
      weight > 10
      ground_cost = float(flat_ground + (cpp_ground[3]) * weight)
      drone_cost = float(flat_drone + (cpp_drone[3]) * weight)
      prem_cost = flat_prem
      lowest_cost = min(ground_cost, drone_cost, prem_cost)
      if ground_cost == lowest_cost:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[0]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
      elif drone_cost == lowest_cost:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[1]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
      else:
        print ("Shipping your package weighing " + str(weight) + " lbs."'\n' + "Using our " + str(shipping_list[2]) + " service "'\n' + "will be the least expensive at $" + str(lowest_cost) +".")
shipping_cost(41.8)
