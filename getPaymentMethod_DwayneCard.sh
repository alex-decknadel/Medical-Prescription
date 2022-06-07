# Alex Decknadel

# Extract information about customer's payment methods.

# Output heading.
echo "Credit cards used by Dwayne Amiya:"

# Extract desired payment method records.
cat prescription_data.csv |
	grep "Dwayne \w\+. Amiya" |
	grep "Credit" |

# Extract desired _fields_.
cut -d, -f2,4,5