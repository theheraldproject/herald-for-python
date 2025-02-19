#  Copyright 2025 Herald Project Contributors
#  SPDX-License-Identifier: Apache-2.0
#

# Provides Herald Analysis API links, allowing applications to receive and analysis Herald Bluetooth and device sensor data.

class Sample:
  """Represents a Herald Analysis API Sample. SHOULD NOT be subclassed."""
  def __init__(self, value: float):
    self.value = value
  
  def getValue(self):
    return self.value



class AnalyserInterface:
  """An interface provided by the micropython or interpreter allowing you to produce new data and pass to other functions."""
  def __init__(self):
    pass
  
  def produce(self, sensor: str, sample: Sample):
    pass



class AnalysisConsumer:
  """Represents an AnalysisConsumer. You subclass these to collect and process data."""
  def __init__(self, analyser):
    """DO NOT replace this. It must be called. Provides your class with an analyser context, allowing you to produce new Samples to other applet code. (Analysis chaining)"""
    self.analyser = analyser

  def getName(self):
    """Provides Herald with a name. Used mainly for logging and debugging. Keep it short!"""
    return None

  def receiveRawSample(self, sensor: str, sample: Sample):
    pass
    # Note: You may call self.analyser