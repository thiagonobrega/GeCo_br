# Functions that can generate attribute values.
#
# These are functions that can be used in the GenerateFuncAttribute() class
# (see module generator.py). They generate values according to some internal
# functionality.
#
# The requirement of any such functions are:
# 1) that it must return a string
# 2) it can have been 0 and 5 parameters
# 
#
# Examples of such functions are:
# - Australian telephone numbers
# - Japanese telephone numbers
# - Credit card numbers
# - US social security numbers
# - Japanese social security numbers
# - Uniformly distributed age values between 0 and 100
# - Normally distributed age values between 0 and 110
# etc.

# Peter Christen and Dinusha Vatsalan, January-March 2012
# =============================================================================
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# =============================================================================

import random

import basefunctions

# -----------------------------------------------------------------------------
#
def generate_phone_number_australia():
  """Randomly generate an Australian telephone number made of a two-digit area
     code and an eight-digit number made of two blocks of four digits (with a
     space between). For example: `02 1234 5678'

     For details see: http://en.wikipedia.org/wiki/ \
                      Telephone_numbers_in_Australia#Personal_numbers_.2805.29
  """
  
#modificado por thiago

  area_code = random.choice(['083', '081', '084', '082', '088'])

  number1 = random.randint(3200,3999)
  number2 = random.randint(1,9999)

  oz_phone_str = str(area_code)+' '+str(number1).zfill(4)+' '+ \
                 str(number2).zfill(4)
  assert len(oz_phone_str) == 13
  assert oz_phone_str[0] == '0'

  return oz_phone_str

# -----------------------------------------------------------------------------
#
def generate_credit_card_number():
  """Randomly generate a credit card made of four four-digit numbers (with a
     space between each number group). For example: '1234 5678 9012 3456'

     For details see: http://en.wikipedia.org/wiki/Bank_card_number
  """

  number1 = random.randint(1,9999)
  assert number1 > 0

  number2 = random.randint(1,9999)
  assert number2 > 0

  number3 = random.randint(1,9999)
  assert number3 > 0

  number4 = random.randint(1,9999)
  assert number4 > 0

  cc_str = str(number1).zfill(4)+' '+str(number2).zfill(4)+' '+ \
           str(number3).zfill(4)+' '+str(number4).zfill(4)

  assert len(cc_str) == 19

  return cc_str

# -----------------------------------------------------------------------------
#
def generate_uniform_value(min_val, max_val, val_type):
  """Randomly generate a numerical value according to a uniform distribution
     between the minimum and maximum values given.

     The value type can be set as 'int', so a string formatted as an integer
     value is returned; or as 'float1' to 'float9', in which case a string
     formatted as floating-point value with the specified number of digits
     behind the comma is returned.

     Note that for certain situations and string formats a value outside the
     set range might be returned. For example, if min_val=100.25 and
     val_type='float1' the rounding can result in a string value '100.2' to
     be returned.

     Suitable minimum and maximum values need to be selected to prevent such a
     situation.
  """

  basefunctions.check_is_number('min_val', min_val)
  basefunctions.check_is_number('max_val', max_val)
  assert min_val < max_val

  r = random.uniform(min_val, max_val)

  return basefunctions.float_to_str(r, val_type)

# -----------------------------------------------------------------------------
#
def generate_uniform_age(min_val, max_val):
  """Randomly generate an age value (returned as integer) according to a
     uniform distribution between the minimum and maximum values given.

     This function is simple a shorthand for:

       generate_uniform_value(min_val, max_val, 'int')
  """

  assert min_val >= 0
  assert max_val <= 130

  return generate_uniform_value(min_val, max_val, 'int')

# -----------------------------------------------------------------------------

def generate_normal_value(mu, sigma, min_val, max_val, val_type):
  """Randomly generate a numerical value according to a normal distribution
     with the mean (mu) and standard deviation (sigma) given.

     A minimum and maximum allowed value can given as additional parameters,
     if set to None then no minimum and/or maximum limit is set.

     The value type can be set as 'int', so a string formatted as an integer
     value is returned; or as 'float1' to 'float9', in which case a string
     formatted as floating-point value with the specified number of digits
     behind the comma is returned.
  """

  basefunctions.check_is_number('mu', mu)
  basefunctions.check_is_number('sigma', sigma)
  assert sigma > 0.0

  if (min_val != None):
    basefunctions.check_is_number('min_val', min_val)
    assert min_val <= mu

  if (max_val != None):
    basefunctions.check_is_number('max_val', max_val)
    assert max_val >= mu

  if ((min_val != None) and (max_val != None)):
    assert min_val < max_val

  if (min_val != None) or (max_val != None):
    in_range = False  # For testing if the random value is with the range
  else:
    in_range = True

  r = random.normalvariate(mu, sigma)

  while (in_range == False):
    if ((min_val == None) or ((min_val != None) and (r >= min_val))):
      in_range = True

    if ((max_val != None) and (r > max_val)):
      in_range = False

    if (in_range == True):
      r_str = basefunctions.float_to_str(r, val_type)
      r_test = float(r_str)
      if (min_val != None) and (r_test < min_val):
        in_range = False
      if (max_val != None) and (r_test > max_val):
        in_range = False

    if (in_range == False):
      r = random.normalvariate(mu, sigma)

  if (min_val != None):
    assert r >= min_val
  if (max_val != None):
    assert r <= max_val

  return basefunctions.float_to_str(r, val_type)

# -----------------------------------------------------------------------------
#
def generate_normal_age(mu, sigma, min_val, max_val):
  """Randomly generate an age value (returned as integer) according to a
     normal distribution following the mean and standard deviation values
     given, and limited to age values between (including) the minimum and
     maximum values given.

     This function is simple a shorthand for:

       generate_normal_value(mu, sigma, min_val, max_val, 'int')
  """

  assert min_val >= 0
  assert max_val <= 130

  age = generate_normal_value(mu, sigma, min_val, max_val, 'int')

  while ((int(age) < min_val) or (int(age) > max_val)):
    age = generate_normal_value(mu, sigma, min_val, max_val, 'int')

  return age

#Funcao recebe o argumento ano e retorna o valor booleano indicando se e ou nao bissexto.
def ehBissexto(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0;

#by thiago
def generate_normal_date(min_val_month, max_val_month , min_year , max_year):
    
  """
  """

  min_val_day = 1
  max_val_day = 31
  
  assert min_val_month >= 1
  assert max_val_month <= 12
  
  assert min_year >= 1900
  assert max_year >= min_year
  
  if min_year == max_year:
      year = max_year
  else:
      year = int(generate_uniform_value(min_year,max_year,'int'))
  
  bisexto = ehBissexto(year)
  
  
  sigma = int(max_val_month/min_val_month)
    
  month = generate_normal_value(min_val_month, sigma, min_val_month, max_val_month, 'int')
  while ((int(month) < min_val_month) or (int(month) > max_val_month)):
    month = generate_normal_value(min_val_month, sigma, min_val_month, max_val_month, 'int')

#feb bisexto
  if month == 2 and not bisexto:
      if max_val_day > 28:
          max_val_day = 28

  if month == 2 and bisexto:
      if max_val_day > 29:
          max_val_day = 29

  if month in [4,6,9,11]:
      if max_val_day > 30:
          max_val_day = 30
  
  sigma = int(max_val_day/min_val_day)
  
  day = generate_normal_value(min_val_day, sigma, min_val_day, max_val_day, 'int')
  
  while ((int(day) < min_val_day) or (int(day) > max_val_day)):
      day = generate_normal_value(min_val_day, sigma, min_val_day, max_val_day, 'int')
  
  return str(day).zfill(2)+"/"+str(month).zfill(2)+"/"+str(year).zfill(2)

def generate_normal_datetime(min_val_day, max_val_day , min_val_month, max_val_month , min_year , max_year):
    
    mydate = generate_normal_date(min_val_day, max_val_day , min_val_month, max_val_month , min_year , max_year)
    
        
    h = generate_uniform_value(0,23,'int')
    m = generate_uniform_value(0,59,'int')
    s = generate_uniform_value(0,59,'int')
    hs = str(h).zfill(2)
    ms = str(m).zfill(2)
    ss = str(s).zfill(2)
    
    
    return mydate + ' ' + hs + ':'+ ms + ':' + ss


# =============================================================================

# If called from command line perform some examples: Generate values
#
if (__name__ == '__main__'):

  num_test = 20

  print 'Generate %d Australian telephone numbers:' % (num_test)
  for i in range(num_test):
    print ' ', generate_phone_number_australia()
  print

  print 'Generate %d credit card numbers:' % (num_test)
  for i in range(num_test):
    print ' ', generate_credit_card_number()
  print

  print 'Generate %d uniformly distributed integer numbers between -100' % \
        (num_test) + ' and -5:'
  for i in range(num_test):
    print ' ', generate_uniform_value(-100, -5, 'int'),
  print

  print 'Generate %d uniformly distributed floating-point numbers with ' % \
        (num_test) + '3 digits between -55 and 55:'
  for i in range(num_test):
    print ' ', generate_uniform_value(-55, 55, 'float3')
  print

  print 'Generate %d uniformly distributed floating-point numbers with ' % \
        (num_test) + '7 digits between 147 and 9843:'
  for i in range(num_test):
    print ' ', generate_uniform_value(147, 9843, 'float7')
  print

  print 'Generate %d uniformly distributed age values between 0 and 120:' % \
        (num_test)
  for i in range(num_test):
    print ' ', generate_uniform_age(0, 120)
  print

  print 'Generate %d uniformly distributed age values between 18 and 65:' % \
        (num_test)
  for i in range(num_test):
    print ' ', generate_uniform_age(18, 65)
  print

  print 'Generate %d normally distributed integer numbers between -200' % \
        (num_test) + ' and -3 with mean -50 and standard deviation 44:'
  for i in range(num_test):
    print ' ', generate_normal_value(-50, 44, -200, -3, 'int')
  print

  print 'Generate %d normally distributed floating-point numbers with ' % \
        (num_test) + '5 digits between -100 and 100 and with mean 22 and ' + \
        'standard deviation 74:'
  for i in range(num_test):
    print ' ', generate_normal_value(22, 74, -100, 100, 'float5')
  print

  print 'Generate %d normally distributed floating-point numbers with ' % \
        (num_test) + '9 digits with mean 22 and standard deviation 74:'
  for i in range(num_test):
    print ' ', generate_normal_value(22, 74, min_val=None, max_val= None,
                                     val_type='float9')
  print

  print 'Generate %d normally distributed floating-point numbers with ' % \
        (num_test) + '2 digits with mean 22 and standard deviation 24 that' + \
        ' are larger than 10:'
  for i in range(num_test):
    print ' ', generate_normal_value(22, 74, min_val=10, max_val=None,
                                     val_type='float2')
  print

  print 'Generate %d normally distributed floating-point numbers with ' % \
        (num_test) + '4 digits with mean 22 and standard deviation 24 that' + \
        ' are smaller than 30:'
  for i in range(num_test):
    print ' ', generate_normal_value(22, 74, min_val=None, max_val=40,
                                     val_type='float4')
  print

  print 'Generate %d normally distributed age values between 0 and 120' % \
        (num_test) + ' with mean 45 and standard deviation 22:'
  for i in range(num_test):
    print ' ', generate_normal_age(45, 22, 0, 120)
  print

  print 'Generate %d normally distributed age values between 18 and 65' % \
        (num_test) + ' with mean 30 and standard deviation 10:'
  for i in range(num_test):
    print ' ', generate_normal_age(30, 10, 18, 65)
  print
