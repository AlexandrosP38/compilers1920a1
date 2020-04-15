"""
Κώδικας που θα χρησιμοποιηθεί ως βάση για την 1η εργασία
των Μεταγλωττιστών (αναγνώριση κειμένου μέσω αυτομάτου DFA).

ΠΡΟΣΟΧΗ: Προσθήκες στον κώδικα επιτρέπονται μόνο
στα σημεία (Α), (Β) και (Γ) - διαβάστε τα σχόλια!
"""



transitions = {'s0':{'0':'s1', '1':'s1', '2':'s1', '3':'s1','4':'s1','5':'s1','6':'s1','7':'s1','8':'s1','9':'s1', '.':'s4'} ,
               's1':{'0':'s1', '1':'s1', '2':'s1', '3':'s1','4':'s1','5':'s1','6':'s1','7':'s1','8':'s1','9':'s1','.':'s2'},
               's2':{'0':'s3', '1':'s3', '2':'s3', '3':'s3','4':'s3','5':'s3','6':'s3','7':'s3','8':'s3','9':'s3'},
               's3':{'0':'s3', '1':'s3', '2':'s3', '3':'s3','4':'s3','5':'s3','6':'s3','7':'s3','8':'s3','9':'s3'},
               's4':{'0':'s5', '1':'s5', '2':'s5', '3':'s5','4':'s5','5':'s5','6':'s5','7':'s5','8':'s5','9':'s5'},
               's5':{'0':'s5', '1':'s5', '2':'s5', '3':'s5','4':'s5','5':'s5','6':'s5','7':'s5','8':'s5','9':'s5'} 

     	      } 


accepts = { 's2':'FLOAT_TOKEN',
	    's3':'FLOAT_TOKEN',
	    's5':'FLOAT_TOKEN'
	
     	  }

def get_char(text,pos):
	""" Returns char (or char category) at position `pos` of `text`,
	or None if out of bounds. """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# (Γ) Προαιρετικά, μπορείτε να ομαδοποιήσετε τους
	# χαρακτήρες εισόδου εδώ.
	# Για λεπτομέρειες δείτε στο:
	# http://mixstef.github.io/courses/compilers/lecturedoc/unit1/module1.html#id11
	
	return c
	

# Δεν επιτρέπεται η παρέμβαση στον κώδικα από αυτό το σημείο και κάτω! 

def scan(text,transitions,accepts,state):
	""" Starting from inital `state`, scans `text` while transitions
	exist in `transitions` dict. After that, if on a state belonging to
	`accepts` dict, returns the corresponding token object, else None.
	"""
	
	# initial position on text
	pos = 0
	
	# memory object for last seen accepting state
	matched = None
	
	while True:
		
		c = get_char(text,pos)	# get next char (or char category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char			

			# remember if current state is accepting
			if state in accepts:
				matched = { 'token':  accepts[state],
					    'lexeme': text[:pos] }
			
		else:	# no transition found, return last match or None
			return matched
			

# testing inputs
for test in ['12.456','6789.','.66998','1234','.']:
	m = scan(test,transitions,accepts,'s0')
	print("Testing '{}'\nResult: {}\n".format(test,m))


