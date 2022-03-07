import re

import binascii

data = """<HtmL>
<heaD>
	<MEta charset="utf-8">
	<MEta http-equiv="X-UA-Compatible" content="IE=edge">
	<Meta name="viewport" content="width=device-width, initial-scale=1.0">

	<lINK rel="shortcut icon" href="img/favicon.ico"> 
	<LiNk rel="stylesheet" href="css/vendor/fluidbox.min.css">
	<LiNK rel="stylesheet" href="css/main.css">

	<TiTlE>🐱 </TitLe>

</heAd>
<BODY>


	<heADer>

		<Div id="logo-container">
			<dIV id="logo"><A href="/">🐱 Top Secret Website 🐱 </A></DiV>
			<DiV id="subtitle">Cats only are authorized</DiV>
		</div>
		<NAv>
			<uL>
				<lI><a href="#">Link 1</A></lI>
				<LI><a href="#">Link 2</a></Li>
				<LI><A href="#">Link 3</A></Li> 
				<lI><A href="mailto:your@address.com" class="bordered">Contact</a></lI>
			</uL>
		</Nav> 

	</HEADer>

	<DiV id="content">

		<SEctiON class="intro">
			<h1>Hello, <sPan class="nl"></sPaN>kitty !</H1>
			<P>
StEg4n0gr4ph1e, The first recorded use of the term was in 1499 by Johannes Trithemius in his Steganographia, a treatise on cryptography and steganography, disguised as a book on magic. Generally, the hidden messages appear to be (or be part of) something else: images, articles, shopping lists, or some other cover text. For example, the hidden message may be in invisible ink between the visible lines of a private letter. Some implementations of steganography that lack a shared secret are forms of security through obscurity, and key-dependent steganographic schemes adhere to Kerckhoffs's principle.
			</P>
		</SECTION>

		<SECTION class="row">
			<DIV class="col-full">
				<H2>You can stop now :)</H2>"""
# regex html tags in data
tags = re.findall(r'<[^>]+>', data)
res = ""
for tag in tags:
	# get tag name
	tag_name = re.findall(r'<([^>]+)>', tag)
	
	# remove tag atributes
	tag_name = tag_name[0].split(' ')[0]
	# remove both kind of slashes
	tag_name = tag_name.replace('/', '').replace('\\', '')
	# regex get ony alphabetic characters
	tag_name = re.findall(r'[a-zA-Z]+', tag_name)
	# print(tag_name)
	res+=tag_name[0]	if tag_name else ""
result = ""
print(res)
for letter in res:
	result = result+ "1" if letter.islower() else result+"0"
print(result)
#regex add spaces between 8 characters
result = re.sub(r'.{8}', r'\g<0> ', result)
# convert bytes to strins
output = ""
result = result.split(' ')
for byte in result:
	output += chr(int(byte,2))

print(output)