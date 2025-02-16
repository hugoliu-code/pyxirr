import datetime

import pyxirr

dates = [
    datetime.date(2000, 1, 1),
    datetime.date(1994, 6, 15),
    datetime.date(1994, 7, 12),
    datetime.date(2017, 10, 30),
    datetime.date(2008, 1, 22),
    datetime.date(1977, 7, 1),
    datetime.date(2005, 12, 30),
    datetime.date(2005, 12, 30),
    datetime.date(2005, 12, 30),
    datetime.date(1976, 12, 19),
    datetime.date(1976, 12, 19),
    datetime.date(1976, 12, 19),
    datetime.date(2107, 3, 23),
]

cf1 = [
    -253524383149.60605,
    -0.0,
    -0.0,
    -0.0,
    -0.0,
    -1.1201669784316488,
    -0.01,
    -0.0,
    -0.0,
    -0.0,
    -0.0,
    -0.0,
    32017.129321072072,
]
cf2 = [
    -253524383149.60605,
    -0.0,
    -0.0,
    -0.0,
    -0.0,
    -1.1201669784316488,
    -0.01,
    -0.0,
    -0.0,
    -0.0,
    -0.0,
    -0.0,
    36590.74097669936,
]

cf3 = [
-1,
-0,
-0,
-0,
-0,
-0.000000000004418379662403645,
-0.00000000000003944393780103963,
-0,
-0,
-0,
-0,
-0,
0.00000014432829111788816
]

# Exhibit 1
# Falsifying example, if large floats are not not normalized
xirr1 = pyxirr.xirr(dates, cf1)
xirr2 = pyxirr.xirr(dates, cf2)

print(xirr1)
print(xirr2)

# Results:
# -0.13761159201780845
# 1.800265354828463e+17

# Exhibit 2
# Normalize cash flows
max_cf1 = max(abs(x) for x in cf1)
max_cf2 = max(abs(x) for x in cf2)
print(max_cf2)
normalized_cf1 = [x / max_cf1 for x in cf1]
normalized_cf2 = [x / max_cf2 for x in cf2]

# Calculate XIRR on normalized cash flows
xirr1 = pyxirr.xirr(dates, normalized_cf1)
xirr2 = pyxirr.xirr(dates, normalized_cf2)
xirr3 = pyxirr.xirr(dates, cf3)

print(xirr1)
print(xirr2)
print(xirr3)

# Normalized results:
# -0.13761159201780845
# -0.13653769882244854

print("------------------------")
for n in normalized_cf2:
    print(n)