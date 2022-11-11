import pandas as pd


df = pd.read_csv('sukkarcornelintegral.csv')
df2 = pd.read_csv('sukkarcornellintegral2.csv')


def err_msg():
    """Function to display error message


    Return:
        string: Display error

    """

    err = "PLEASE I DON't UNDERSTAND THAT. RERUN AND ENTER A VALID COMMAND"

    return err


# Calculate well_depth or height

well_depth = float(input('What is the well depth in ft? '))

# Temperature Conversion From Fahrenheit To Rankine

temp_avg_sys = float(input('what is the average temp in fahrenheit? '))


def temp_avg_in_rankine():
    """Function to calculate temperature in degrees rankine


    Return:
        floats: Temperature in degrees rankine

    """

    value = f"{460 + temp_avg_sys}"

    return value


# Evaluating sukkar and cornell integral right hand side(scrhs)

gas_specific_gravity = float(input('what is the gas specific gravity? '))


def evaluate_scrhs():
    """Function to evaluate the sukkar and cornell
    integral right hand side


    Return:
        floats: sukkar and cornell integral-RHS

    """

    scrhs = (0.01875 * float(gas_specific_gravity * well_depth)) / float(temp_avg_in_rankine())

    return scrhs


# Calculating pseudocritical temperature and pseudocritical pressure

def natural_gas_systems():
    """Function to calculate pseudocritical
    temperature of gas


    Return:
        floats: pseudocritical temperature

    """
    tpc_natural_gas_systems = 170.491 + 307.344 * gas_specific_gravity

    return tpc_natural_gas_systems


def natural_gas_systems2():
    """Function to calculate pseudocritical
    pressure of gas


    Return:
        floats: pseudocritical pressure

    """

    ppc_natural_gas_systems = 709.604 - 58.718 * gas_specific_gravity

    return ppc_natural_gas_systems


def gas_condensate_systems():
    """Function to calculate pseudocritical
    temperature in gas condensate systems


    Return:
        floats: pseudocritical temperature

    """

    tpc_gas_condensate_systems = 149.18 + 358.14 * gas_specific_gravity - 66.976 * gas_specific_gravity ** 2

    return tpc_gas_condensate_systems


def gas_condensate_systems2():
    """Function to compute pseudocritical
    pressure in gas condensate systems


    Return:
        floats: pseudocritical pressure

    """

    ppc_gas_condensate_systems = 787.06 - 147.34 * gas_specific_gravity - 7.916 * gas_specific_gravity ** 2

    return ppc_gas_condensate_systems


# COMPUTING PSEUDOREDUCED PROPERTIES
# gas_type = input('type in a gas system:Natural gas system or gas condensate system? ')
# if (gas_type == 'Natural gas system'):
def pseudo_reduced_temp():
    """Function to compute reduced temperature


    Return:
        floats: reduced temperature rounded to one
        decimal place

    """

    tpr_pseudo_reduced_temp = float(temp_avg_in_rankine()) / natural_gas_systems()

    return round(tpr_pseudo_reduced_temp, 1)


static_wellhead_pressure = float(input('what is the value of the wellhead pressure in psia '))


def pseudo_reduced_wellhead_pressure():
    """Function to compute reduced pressure
    at wellhead pressure


    Return:
        floats: reduced pressure at wellhead rounded
        to three decimal places

    """

    ppr1_wellhead = static_wellhead_pressure / natural_gas_systems2()

    return round(ppr1_wellhead, 3)


input('using the values of Tpr and Ppr displayed below. Goto sukkarcornel integral'
      'table and read the value of the CELL. Type "ok" to see Tr and Pr values- ')

print('')
print('<-------------------------------------->')
print(f"REDUCED TEMP= {pseudo_reduced_temp()}")
print(f"REDUCED PRESSURE = {pseudo_reduced_wellhead_pressure()}")
print('<-------------------------------------->')
print('')

# Block for calculating static BHP for REDUCED PRESSURE GREATER THAN 2.0 or PRESSURE ABOVE 2000

decision = input('IS REDUCED PRESSURE GREATER THAN 2.0 or PRESSURE ABOVE 2000 psia? TYPE "yes" or "no" TO CONTINUE => ')

if decision.upper() == "YES":

    print('<------------------------------------------------------------------------------------>')
    print('SUKKAR_CORNELL INTEGRAL TABLE FOR PRESSURES ABOVE 2000 psia or Ppr = 2.0 and ABOVE '
          'constant B = 0')
    print('<------------------------------------------------------------------------------------>')


    def table_integral_head():
        """Function to display sukkar and cornell
        table of integral-head


        Return:
            dataframe: for the first fifty one rows
        """

        return df.head(51)


    #     Stores table_integral_head in the variable t1
    t1 = table_integral_head()


    def table_integral_tail():
        """Function to display sukkar and cornell
        table of integral-tail


        Return:
            dataframe: for the last forty nine rows

        """

        return df.tail(49)


    #     Stores table_integral_tail in the variable t2
    t2 = table_integral_tail()

    print('TABLE 1')
    print('<--------------------------------------------------------------------------------------------------->')
    print(t1)
    print('<--------------------------------------------------------------------------------------------------->')
    print('CONTINUE FROM TABLE 1')
    print('<--------------------------------------------------------------------------------------------------->')
    print(t2)
    print('<--------------------------------------------------------------------------------------------------->')

    #     First interpolation to compute the sukkar and cornell integral value

    ppr_above = float(input("what is the value of CELL ABOVE 'Ppr'? "))
    ppr_below = float(input("what is the value of CELL BELOW 'Ppr'? "))
    sciv_above = float(input("what is the sukkarcornel integral value corresponding to 'value of CELL ABOVE Ppr'? "))
    sciv_below = float(input("what is the sukkarcornel integral value corresponding to 'value of CELL BELOW Ppr'? "))

    a = ppr_above - pseudo_reduced_wellhead_pressure()
    a2 = ppr_above - ppr_below
    b = sciv_above - sciv_below


    def interpolated_integral_value():
        """Function to interpolate sukkar and cornell
        integral value


        Return:
            i_integral_value(floats): interpolated integral value

        """

        i_integral_value = sciv_above - ((a / a2) * b)

        return i_integral_value


    def real_integral_value():
        """Function to calculate real integral value


        Return:
            real_value(floats): Difference btw interpolated value and
            the sukkar and cornell integral-RHS

        """

        real_value = interpolated_integral_value() - evaluate_scrhs()
        return real_value


    print('')
    print('<-------------------------------------------------------->')
    print(f"sukkar and cornel integral value is:{real_integral_value()}")
    print('<-------------------------------------------------------->')
    print('')

    #     Second interpolation to compute reduced pressure at real integral value

    upper_value_integral = float(input('what is the integral value of CELL ABOVE '
                                       '"sukkar and cornel integral value"? '))
    lower_value_integral = float(input('what is the integral value of CELL BELOW '
                                       '"sukkar and cornel integral value"? '))
    ppr_of_upper_value_integral = float(
        input('what is the value of Ppr corresponding to integral value of '
              'CELL ABOVE "sukkar and cornel integral value"? '))
    ppr_of_lower_value_integral = float(
        input('what is the value of Ppr corresponding to integral value of '
              'CELL BELOW "sukkar and cornel integral value"? '))

    i = upper_value_integral - real_integral_value()

    i2 = upper_value_integral - lower_value_integral

    pr = ppr_of_upper_value_integral - ppr_of_lower_value_integral


    def pseudo_reduced_bhp():
        """Function to compute reduced
        bottom hole pressure


        Return:
            floats: pseudo_reduced BHP rounded to
            three decimal places

        """

        reduced_bhp = ppr_of_upper_value_integral - (i / i2) * pr

        return round(reduced_bhp, 3)


    def static_bhp():
        """Function to compute the
        Static Bottom Hole Pressure


        Return:
            pws(floats): The static BHP rounded to 3
            decimal places

        """

        pws = pseudo_reduced_bhp() * natural_gas_systems2()

        return f"The static_bhp is:{round(pws, 3)} psia"


    print('')
    print('<-------------------------------------->')
    print(static_bhp())

# Block for calculating static BHP for REDUCED PRESSURES FROM 1.0 to 5.0 or PRESSURES FROM 600 psia to 3200

elif decision.upper() == "NO":
    print('<-------------------------------------------------------------------------------------------------------->')
    print('SUKKAR_CORNELL_INTEGRAL TABLE FOR REDUCED PRESSURES FROM 1.0 to 5.0 or PRESSURES FROM 600 psia to 3200 '
          'constant B = 0')
    print('<-------------------------------------------------------------------------------------------------------->')


    def table_integral_head():
        """Function to display sukkar and cornell
        table of integral-head


        Return:
            dataframe: for the first forty five rows

        """

        return df2.head(45)


    #     Stores table_integral_head in the variable t1
    t1 = table_integral_head()

    print(t1)
    print('<------------------------------------------------------------------------------------------------------>')

    #     First interpolation to compute the sukkar and cornell integral value

    ppr_above = float(input("what is the value of CELL ABOVE 'Ppr'? "))
    ppr_below = float(input("what is the value of CELL BELOW 'Ppr'? "))
    sciv_above = float(input("what is the sukkarcornel integral value corresponding to 'value of CELL ABOVE Ppr'? "))
    sciv_below = float(input("what is the sukkarcornel integral value corresponding to 'value of CELL BELOW Ppr'? "))

    a = ppr_above - pseudo_reduced_wellhead_pressure()
    a2 = ppr_above - ppr_below
    b = sciv_above - sciv_below


    def interpolated_integral_value():
        """Function to interpolate sukkar and cornell
        integral value


        Return:
           i_integral_value(floats): interpolated integral value

        """

        i_integral_value = sciv_above - ((a / a2) * b)

        return i_integral_value


    def real_integral_value():
        """Function to calculate real integral value


        Return:
            real_value(floats): Difference btw interpolated value and
            the sukkar and cornell integral-RHS

        """

        real_value = interpolated_integral_value() - evaluate_scrhs()

        return real_value


    print('')
    print('<-------------------------------------------------------->')
    print(f"sukkarcornel integral value is:{real_integral_value()}")
    print('<-------------------------------------------------------->')
    print('')

    #     Second interpolation to compute reduced pressure at real integral value
    upper_value_integral = float(input('what is the integral value of CELL ABOVE "sukkarcornel integral value"? '))
    lower_value_integral = float(input('what is the integral value of CELL BELOW "sukkarcornel integral value"? '))
    ppr_of_upper_value_integral = float(
        input('what is the value of Ppr corresponding to integral value of CELL ABOVE "sukkarcornel integral value"? '))
    ppr_of_lower_value_integral = float(
        input('what is the value of Ppr corresponding to integral value of CELL BELOW "sukkarcornel integral value"? '))

    i = upper_value_integral - real_integral_value()

    i2 = upper_value_integral - lower_value_integral

    pr = ppr_of_upper_value_integral - ppr_of_lower_value_integral


    def pseudo_reduced_bhp():
        """Function to compute reduced
        bottom hole pressure


        Return:
            floats: pseudo-reduced BHP rounded to
            three decimal places

        """

        reduced_bhp = ppr_of_upper_value_integral - (i / i2) * pr

        return round(reduced_bhp, 3)


    def static_bhp():
        """Function to compute the
        Static Bottom Hole Pressure


        Return:
            pws(floats): The static BHP rounded to 3
            decimal places

        """

        pws = pseudo_reduced_bhp() * natural_gas_systems2()

        return f"The static_BHP is:{round(pws, 3)} psia"


    print('')
    print('<-------------------------------------->')
    print(static_bhp())

else:
    print(err_msg())

