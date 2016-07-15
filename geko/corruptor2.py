# corrupter2.py - Python module to corrupt (modify) generate synthetic data.
#
#                Part of a flexible data generation system.
#
# Peter Christen and Dinusha Vatsalan,  January-March 2012
# =============================================================================
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# =============================================================================

"""Module containing several classes to corrupt synthetic data according to
   user specification.
"""

# -----------------------------------------------------------------------------
# Import necessary modules

import math
import random
import basefunctions

# =============================================================================
# Helper functions to randomly select a position for where to apply a
# modification
from corruptor import *
# =============================================================================

class CorruptIncomeValue(CorruptValue):
  """Use a keyboard layout to simulate typing errors. They keyboard is
     hard-coded into this method, but can be changed easily for different
     keyboard layout.

     A character from the original input string will be randomly chosen using
     the position function, and then a character from either the same row or
     column in the keyboard will be selected.

     The additional arguments (besides the base class argument
     'position_function') that have to be set when this attribute type is
     initialised are:

     row_prob  The probability that a neighbouring character in the same row
               is selected.

     col_prob  The probability that a neighbouring character in the same
               column is selected.

     The sum of row_prob and col_prob must be 1.0.
  """

  # ---------------------------------------------------------------------------

  def __init__(self, **kwargs):
    """Constructor. Process the derived keywords first, then call the base
       class constructor.
    """

    self.row_prob = None
    self.col_prob = None
    self.name =     'Num Value'

    # Process all keyword arguments
    #
    base_kwargs = {}  # Dictionary, will contain unprocessed arguments

    base_kwargs['position_function'] = 0

#     CorruptValue.__init__(self, base_kwargs)  # Process base arguments


  # ---------------------------------------------------------------------------

  def corrupt_value(self, in_str):
    """Method which corrupts the given input string by replacing a single
       character with a neighbouring character given the defined keyboard
       layout at a position randomly selected by the position function.
    """

    if (len(in_str) == 0):  # Empty string, no modification possible
      return in_str
  
    mod_str = in_str
      
    if "." in in_str:
        if random.randint(0,100) > 50:
            mod_str = in_str.split(".")[0]
        else:
            rad = in_str.split(".")[0]
            n = str(random.randint(0,99))
            mod_str = rad + "." + n
    else:
        if random.randint(0,100) > 30:
            mod_str = in_str[:-2] + str(random.randint(0,9)) + str(random.randint(0,9))
            mod_str = mod_str+".00"
        else:
            mod_str = mod_str+".00"

    return mod_str

class CorruptDateValue(CorruptValue):
  """  """

  # ---------------------------------------------------------------------------

  def __init__(self, **kwargs):
    """Constructor. Process the derived keywords first, then call the base
       class constructor.
    """

    self.row_prob = None
    self.col_prob = None
    self.name =     'Num Value'

    # Process all keyword arguments
    #
    base_kwargs = {}  # Dictionary, will contain unprocessed arguments

    base_kwargs['position_function'] = 0

#     CorruptValue.__init__(self, base_kwargs)  # Process base arguments


  # ---------------------------------------------------------------------------

  def corrupt_value(self, in_str):
    """Method which corrupts the given input string by replacing a single
       character with a neighbouring character given the defined keyboard
       layout at a position randomly selected by the position function.
    """

    if (len(in_str) == 0):  # Empty string, no modification possible
      return in_str
    
    import string
    
    mod_str = string.replace(in_str,"/","-")


    return mod_str
