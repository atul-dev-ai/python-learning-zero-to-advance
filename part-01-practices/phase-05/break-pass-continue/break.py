"""
ekhane loop ba conditional control korar jonno bebohar kora hoy.
`break` loop thamiye dey.
`continue` current iteration skip kore next step e jay.
`pass` kichui kore na sudho placeholder hisebe kaj kore thake.ekhane code likhe ses hoy nai future e kono block boshano hobe.
"""

# break
for i in range(1, 6):
    if i == 3:
        break # 3 e pousiyei off kore dey
    print(i)


# continue
for x in range (1, 6):
    if x == 3:
        continue
    print(x)


