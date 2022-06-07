# Alex Decknadel

# Extract information about customer's payment methods.

# Whitespace
echo ""

# Set name and type, prompt if needed.
firstName=$1; lastName=$2; type=$3;
if [[ ! "$type" ]]
then
	echo -n "First Name: "; read firstName
	echo -n "Last Name: "; read lastName
	echo -n "Payment Type: "; read type
fi

# Output heading.
echo ""

if [[ -z "$firstName" ]]; then
	if [[ -z "$lastName" ]]; then
		if [[ -z "$type" ]]; then
			echo "Please try again!"
			return 0
		else
			echo "Any payment method that uses $type:"
		fi
	elif [[ -z "$type" ]]; then
		echo "Any payment type used by anyone with the last name $lastName:"
	else
		echo "$type used by anyone with the last name $lastName:"
	fi
elif [[ -z "$lastName" ]]; then
	if [[ -z "$type" ]]; then
		echo "Any payment type used by anyone named $firstName:"
	else
		echo "$type used by anyone named $firstName:"
	fi
elif [[ -z "$type" ]]; then
	echo "Any payment type used by $firstName $lastName:"
else
	echo "$type used by $firstName $lastName:"
fi

# Extract desired payment method records.
cat prescription_data.csv |
	grep -i "$firstName" |
	grep -i "$lastName" |
	grep -i "$type" |

# Extract desired _fields_.
cut -d, -f5,2,4

# Whitespace
echo ""