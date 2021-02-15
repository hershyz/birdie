<img src="https://raw.githubusercontent.com/hershyz/birdie/main/birdie.png">
<h3>Mass E-mailing solution for event planners.</h3>
<h4>Download, unzip, and run <a href="https://github.com/hershyz/birdie/releases/tag/rel0.1">here</a>.</h4>

<br>

<p>Commands:</p>
<pre>
help []:                 shows all commands
store [address, name]:   stores sponsors/members
sendall []:              sends email template to all recipients
send [name]:             sends email template to a specific recipient
bcc []:                  sends a bcc email to all participants in the store file
</pre>

<br>

<p>Settings:</p>
<pre>
The local settings.ini file has the following configurations:
email:     [sender email address]
password:  [password for sender email address]
subject:   [subject for all emails sent]
tag:       [tag for name replacement]
</pre>

<br>

<p>Tags:</p>
<pre>
By default, the tag in the settings.ini file is set to <strong>sponsor</strong>,
meaning that typing <sponsor> in the template email will replace it with the name of the recipient.
<br>
If template.txt looks like this:
Hello &ltsponsor&gt,
Goodbye &ltsponsor&gt.
<br>
The output of running <strong>python birdiecli.py send ExampleMember</strong> would be:
Hello ExampleMember,
Goodbye ExampleMember.
</pre>

<p>Running:</p>
<code>python birdiecli.py [+args]</code>
