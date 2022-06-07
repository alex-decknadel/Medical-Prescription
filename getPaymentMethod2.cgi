#!/bin/bash
#
# Alex Decknadel
# Purpose: Extract desired customer payment information from prescription data store.

TITLE="Customer Payment Information"
SAMPLE_INPUTS="firstName=Dwayne&lastName=Amiya&payType=Credit"
 
# Get provided inputs to set variables.
if [[ -z "$QUERY_STRING" ]]; then
 QUERY_STRING="$SAMPLE_INPUTS"
fi
eval "declare ${QUERY_STRING//&/;}"

# Output response header.
cat <<.CGI
Content-type: text/html

.CGI

# Output server errors.
exec 2>&1

# Inputs/results web page header. HTML start.
cat <<.HTML
<html lang="en">
<head>
<meta charset="utf-8" />
<link rel="shortcut icon" href="" />
<link rel="apple-touch-icon" href="" />
<title>Alex Decknadel $TITLE</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link href="../common/css/default.css" rel="stylesheet" type="text/css" />
<link href="https://use.typekit.net/egm1aon.css" rel="stylesheet" type="text/css" />
<script src="../common/js/jquery-3.1.1.min.js" type="text/javascript"></script>
<script src="../common/js/lib.js" type="text/javascript"></script>
</head>
<body>
<header class="outerwrap">
<div class="innerwrap">
<h1><a href="/"><span>$TITLE</span></a></h1>
<nav id="primary">
<ul>
<li><a href="..">Home</a></li>
<li><a href="..#about">About</a></li>
<li><a href="#contact">Contact</a></li>
</ul>
</nav>
</div>
</header>
.HTML
#HTML end

# Transforms spaces in previous input. Create and change variable payType.
payType=${payType//+/ }

# Prompt for inputs. HTML start
cat <<.HTML
<main>
<article>
<div class="outerwrap" id="customer">
<section class="innerwrap" id="form">
<h3>Customer Information</h3>
<div>
<p>You must enter a value in the form to get results.</p>
<form>
<table>
<tr><td>First Name: <td><input name="firstName" value="$firstName">
<tr><td>Last Name: <td><input name="lastName" value="$lastName">
<tr><td>Payment Type: <td><input name="payType" value="$payType">
<tr align=CENTER><td colspan=2><input type="submit" value="Search">
</table>
</form>
</div>
.HTML
#HTML end

# Output Header. Nested if... else statement.
if [[ -z "$firstName" ]]; then
	if [[ -z "$lastName" ]]; then
		if [[ -z "$payType" ]]; then
			exit 0
		else
			oHeader="Any payment method that uses $payType:"
		fi
	elif [[ -z "$payType" ]]; then
		oHeader="Any payment type used by anyone with the last name $lastName:"
	else
		oHeader="All $payType used by anyone with the last name $lastName:"
	fi
elif [[ -z "$lastName" ]]; then
	if [[ -z "$payType" ]]; then
		oHeader="Any payment type used by anyone named $firstName:"
	else
		oHeader="All $payType used by anyone named $firstName:"
	fi
elif [[ -z "$payType" ]]; then
	oHeader="Any payment type used by $firstName $lastName:"
else
	oHeader="Any $payType used by $firstName $lastName:"
fi
#End if... else statement.

# Extract records. Basic linux commands cat, grep, and awk.
results=$(
cat /home/ubuntu/IS240/prescription_data.csv |
	grep -i "$firstName" |
	grep -i "$lastName" |
	grep -i "$payType" |
awk -F, '{ print "<tr><td>", $5, "<td>", $2 }'
)

#Output results. More HTML.
cat <<.HTML
<div>
<h4>$oHeader</h4>
<table border>
<tr><th>Customer <th>Payment Type
$results
</table>
</div>
</section>
</div>
</article>
</main>
<footer class="outerwrap">
<div class="innerwrap">
<section id="contact">
<p>Alex Decknadel</p>
<p><em>adecknadel19@mail.wou.edu</em></p>
</section>
</div>
</footer>
</body>
</html>
.HTML
#HTML end.