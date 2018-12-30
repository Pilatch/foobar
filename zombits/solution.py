def answer(y, x):
  sizeOfTestSetY = len(y)
  sizeOfTestSetX = len(x)
  if ( sizeOfTestSetY == 0 or sizeOfTestSetX == 0 or sizeOfTestSetX != sizeOfTestSetY ):
    return None

  # So these rabbits are REALLY consistent,
  # which means we expect the same percentage improvement for each test pair.
  # So we can look at any given test
  # and determine the improvement.
  # May as well choose the test with the smallest time.
  lowestX = min(x)
  lowestY = min(y)
  timeReduction = lowestX - lowestY
  timeReductionPercentageOfX = 100 * timeReduction / lowestX
  return int( round(timeReductionPercentageOfX) )
