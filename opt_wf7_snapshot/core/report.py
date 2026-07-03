

import json
import os


def html(data):

    path="/opt/wf/reports/html/report.html"


    page=f"""

<html>

<head>

<title>WF Security Report</title>

<style>

body {{
background:#111;
color:#0f0;
font-family:monospace;
padding:30px;
}}

.card {{

border:1px solid #0f0;
padding:20px;

}}

</style>

</head>


<body>


<h1>WF Security Framework</h1>


<div class="card">

<pre>

{json.dumps(data,indent=4)}

</pre>


</div>


</body>

</html>

"""


    with open(path,"w") as f:

        f.write(page)



    return path



