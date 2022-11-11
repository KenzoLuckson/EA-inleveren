import numpy as np
import statistics as stat
import math
from arduino_device import ArduinoVISADevice, list_devices

class DiodeExperiment:
    def __init__(self):
        self.device = ArduinoVISADevice(port="ASRL4::INSTR")

    def scan(self, start, stop, repeats):
        U_LED_list_average = []
        I_LED_list_average = []
        U_resistor_list_average = []
        fault_U_resistor_list = []
        fault_U_LED_list = []
        fault_I_LED_list= []

        for ADC in range(start, stop):

            self.device.set_output_value(ADC)
            U_LED_list = []
            I_LED_list = []
            U_resistor_list = []
            U_LED_total = 0
            I_LED_total = 0
            U_resistor_total = 0
            for x in range(repeats):
                U_LED = self.device.get_input_voltage(channel=1) - self.device.get_input_voltage(channel=2)
                I_LED = self.device.get_input_value(channel=2)/220
                U_resistor = self.device.get_input_voltage(channel=2)

                U_LED_list.append(U_LED)
                I_LED_list.append(I_LED)
                U_resistor_list.append(U_resistor)

                U_LED_total += U_LED
                I_LED_total += I_LED
                U_resistor_total += U_resistor

            U_LED_avg = U_LED_total/repeats
            I_LED_avg = I_LED_total/repeats
            U_resistor_avg = U_resistor_total/repeats


            fault_U_LED = stat.stdev(U_LED_list)/ math.sqrt(repeats)
            fault_I_LED = stat.stdev(I_LED_list)/ math.sqrt(repeats)
            fault_U_resistor = stat.stdev(U_resistor_list)/ math.sqrt(repeats)


            #add the measurements to the lists
            fault_U_LED_list.append(fault_U_LED)
            fault_I_LED_list.append(fault_I_LED)
            fault_U_resistor_list.append(fault_U_resistor)

            U_LED_list_average.append(U_LED_avg)
            I_LED_list_average.append(I_LED_avg)
            U_resistor_list_average.append(U_resistor_avg)



        #turn LED off
        self.device.set_output_value(0)
        return U_LED_list_average, I_LED_list_average, U_resistor_list_average, fault_U_LED_list, fault_I_LED_list, fault_U_resistor_list



    