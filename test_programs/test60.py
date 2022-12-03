from os import dup
from tempfile import NamedTemporaryFile


def platforms_required(arrivals, departures):
    no_of_platforms = 1

    arrivals.sort()
    departures.sort()

    i, j = 1, 0

    while i < len(departures):
        if departures[j] < arrivals[i]:
            j += 1
        else:
            no_of_platforms += 1
        i += 1

    return no_of_platforms

arrivals = [int(arrival) for arrival in "1026 0445 0145 0555 0710 1712 1105 0506 0531 1930 0220 0611 0553 0053 0401 2000 0225 1359 1159 0120 1857 0740 0253 0303 0740 1434 1407 0807 0423 0500 0851 0809 0527 0123 1117 0023 1050 1613 1025 1225 0826 0422 0221 0028 0515 0401 1241 0038 0315 1007 0508 1054 0803 0333 0011 0225 0137 0030 0344 0036 0841 1419 0552 0422 0337 1222 1422 0010 0258 1434 0538 0153 0808 0347 0104 1136 0302 0357 0938 2015 0403 0258 0736 1057 1547 0531 1642 2333 0511 1301 1059 0638 0117 0314 0905 1314 1103 0356 0006 0235 1209 0849 0304 0539 0921 0625 0741 0047 0055 0127 0003 0053 0608 1725 1431 1427 0814 0935 1435 0938 0448 0930 0549 1002 0909 0329 1203 0824 0212 0852 1825 0541 1136 0825 0110 1301 1619 0031 0037 0140 0443 0831 1220 0346 1242 1414 1702 0113 0901 1221 0742 0941 0711 0825 0220 1526 0125 0006 1418 1632 1020 1957 0711 0552 0430 0157 0359 0212 1150 2212 0857 1351 1531 0219 0006 0813 0141 1730 0458 0911 1201 0218 0441 1121 0216 0501 0528 1049 0158 0646 1303 0018 0123 1408 1750 0604 1042 0001 1049 0343 0821 0154 0139 1138 1138 2107 0318 0556 1259 0044 0457 0116 1555 1546 0525 1648 1612 0504 1218 2231 1408 0922 1253 0353 0759 0727 0817 0015 0650 0519 1723 1329 0357 0839 0440 0824 0805 1524 0943 0116 0937 0740 0357 1023 0314 0931 1844 1639 0232 0023 0549 0028 1135 1220 0449 0925 1112 1652 0609 2316 1205 0133 0223 0543 1004 1426 0814 0422 1134 0228 0832 0641 1643 1339 1725 1023 1017 1642 0627 0642 0934 1349 0624 1411 0246 0508 1113 0955 0014 0258 0502 0749 1423 0400 0809 0157 2100 0120 0935 1417 1204 1016 0144 0724 1221 0207 1745 1905 0333 0324 1407 1537 1246 1543 0226 1031 1045 1325 0957 0419 0528 0419 1239 0131 0452 0834 0003 0430 0544 0348 0538 0952 1956 0024 1140 0407 0800 0026 1101 1301 0838 0555 0816 0130 1645 0025 0013 0136 0810 1624 0819 0811 1138 0622 1643 1113 1434 1311 1501 0847 0950 0356 0305 1825 1135 0946 1550 0211 0835 0539 0335 1123 0904 0938 0812 1339 1921 1511 0709 0130 1222 0820 0405 0330 1254 0432 0130 0033 0254 0826 0343 0830 1708 0657 1149 1148 0406 1204 1253 1006 0421 0258 2022 1027 0110 1426 0458 0128 0039 0537 0737 1938 0849 0424 1332 0140 1123 0103 0250 0600 0749 0247 1243 0108 0138 1119 0443 0409 0343 0654 0413 0658 0333 0022 0739 0453 0051 0104 0240 1201 1328 0208 0242 1020 1305 0708 0630 1314 1018 1104 2137 0224 1051 0543 0838 0539 0606 0949 1435 1034 0402 1105 0936 0530 0946 1629 1641 0744 0023 0508 0036 0300 0756 0302 0733 0600 2009 0804 0653 1312 0024 1217 0345 0301 1450 0103 1512 0905 0000 0012 0854 0451 0317 0336 0125 0400 0829 0202 0927 0257 0511 0406 1548 0453 1518 1057 2016 0522 0938 0346 0536 1723 0531 0727 0232 1050 0155 0738 2012 0957 0555 0504 0652 1301 0522 0351 0136 0511 0334 0410 0933 0805 1603 1808 0105 0325 1814 0024 0552 0401 0041 1412 0800 0133 0007 0755 2005 1258 1034 1215 0014 1553 0807 0310 1416 0246 0243 0026 0857 2157 1605 0555 1322 0253 1130 0702 1350 0050 0105 0345 0121 0350 0300 1616 0448 1008 0737 0629 0700 0945 0045 0817 1947 0549 1451 1732 0935 0135 0132 0408 1407 1801 1640 0050 0313 0021 0308 1320 1207 2216 1918 0111 0348 0621 0030 0842 0818 0028 1056 1941 1635 1111 0508 0420 0139 1036 0717 1250 0320 0536 0018 0156 0808 1754 0451 0432 0236 1128 0912 1326 1525 0526 0355 0439 0223 1702 2109 0503 1629 0224 0107 1649 1338 0722 0840 0923 0001 0144 0102 1128 0839 0329 0443 1402 1132 0226 0422 0456 0157 1126 0458 1114 0600 0012 0301 0313 1213 0210 1110 0205 0034 0042 0320 0313 0101 0253 0301 0311 1539 1911 0835 1556 1049 0017 0530 1604 0002 0410 0117 0428 1638 0930 0349 0708 1327 0118 0929 0402 0437 2143 0424 0751 0230 2321 0030 1555 1446 0404 1135 0914 1305 0215 0455 0356 1216 0302 0815 1357 0952 1051 0036 0059 0030 0147 0403 1720 0722 1509 0423 0207 0428 0214 1227 0448 0111 0206 0248 0313 0246 0424 1416 0738 1240 0558 1625 0548 0739 0134 0704 0656 0836 0302 0553 0105 0101 0115 1438 0208 0244 1503 1231 1619 0616 0934 1524 0800 0740 1146 0347 1002 1550 0943 0657 0256 0559 0234 0745 1002 0709 0801 0345 1138 0536 2214 0659 0427 0850 0145 1938 0726 0328 0407 1512 0358 0439 0538 0326 2305 0015 0854 1636 0403 1556 0218 1139 1319 1042 0216 1103 0206 1519 0920 0228 0203 0444 0911".split(" ")]
departures = [int(departure) for departure in "1713 2242 1144 0848 1941 1734 2347 1726 2247 2018 0355 2249 2134 0758 2044 2354 0237 2152 1221 0532 2031 0820 1013 2311 2150 2321 1909 2344 1732 2127 2126 1602 0945 0705 1632 1305 1604 1639 1630 1334 1858 2131 0350 1625 1443 0926 1245 1802 1558 1406 1442 2024 1450 0703 0508 1341 1445 1624 1414 2143 1306 1808 0845 1717 1928 1620 1631 1101 2146 2153 1524 2306 0944 0702 1219 1318 1431 2044 1616 2106 1631 0841 1128 1732 1957 0719 2052 2342 2016 1348 1505 0957 1749 0509 2140 1515 2114 1245 1806 1439 1951 2341 0518 2315 2304 1117 1701 1837 0346 2200 0118 1537 0714 1757 2237 2139 2103 1707 2031 1848 1623 2105 2125 1205 1730 0512 1928 1816 2250 1624 1828 1227 2308 1044 0809 1636 2101 0321 0121 1237 1157 1633 1731 2050 1419 1724 2155 0705 2109 2343 0844 2246 2037 1452 1131 2135 1441 0549 1810 2039 2306 2215 1057 0739 2323 1250 1024 1856 2152 2238 2323 1855 1920 0454 1008 2059 1556 2202 1645 2320 1843 1812 1011 2052 1639 1555 2234 2025 1502 2224 1742 0957 1527 2110 1929 1712 2159 0239 2113 1841 2211 1221 1028 2124 1614 2139 2240 0926 1527 1839 0721 2316 1931 1648 0817 1707 2002 0921 2342 2336 1842 2257 1925 0827 1800 1349 1949 1242 0906 1954 1732 1721 2010 2349 2034 1527 1328 2000 2130 1804 1745 1105 1406 2245 1649 1411 2300 2330 0713 0553 2329 0632 1556 1942 1446 1510 1253 2341 1532 2322 1810 0445 1953 1619 1436 2145 1115 0715 1245 2126 1834 2101 2326 1850 1736 1346 1914 1806 0727 2249 1611 1700 1410 1910 1831 1355 2136 2157 0229 0446 1022 1914 1709 1717 1442 1748 2156 0651 1424 1951 2304 1154 2200 1059 1510 2047 2142 2013 1303 0901 2134 1927 1256 2205 0709 2129 1602 1336 1045 0821 2352 1559 1626 1224 0627 2134 1348 1827 1508 1001 1051 1546 2101 1934 2011 2339 1807 0953 2005 1542 2144 1448 2203 0452 1934 1309 0622 0853 1814 1812 1557 2039 1920 1627 2149 1955 1519 1312 1702 2252 1107 1049 0420 2128 1717 2146 1751 1413 2335 1815 0817 1907 2211 1023 2318 1423 1957 1616 2012 2308 1259 2114 0808 1527 2135 1638 1956 0408 0655 1346 0527 1248 2055 2235 1358 1501 0907 2101 2244 2108 0929 2200 2056 1532 0256 1900 2218 1358 0214 1414 1105 2311 1232 0611 1848 1543 1459 0743 1143 1905 2241 1758 1446 0136 2323 1705 2057 0504 2029 1708 1642 1945 0926 0802 1821 1028 1145 1527 1531 1419 1730 0243 0324 2131 2117 2022 1426 1836 1540 1319 2337 2304 1948 1607 1220 1407 1804 2209 2025 1412 1729 2134 1353 0905 1529 1647 2345 0848 0835 0947 1710 1325 1519 2255 0803 1008 2048 2005 1952 2328 1717 1523 2043 2141 1711 1030 2211 1522 0202 0043 1022 1848 1457 1313 0448 0722 1601 2005 1042 1802 2114 1145 2253 2209 2210 1705 2128 0624 1345 1648 2009 2242 1248 2214 1019 2020 1447 2144 2119 2056 2356 1646 1002 2331 0657 0428 0422 0608 1149 2047 1900 1241 2358 2201 0755 1351 2317 1623 2205 1518 2210 1518 1657 1838 2026 0822 2203 1449 1639 1313 2241 1814 1023 1611 1626 0708 1743 0125 2302 2254 2143 1922 1710 0604 1204 2020 1414 1947 0409 1747 0626 0751 1729 1710 2334 2304 1750 0839 1120 1929 1640 1605 1951 1433 1607 2306 1343 2203 0622 2341 1705 1905 2318 1218 1946 1354 0344 1803 1858 2229 2237 2303 0946 1420 1956 1118 2246 1957 1738 2038 2217 1217 1236 0836 1816 1744 0832 1932 2300 2037 1304 0514 1004 2257 1722 2112 1221 2035 1956 1918 1833 2225 1823 1505 1952 2343 2110 1611 2024 0233 1220 1935 1750 1457 1212 1003 1126 1034 0454 1922 1714 2323 1619 1446 1943 1543 2243 1114 0840 2212 2316 1258 1126 0629 0514 1416 1608 1821 1442 0842 1554 1251 1231 1030 1804 2051 2339 0714 2109 2232 1423 2351 1853 1919 1637 2250 1155 2106 2029 1646 2330 1719 2153 1156 1925 0417 2039 1118 2131 2238 2355 1730 2142 2357 1210 1956 1626 0611 1409 2256 2243 1157 2324 1509 2001 1022 1845 2333 2255 1305 0935 0646 0113 1348 2333 2304 1522 2207 2018 0408 1657 1757 1547 1404 0849 1549 2102 0331 1622 1827 2135 2307 1635 1137 1805 0945 1822 2027 1657 0954 2358 0340 0850 1720 0811 0715 2121 1826 1626 2004 1405 1931 2246 2047 2218 1022 1439 1401 1900 2130 2328 2119 1851 0428 1235 1811 1040 1906 2212 1937 1405 2210 0710 2359 1021 0759 1406 0312 2110 1238 0839 2110 2021 0854 0850 0912 2329 2350 1253 1802 2114 0632 2350 0900 2204 1853 1419 1038 1556 0259 1601 1738 1701 2302 2140 1147".split(" ")]

# print(platforms_required(arrivals, departures))

def set_matrix_zeros(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True


    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0

    if row_zero:
        for c in range(cols):
            matrix[0][c] = 0

    return matrix

# matrix = [[0,1,1],[1,1,1],[1,1,0]]
# print(set_matrix_zeros(matrix))


def pascals_triangle(n):
    res = [[1]]

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []

        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)

    return res

# print(pascals_triangle(5))

class NextPermutation:

    def swap(self, nums, ind1, ind2):
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp

    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1

    def next_permutation(self, nums):
        if len(nums) == 1:
            return nums

        if len(nums) == 2:
            return self.swap(nums, 0, 1)

        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1

        self.reverse(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return nums

        next_num = dec + 1
        while nums[next_num] <= nums[dec] and next_num <= len(nums) - 1:
            next_num += 1

        self.swap(nums, next_num, dec)

        return nums

# print(NextPermutation().next_permutation([1,5,4,3,2]))

def maximum_subarray_sum(nums):
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(curr_sum, max_sum)

    return max_sum

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(maximum_subarray_sum(arr))

def swap(nums, ind1, ind2):
    temp = nums[ind1]
    nums[ind1] = nums[ind2]
    nums[ind2] = temp

    return nums

def sort_array_of_0s_1s_and_2s(nums):
    l, r = 0 , len(nums) - 1
    i = 0

    while i <= r:
        if nums[i] == 0:
            swap(nums, l, i)
            l += 1
        elif nums[i] == 2:
            swap(nums, i, r)
            r -= 1
            i -= 1
        i += 1

    return nums

# print(sort_array_of_0s_1s_and_2s([2,0,2,1,1,0]))

def stock_buy_and_sell(nums):
    left, right = 0, 1
    max_profit = 0
    
    while right < len(nums):
        if nums[left] < nums[right]:
            curr_profit = nums[right] - nums[left]
            max_profit = max(curr_profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit

# print(stock_buy_and_sell([7,1,5,3,6,4]))

def rotate_matrix(matrix):
    left, right = 0, len(matrix[0]) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            temp = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = temp

        right -= 1
        left += 1

    return matrix

input = [   [1,2,3,4],
            [4,5,6,7],
            [7,8,9,1], 
            [1,2,3,4]]
# print(rotate_matrix(input))


def merge_overlapping_subintervals(intervals):
    intervals.sort(key = lambda i: i[0])
    new_intervals = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = new_intervals[-1][1]

        if start <= last_end:
            new_intervals[-1][1] = max(end, last_end)
        else:
            new_intervals.append([start, end])

    return new_intervals

# input = [[1,3],[5,10],[6,7], [2,5]]
# print(merge_overlapping_subintervals(input))

def merge_two_sorted_arrays(arr1, arr2):
    i, j = len(arr1) - 1, 0

    while j < len(arr2) and i >= 0:
        if arr1[i] > arr2[j]:
            temp = arr1[i]
            arr1[i] = arr2[j]
            arr2[j] = temp

        i -= 1
        j += 1

    arr1.sort()
    arr2.sort()

    return arr1, arr2    


# arr1 = [1,3,5,7]
# arr2 = [4,6,10]
# print(merge_two_sorted_arrays(arr1, arr2))

    
def find_duplicate(nums):
    slow = fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow2 = 0

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

# print(find_duplicate([1,3,4,2,5,6,2]))


def find_repeat_and_missing_number(nums):
    for i in range(len(nums)):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            duplicate = abs(x) + 1
        else:
            nums[x] = -nums[x]

    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    return duplicate, missing

# print(find_repeat_and_missing_number([1,3,2,4,5,5]))

class CountInversions:

    def count_inversions_in_array(self, nums):
        self.count = 0
        self.merge_sort(nums)
        return self.count

    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_array = nums[:mid]
            right_array = nums[mid:]

            self.merge_sort(left_array)
            self.merge_sort(right_array)

            i,j,k = 0,0,0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    nums[k] = left_array[i]
                    i += 1
                else:
                    nums[k] = right_array[j]
                    j += 1
                    self.count += len(left_array) - i
                k += 1
            
            while i < len(left_array):
                nums[k] = left_array[i]
                i += 1
                k += 1
        
            while j < len(right_array):
                nums[k] = right_array[j]
                j += 1
                k += 1

        return nums


# print(CountInversions().count_inversions_in_array([5,4,3,2]))

def search_in_2d_matrix(matrix, target):
    top, bottom = 0, len(matrix) - 1

    while top < bottom:
        mid_row = (top + bottom) // 2

        if target < matrix[mid_row][0]:
            bottom = mid_row - 1
        elif target > matrix[mid_row][-1]:
            top = mid_row + 1
        else:
            break

    if top > bottom:
        return False

    mid_row = (top + bottom) // 2
    left, right = 0, len(matrix[0]) - 1

    while left <= right:
        mid = (left + right) // 2
        if target < matrix[mid_row][mid]:
            right = mid - 1
        elif target > matrix[mid_row][mid]:
            left = mid + 1
        else:
            return True

    return False

matrix = [  [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]]
# matrix = [[1]]
# print(search_in_2d_matrix(matrix, 0))

class PowXN:

    def pow_x_n(self, x, n):
        res = self.pow(x,abs(n))
        return res if n > 0 else 1/res

    def pow(self, x, n):
        if x == 0: return 0
        if n == 0: return 1

        res = pow(x * x, n // 2)
        return res if n % 2 == 0 else res * x

    
# print(PowXN().pow_x_n(2,-10))

def majority_element_n_by_2(nums):
    candidate = 0
    life = 0

    for num in nums:
        if num == candidate:
            life += 1
        elif life == 0:
            candidate = num
            life += 1
        else:
            life -= 1

    return candidate

# print(majority_element([2,2,2,2,2,3,3,3,3]))

def majority_element_n_by_3(nums):
    res = []
    candidate1 = 0
    life1 = 0

    candidate2 = 0
    life2 = 0

    for num in nums:
        if candidate1 == num:
            life1 += 1
        elif candidate2 == num:
            life2 += 1
        elif life1 == 0:
            candidate1 = num
            life1 += 1
        elif life2 == 0:
            candidate2 = num
            life2 += 1
        else:
            life1 -= 1
            life2 -= 1

    count1 = 0
    count2 = 0
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1

    if count1 > len(nums) / 3:
        res.append(candidate1)
    if count2 > len(nums) / 3:
        res.append(candidate2)

    return res

# print(majority_element_n_by_3([0,0,0]))

def grid_unique_paths(m, n):
    row = [1] * n

    for i in range(m - 1):
        temp = [1] * n
        for j in range(n-1, -1, -1):
            temp[j - 1] = temp[j] + row[j - 1]
        row = temp
    return row[0]

# print(grid_unique_paths(3, 6))

class ReversePairs:

    def reverse_pairs(self, nums):
        self.count = 0
        self.merge_sort(nums)
        return self.count

    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_array = nums[:mid]
            right_array = nums[mid:]

            self.merge_sort(left_array)
            self.merge_sort(right_array)

            i,j = 0,0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] > 2 * right_array[j]:
                    self.count += len(left_array) - i
                    i += 1
                else:
                    j += 1

            i,j,k = 0,0,0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    nums[k] = left_array[i]
                    i += 1
                else:
                    nums[k] = right_array[j]
                    j += 1
                k += 1
            
            while i < len(left_array):
                nums[k] = left_array[i]
                i += 1
                k += 1
        
            while j < len(right_array):
                nums[k] = right_array[j]
                j += 1
                k += 1

        return nums

# print(ReversePairs().reverse_pairs([2,4,3,5,1]))

def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return (left + 1, right + 1)

# print(two_sum([1,3,4,5,7,10,11], 9))

def four_sum(nums, target):
    nums.sort()
    res, quad = [], []

    def k_sum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                k_sum(k - 1, i + 1, target - nums[i])
                quad.pop()
            return
        
        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append(quad + [nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    k_sum(4, 0, target)
    return res


# print(four_sum([1,0,-1,0,-2,2], 0))

def longest_consecutive_sequence(nums):
    nums = set(nums)
    longest = 0

    for num in nums:
        if (num - 1) in nums:
            continue
        length = 1
        while (num + length) in nums:
            length += 1
        longest = max(longest, length)
        
    return longest

# print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))


n = 5
res = 1
for i in range(n, 0, -1):
	res *= i
# print(res)



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

