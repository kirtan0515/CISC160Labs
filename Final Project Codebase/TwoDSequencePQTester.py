'''
' Tester code for Question 05 (TwoDSequencePQ) of the Final Project.
'''

from TwoDSequencePQ import TwoDSequencePQ

#7.1) Test the TwoDSequencePQ constructor
print("------------------------------------------------------------")
print("7.1) Test the TwoDSequencePQ constructor")
print("------------------------------------------------------------")

pq = TwoDSequencePQ()
pause = False

print("len:      0\t= " + str(len(pq)))
print("is_empty: True\t= " + str(pq.is_empty()))

if pause:
    ()
else:
    print()

#7.2) Test accessing an empty TwoDSequencePQ
print("------------------------------------------------------------")
print("7.2) Test accessing an empty TwoDSequencePQ")
print("------------------------------------------------------------")

try:
    print("None:\t= " + str(pq.min()))
except:
    print("None:\t= None (via exception)")

try:
    print("None:\t= " + str(pq.remove_min()))
except:
    print("None:\t= None (via exception)")

if pause:
    input()
else:
    print()

#7.3) Test the TwoDSequencePQ add method with ints as keys
print("------------------------------------------------------------")
print("7.3) Test the TwoDSequencePQ add method with ints keys")
print("------------------------------------------------------------")

pq = TwoDSequencePQ()

pq.add(5, 10)

print("len:      1\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (5, 10)\t\t    = " + str(pq.min()))
print()

pq.add(2, 1)

print("len:      2\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (2, 1)\t\t    = " + str(pq.min()))
print()

pq.add(23, "My Password is Taco")

print("len:      3\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (2, 1)\t\t    = " + str(pq.min()))
print()

pq.add(10, "Baklava")

print("len:      4\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (2, 1)\t\t    = " + str(pq.min()))
print()

pq.add(0, "Should be second")

print("len:      5\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be second')   = " + str(pq.min()))
print()

pq.add(123, "Last")

print("len:      6\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be second')   = " + str(pq.min()))
()

pq.add(14, "Weird, right?")

print("len:      7\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be second')   = " + str(pq.min()))
print()

pq.add(0, "Should be first")

print("len:      8\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be <either>') = " + str(pq.min()))
print()

pq.add(47, 555.55)

print("len:      9\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be <either>') = " + str(pq.min()))
print()

pq.add(1, ["A", "list", "of", "stuff"])

print("len:      10\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be <either>') = " + str(pq.min()))
print()

pq.add(15, "¡Top!")

print("len:      11\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be <either>') = " + str(pq.min()))
print()

if pause:
    input()
else:
    print()

#7.4) Test the TwoDSequencePQ min and remove_min methods
print("------------------------------------------------------------")
print("7.4) Test the TwoDSequencePQ min and remove_min methods")
print("------------------------------------------------------------")

print("remove_min: (0, 'Should be <either>')\t= " + str(pq.remove_min()))
print("len:        10\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (0, 'Should be <either>')\t= " + str(pq.min()))
print("remove_min: (0, 'Should be <either>')\t= " + str(pq.remove_min()))
print("len:        9\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.min()))
print("remove_min: (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.remove_min()))
print("len:        8\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (2, 1)\t\t\t= " + str(pq.min()))
print("remove_min: (2, 1)\t\t\t= " + str(pq.remove_min()))
print("len:        7\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (5, 10)\t\t\t= " + str(pq.min()))
print("remove_min: (5, 10)\t\t\t= " + str(pq.remove_min()))
print("len:        6\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))

if pause:
    input()
else:
    print()

print("min:        (10, 'Baklava')\t= " + str(pq.min()))
print("remove_min: (10, 'Baklava')\t= " + str(pq.remove_min()))
print("len:        5\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (14, Weird, right?')\t= " + str(pq.min()))
print("remove_min: (14, Weird, right?')\t= " + str(pq.remove_min()))
print("len:        4\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (15, '¡Top!')\t\t= " + str(pq.min()))
print("remove_min: (15, '¡Top!')\t\t= " + str(pq.remove_min()))
print("len:        3\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (23, 'My Password is Taco')\t= " + str(pq.min()))
print("remove_min: (23, 'My Password is Taco')\t= " + str(pq.remove_min()))
print("len:        2\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (47, 555.55)\t\t= " + str(pq.min()))
print("remove_min: (47, 555.55)\t\t= " + str(pq.remove_min()))
print("len:        1\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (123, 'Last')\t\t= " + str(pq.min()))
print("remove_min: (123, 'Last')\t\t= " + str(pq.remove_min()))
print("len:        0\t\t\t\t= " + str(len(pq)))
print("is_empty:   True\t\t\t= " + str(pq.is_empty()))

if pause:
    input()
else:
    print()

#7.5) Try to test the underlying heap structure. MAY NOT WORK!
print("------------------------------------------------------------")
print("7.5) Try to test the underlying heap structure. MAY NOT WORK!")
print("     NOTE: Only populated priorities will print!")
print("           If nothing is at a given priority, it will be skipped.")
print("------------------------------------------------------------")

pq = TwoDSequencePQ()

pq.add(5, 10)
pq.add(2, 1)
pq.add(23, "My Password is Taco")
pq.add(10, "Baklava")
pq.add(0, "Should be second")
pq.add(123, "Last")
pq.add(14, "Weird, right?")
pq.add(0, "Should be first")
pq.add(47, 555.55)
pq.add(1, ["A", "list", "of", "stuff"])
pq.add(15, "¡Top!")

pointer = None

if pointer is None:
    try:
        pointer = pq._head
    except:
        pass

if pointer is None:
    try:
        pointer = pq.head
    except:
        pass

if pointer is None:
    try:
        pointer = pq._head_node
    except:
        pass

if pointer is None:
    try:
        pointer = pq.head_node
    except:
        pass

if pointer is None:
    try:
        pointer = pq._h
    except:
        pass

if pointer is None:
    try:
        pointer = pq.h
    except:
        pass

if pointer is None:
    try:
        pointer = pq._header
    except:
        pass

if pointer is None:
    try:
        pointer = pq.header
    except:
        pass

if pointer is None:
    try:
        pointer = pq._first
    except:
        pass

if pointer is None:
    try:
        pointer = pq.first
    except:
        pass

if pointer is None:
    try:
        pointer = pq._data
    except:
        pass

if pointer is None:
    try:
        pointer = pq.data
    except:
        pass

if pointer is None:
    try:
        pointer = pq._node
    except:
        pass

if pointer is None:
    try:
        pointer = pq.node
    except:
        pass

if pointer == None:
    print("Array unidentified. Check the internal structure.")
else:
    i = 0
    while i <= 123: #Maximum key
        if pointer[i] != []:
            if pointer[i] is None:
                values = "None"
            else:
                values = pointer[i]

            print("Key: " + str(i) + "; Values: " + str(values))
        i += 1

    if len(pointer) > 124:
        print("NOTE! Array is too big! Length of " + str(len(pointer)) + " exceeds 124 (maximum key + 1)!")

if pause:
    input()
else:
    print()

#7.6) Test the various key types that shouldn't be allowed
print("------------------------------------------------------------")
print("7.6) Test the various key types that shouldn't be allowed")
print("------------------------------------------------------------")

pq = TwoDSequencePQ()

try:
    pq.add(3.5, "Uh oh")
except:
    print("Good. Float key value failed. (Exception)")
else:
    if len(pq) == 0:
        print("Good. Float key value failed. (Not allowed)")
    else:
        print("FLOAT KEY VALUE ALLOWED!")

pq = TwoDSequencePQ()

try:
    pq.add("3", "Uh oh")
except:
    print("Good. String key value of an integer failed. (Exception)")
else:
    if len(pq) == 0:
        print("Good. String key value of an integer failed. (Not allowed)")
    else:
        print("STRING KEY VALUE OF AN INTEGER ALLOWED!")

pq = TwoDSequencePQ()

try:
    pq.add("Uh oh", "Uh oh")
except:
    print("Good. String key value failed. (Exception)")
else:
    if len(pq) == 0:
        print("Good. String key value failed. (Not allowed)")
    else:
        print("STRING KEY VALUE ALLOWED!")

pq = TwoDSequencePQ()

try:
    pq.add(-5, "¡Top!")
except:
    print("Good. Negative key value failed. (Exception)")
else:
    if len(pq) == 0:
        print("Good. Negative key value failed. (Not allowed)")
    else:
        print("NEGATIVE KEY VALUE ALLOWED!")
        pq.remove_min()
