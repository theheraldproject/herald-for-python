#  Copyright 2025 Herald Project Contributors
#  SPDX-License-Identifier: Apache-2.0
#

# This file holds API unique to the Micropython implementation. These API are also provided by the Interpreter class


class HeraldApplet:
  """Individual executable code for running on a Herald API compatible device. Override this class to create your own applet."""
  def __init__(self, environment):
    """ DO NOT replace this function. It must always be called."""
    self.analysisConsumers = []
    self.environment = environment

  def setup(self):
    """Override this function to implement your own applet initialisation. A good place to populate your self.analysisConsumers array."""
    pass
  
  def loop(self):
    """Override this function to periodically execute applet code. Note: Analysis API will called your Analysis Consumers itself - there's no need to poll and do this yourself."""
    pass

  def getAnalysisConsumers(self):
    """DO NOT replace this function. It is used by the Herald Analysis API to fetch your analysis consumers."""
    return self.analysisConsumers
  
