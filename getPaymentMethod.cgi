#!/bin/bash
# Alex Decknadel
#
# Purpose: Extract information about customer's payment methods.

# Get and declare URL-provided inputs to set variables.
eval "declare ${QUERY_STRING//&/;}"

# Output heading.
echo "Content-type: text/csv "
echo ""

# Transforms spaces in previous input
payType=${payType//+/ }

if [[ -z "$firstName" ]]
then
	if [[ -z "$lastName" ]]
	then
		if [[ -z "$payType" ]]
		then
			echo "Please try again!"
			exit 0
		else
			echo "Any payment method that uses $payType:"
		fi
	elif [[ -z "$payType" ]]
     	then
		echo "Any payment type used by anyone with the last name $lastName:"
	else
		echo "$payType used by anyone with the last name $lastName:"
	fi
elif [[ -z "$lastName" ]]
then
	if [[ -z "$payType" ]] 
	then
		echo "Any payment type used by anyone named $firstName:"
	else
		echo "$payType used by anyone named $firstName:"
	fi
elif [[ -z "$payType" ]]
then
	echo "Any payment type used by $firstName $lastName:"
else
	echo "$payType used by $firstName $lastName:"
fi

# Extract desired payment method records.
cat /home/ubuntu/IS240/prescription_data.csv |
	grep -i "$firstName" |
	grep -i "$lastName" |
	grep -i "$payType" |

# Extract desired _fields_.
cut -d, -f5,2

# Whitespace
echo ""
