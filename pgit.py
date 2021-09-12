"""Fills out git username and token recovered from Bitwarden CLI.
User is prompted for Bitwarden master password. Locks session immediately after recovering token.
Use "bw list items --pretty" to find the Bitwarden item ID for the github token.

Usage
-----
pgit pull
pgit push
"""

if __name__ == '__main__':
	import subprocess as sb
	import sys, json

	git_token_id = "TOKEN_BITWARDEN_ITEM_ID"
	if sys.argv[1] == '-h' or sys.argv[1] == '--help':
			print(__doc__)
			quit()
	elif sys.argv[1] == "push":
		cmd = "git push"
	elif sys.argv[1] == "pull":
		cmd = "git pull"
	else:
		raise ValueError("Invalid argument")
		
	try:
		result = sb.run(["bw", "get", "item", git_token_id], stdout=sb.PIPE)
		sb.run(["bw", "lock"])
		
		item_str = result.stdout.decode('utf-8')
		item_dict = json.loads(item_str)
		token = item_dict["login"]["password"]
		
		sb.run(["pull-push.exp", cmd, token])
	except:
		pass
	
	
