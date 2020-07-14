#!/usr/bin/env python3

from random import random
import time

def test(work_lambda, iters=1000):
  begin = time.time_ns()
  for _ in range(0, iters):
    work_lambda()
  end = time.time_ns()
  return (end - begin) / iters

class NormalPoint:
  def __init__(self, x):
    self.x = x

class SlotsPoint:
  __slots__ = ["x"]
  def __init__(self, x):
    self.x = x

def normal_work():
  some_data = []
  # Create
  for i in range(0, 1000):
    some_data.append(NormalPoint(random()))
  # Write
  for i in range(0, 1000):
    some_data[i].x = random()

  # Read
  a_sum = 0.0
  for i in range(0, 1000):
    a_sum += some_data[i].x

def slots_work():
  some_data = []
  # Create
  for i in range(0, 1000):
    some_data.append(SlotsPoint(random()))
  # Write
  for i in range(0, 1000):
    some_data[i].x = random()

  # Read
  a_sum = 0.0
  for i in range(0, 1000):
    a_sum += some_data[i].x
  

def main():

  # We are going to time how long it takes to:
  #  - create a lot of items
  #  - write to the x value on each item
  #  - read all the x values and compute a sum

  normal_ns = test(normal_work)
  slots_ns = test(slots_work)

  print(f"normal_ns={normal_ns}")
  print(f"slots_ns={slots_ns}")

  # Reverse processing order in case the python VM does something smart

  slots_ns = test(slots_work)
  normal_ns = test(normal_work)

  print(f"slots_ns={slots_ns}")
  print(f"normal_ns={normal_ns}")


if __name__ == '__main__':
  main()

