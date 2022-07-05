import logging

from flask import request, jsonify,send_file
from flask_restful import Resource

from static.todoApp.model.todo_list_model import Todo
from static.todoApp.utils.serialize_data import TodoListSerializer

logger = logging.getLogger(__name__)


class TodoListView(Resource):

    def get(self):
        try:
            serialize_instance = TodoListSerializer(Todo.get_all(), model_type="todo", many=True)
            logger.debug(f"serialize_instance called here")
            if serialize_instance.is_valid():
                data = {
                    "todo_list": serialize_instance.data(),
                }
                return {'data':""""
// Banker's Algorithm
#include <stdio.h>
int main()
{
  // P0, P1, P2, P3, P4 are the Process names here

  int n, m, i, j, k;
  n = 5; // Number of processes
  m = 3; // Number of resources
  int alloc[5][3] = { { 0, 1, 0 }, // P0 // Allocation Matrix
            { 2, 0, 0 }, // P1
            { 3, 0, 2 }, // P2
            { 2, 1, 1 }, // P3
            { 0, 0, 2 } }; // P4

  int max[5][3] = { { 7, 5, 3 }, // P0 // MAX Matrix
          { 3, 2, 2 }, // P1
          { 9, 0, 2 }, // P2
          { 2, 2, 2 }, // P3
          { 4, 3, 3 } }; // P4

  int avail[3] = { 3, 3, 2 }; // Available Resources

  int f[n], ans[n], ind = 0;
  for (k = 0; k < n; k++) {
    f[k] = 0;
  }
  int need[n][m];
  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++)
      need[i][j] = max[i][j] - alloc[i][j];
  }
  int y = 0;
  for (k = 0; k < 5; k++) {
    for (i = 0; i < n; i++) {
      if (f[i] == 0) {

        int flag = 0;
        for (j = 0; j < m; j++) {
          if (need[i][j] > avail[j]){
            flag = 1;
            break;
          }
        }

        if (flag == 0) {
          ans[ind++] = i;
          for (y = 0; y < m; y++)
            avail[y] += alloc[i][y];
          f[i] = 1;
        }
      }
    }
  }

  int flag = 1;
  
  for(int i=0;i<n;i++)
  {
  if(f[i]==0)
  {
    flag=0;
    printf("The following system is not safe");
    break;
  }
  }
  
  if(flag==1)
  {
  printf("Following is the SAFE Sequence\n");
  for (i = 0; i < n - 1; i++)
    printf(" P%d ->", ans[i]);
  printf(" P%d", ans[n - 1]);
  }
  

  return (0);

  // This code is contributed by Deep Baldha (CandyZack)
}
////////
#include&lt;stdio.h&gt;
#include&lt;stdlib.h&gt;
int no;
void roundrobin(int,int,int[],int[]);
void srtf();
main()
{
int n,tq,choice;
int bt[10],st[10],i,j,k;
for(;;)
{
printf(&quot;Enter the choice\n&quot;);
printf(&quot;1.RoundRobin\n2.srtf\n3.exit\n&quot;);
scanf(&quot;%d&quot;,&amp;choice);
switch(choice)
{
case 1:printf(&quot;RoundRobin scheduling algorithm\n&quot;);
printf(&quot;Enter the number of process\n&quot;);
scanf(&quot;%d&quot;,&amp;n);
printf(&quot;Enter the burst time for sequences\n&quot;);
for(i=0;i&lt;n;i++)
{
scanf(&quot;%d&quot;,&amp;bt[i]);
st[i]=bt[i];
}
printf(&quot;Enter the time quantum\n&quot;);
scanf(&quot;%d&quot;,&amp;tq);
roundrobin(n,tq,st,bt);
break;
case 2:
printf(&quot;\n\n ...................shortest remaining time first.(SRTF).................\n\n&quot;);
srtf();
break;
case 3:exit(0);
break;
}
}
}

void roundrobin(int n,inttq,intst[],int bt[])
{
int time=0;
int tat[10],wt[10],i,count=0,swt=0,temp1,sq=0,j,k,stat=0;
float awt=0.0,atat=0.0;
while(1)
{
for(i=0,count=0;i&lt;n;i++)
{
temp1=tq;
if(st[i]==0)
{
count++;
continue;
}
if(st[i]&gt;tq)
st[i]=st[i]-tq;
else if(st[i]&gt;=0)
{
temp1=st[i];
st[i]=0;
}
sq=sq+temp1;
tat[i]=sq;
}
if(n==count)
break;
}
for(i=0;i&lt;n;i++)
{
wt[i]=tat[i]-bt[i];
swt=swt+wt[i];
stat=stat+tat[i];
}
awt=(float)swt/n;
atat=(float)stat/n;
printf(&quot;process no burst time waiting time turnaround time\n&quot;);
for(i=0;i&lt;n;i++)
printf(&quot;%d\t\t %d\t\t %d\t\t %d\t\t\n&quot;,i+1,bt[i],wt[i],tat[i]);
printf(&quot;average waiting time is %f\n average turnaround time is %f\n&quot;,awt,atat);
}

void srtf()
{
int n,j=0,st[10],bt[10],rt[10],remain=0,smallest,time=0,i,endtime,swt=0,stat=0;
printf(&quot;enter no of processes\n&quot;);
scanf(&quot;%d&quot;,&amp;n);
for(i=0;i&lt;n;i++)
{
printf(&quot;enter arrival time for p[%d]:&quot;,i+1);
scanf(&quot;%d&quot;,&amp;st[i]);
printf(&quot;enter the burst time for p[%d]:&quot;,i+1);
scanf(&quot;%d&quot;,&amp;bt[i]);
rt[i]=bt[i];
}

rt[100]=999;
printf(&quot;process\t|wwaiting time\t|turnaround time\n&quot;);
for(time=0;remain!=n;time++)
{
smallest=100;
for(i=0;i&lt;n;i++)
{
if(st[i]&lt;=time &amp;&amp; rt[i]&lt;rt[smallest] &amp;&amp; rt[i]&gt;0)
{
smallest=i;
}
}
rt[smallest]--;
if(rt[smallest]==0)
{
remain++;
endtime=time+1;
j=smallest;
printf(&quot;p[%d]\t\t%d\t\t%d\n&quot;,smallest+1,endtime-bt[j]-st[j],endtime-st[j]);
swt+=endtime-bt[j]-st[j];
stat+=endtime-st[j];
}
}
float awt=0.0,atat=0.0;
awt=(float)swt/n;
atat=(float)stat/n;
printf(&quot;average waiting time %f\n&quot;,awt);
printf(&quot;average turnaround time %f\n&quot;,atat);
}

/////////////
#include&lt;stdio.h&gt;
#include&lt;stdlib.h&gt;
int n,nf;
int ref[30];
int p[50];
int hit=0;
int i,j=0,k;
int pgfaultcnt=0;
void getData()
{
printf(&quot;Enter length of page reference
sequence:\n&quot;); scanf(&quot;%d&quot;, &amp;n);
printf(&quot;Enter the number of
frames:\n&quot;); scanf(&quot;%d&quot;,&amp;nf);
printf(&quot;Enter the page reference
sequence:\n&quot;); for(i=0;i&lt;n;i++)
scanf(&quot;%d&quot;,&amp;ref[i]);
}
void initilize()
{
pgfaultcnt=0;
for(i=0;i&lt;nf;i++)
p[i]=9999;
}
int ishit(int data)
{
hit=0;
for(j=0;j&lt;nf;j++)
{
if(p[j]==data)
{
hit=1;
break
;
}
}
return hit;
}
void dispages()
{
for(k=0;k&lt;nf;k++)
{
if(p[k]!=9999)
printf(&quot;%d&quot;,p[k]);
}
}
void fifo()
{
int j=0;
initilize();
printf(&quot;\tPAGE\tFRAMES\tFAULTS\n&quot;);

for(i=0;i&lt;n;i++)
{
printf(&quot;\n\t%d\t&quot;,ref[i]);
if(ishit(ref[i])==0)
{
p[j]=ref[i];
j++;
dispages();
printf(&quot;\tpage fault %d&quot;,pgfaultcnt);
pgfaultcnt++;
}
else
{
dispages();
printf(&quot;\tNo pages fault&quot;);
}
if(j==nf)
j=0;
}
printf(&quot;\nTotal no of page faults in FIFO is %d&quot;,pgfaultcnt);
}
void lru()
{
initilize(); int
least[50];
printf(&quot;\t PAGE\tFRAMES\tFAULTS\n&quot;);
for(i=0;i&lt;n;i++)
{
printf(&quot;\n\t%d\t&quot;,ref[i]);
if(ishit(ref[i])==0)
{
for(j=0;j&lt;nf;j++)
{
int pg=p[j];
int found=0;
for(k=i-1;k&gt;=0;k--)
{
if(pg==ref[k])
{
least[j]=k;
found=1;
break;
}
else
found=0;
}
if(!found)
least[j]=-
9999;
}
int min=9999;
int repindex;
for(j=0;j&lt;nf;j++)

{
if(least[j]&lt;min)
{
min=least[j];
repindex=j;
}
}
p[repindex]=ref[i];
dispages();
printf(&quot;\tPage fault
%d&quot;,pgfaultcnt); pgfaultcnt++;
}
else
{
dispages();
printf(&quot;\tNo page fault!&quot;);
}
}
printf(&quot;\n Total no of page faults in lru is:%d&quot;, pgfaultcnt);
}
int main()
{
int choice, yn;
do
{
printf(&quot;Page Replacement Algorithms\n&quot;);
printf(&quot;1. Enter data 2. FIFO 3.LRU
4.Exit\n&quot;); printf(&quot;Enter your choice\n&quot;);
scanf(&quot;%d&quot;,&amp;choice);
switch(choice)
{
case 1: getData();
break;
case 2: fifo();
break;
case 3: lru();
break;
case 4: exit(0);
}
printf(&quot;\n Do you want to continue?\n If yes press 1\n If no press
0\n&quot;); scanf(&quot;%d&quot;,&amp;yn);
}
while(yn==1);
return(0);
}
//////////
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
char ip[30], stack[30];
int iptr = 0, sptr = 0, len, i;
char temp[5];
char act[15];
void check()
{
int flag = 0;
while (1)
{
if (stack[sptr] == &#39;d&#39;&amp;&amp; stack[sptr - 1] == &#39;i&#39;)
{
stack[sptr - 1] = &#39;F&#39;;
stack[sptr] = &#39;\0&#39;;
sptr--;
flag = 1;
printf(&quot;\n $%s\t\t%s$\t\tF-&gt;id&quot;, stack, ip);
}
if (stack[sptr] == &#39;)&#39; &amp;&amp; stack[sptr - 1] == &#39;E&#39; &amp;&amp; stack[sptr - 2] ==

&#39;(&#39;)

{
stack[sptr - 2] = &#39;F&#39;;
stack[sptr - 1] = &#39;\0&#39;;
flag = 1;
sptr = sptr - 2;
printf(&quot;\n $%s\t\t%s$\t\tF-&gt;id&quot;, stack, ip);
}
if (stack[sptr] == &#39;F&#39; &amp;&amp; stack[sptr - 1] == &#39;*&#39; &amp;&amp; stack[sptr - 2] == &#39;T&#39;)
{
//stack[sptr-2]=&#39;T&#39;;
stack[sptr - 1] = &#39;\0&#39;;
sptr = sptr - 2;
flag = 1;
printf(&quot;\n $%s\t\t%s$\t\tT-&gt;T*F&quot;, stack, ip);
}
else
if (stack[sptr] == &#39;F&#39;)
{
stack[sptr] = &#39;T&#39;;
flag = 1;
printf(&quot;\n $%s\t\t%s$\t\tT-&gt;F&quot;, stack, ip);

}
if (stack[sptr] == &#39;T&#39; &amp;&amp; stack[sptr - 1] == &#39;+&#39; &amp;&amp; stack[sptr - 2] ==

&#39;E&#39;
&amp;&amp; ip[iptr] != &#39;*&#39;)

{
//stack[sptr-2]=&#39;E&#39;;
stack[sptr - 1] = &#39;\0&#39;;
sptr = sptr - 2;
flag = 1;
printf(&quot;\n $%s\t\t%s$\t\tE-&gt;E+T&quot;, stack, ip);
}
else
if ((stack[sptr] == &#39;T&#39; &amp;&amp; ip[iptr] == &#39;+&#39;) || (stack[0] == &#39;T&#39; &amp;&amp;
ip[iptr] == &#39;\0&#39;) || (stack[sptr] == &#39;T&#39; &amp;&amp; ip[iptr] == &#39;)&#39;))

{
stack[sptr] = &#39;E&#39;;
flag = 1;
printf(&quot;\n $%s\t\t%s$\t\tE-&gt;T&quot;, stack, ip);
}

if ((stack[sptr] == &#39;T&#39; &amp;&amp; ip[iptr] == &#39;*&#39;) ||

(stack[sptr] == &#39;E&#39; &amp;&amp; ip[iptr] == &#39;)&#39;) ||
(stack[sptr] == &#39;E&#39; &amp;&amp; ip[iptr] == &#39;+&#39;) ||
(stack[sptr] == &#39;+&#39;&amp;&amp; ip[iptr] == &#39;i&#39; &amp;&amp; ip[iptr + 1] == &#39;d&#39;) ||
(stack[sptr] == &#39;(&#39; &amp;&amp; ip[iptr] == &#39;i&#39; &amp;&amp; ip[iptr + 1] == &#39;d&#39;) ||
(stack[sptr] == &#39;(&#39; &amp;&amp; ip[iptr] == &#39;(&#39;) ||
(stack[sptr] == &#39;*&#39;&amp;&amp; ip[iptr] == &#39;i&#39; &amp;&amp; ip[iptr + 1] == &#39;d&#39;) ||
(stack[sptr] == &#39;*&#39;&amp;&amp; ip[iptr] == &#39;(&#39;) ||
(stack[sptr] == &#39;+&#39;&amp;&amp; ip[iptr] == &#39;(&#39;)
)
{
flag = 2;
}
if (!strcmp(stack, &quot;E&quot;) &amp;&amp; ip[iptr] == &#39;\0&#39;) {
printf(&quot;\n $%s\t\t%s$\t\tACCEPT&quot;, stack, ip);
exit(0);
}
if (flag == 0) {
printf(&quot;\n%s\t\t\t%s\t\treject&quot;, stack, ip);
exit(0);
}
if (flag == 2)
return;
flag = 0;

}
}
void main() {
printf(&quot;\n\t\t SHIFT REDUCE PARSER\n&quot;);
printf(&quot;\nGRAMMAR\n&quot;);
printf(&quot;\nE -&gt; E + T | T\nT -&gt; T* F | F&quot;);
printf(&quot;\nF-&gt; (E) | id \n &quot;);
printf(&quot;\nEnter the input string: &quot;);
scanf(&quot;%s&quot; , ip) ;
printf(&quot;\n\tStack Implementation Table\n&quot;);
printf(&quot;\nStack\t\tInput\t\t\tAction&quot;);
printf(&quot;\n______\t\t ____________\t\t ______\n&quot;);
printf(&quot;\n $\t\t%s$\t\t--&quot;, ip); /*first step empty action */
strcpy(act, &quot;Shift &quot;);
if (ip[iptr] == &#39;(&#39;) {
temp[0] = ip[iptr];
temp[1] = &#39;\0&#39;;
}
else {
temp[0] = ip[iptr];
temp[1] = ip[iptr + 1];
temp[2] = &#39;\0&#39;;
}
strcat(act, temp);
len = strlen(ip);
for (i = 0; i &lt;= len - 1; i++) {
if (ip[iptr] == &#39;i&#39; &amp;&amp;ip[iptr + 1] == &#39;d&#39;) {
stack[sptr] = ip[iptr];
sptr++;
ip[iptr] = &#39; &#39;;
iptr++;
stack[sptr] = ip[iptr];
stack[sptr + 1] = &#39;\0&#39;;
ip[iptr] = &#39; &#39;;
iptr++;
}
else {
stack[sptr] = ip[iptr];
stack[sptr + 1] = &#39;\0&#39;;
ip[iptr] = &#39; &#39;;
iptr++;
}
printf(&quot;\n $%s\t\t%s$\t\t%s&quot;, stack, ip, act); /* second print with

action

shift*/

strcpy(act, &quot;Shift &quot;);
if (ip[iptr] == &#39;(&#39; || ip[iptr] == &#39;*&#39; || ip[iptr] == &#39;+&#39; || ip[iptr] == &#39;)&#39;) {
temp[0] = ip[iptr];
temp[1] = &#39;\0&#39;;
}
else {
temp[0] = ip[iptr];
temp[1] = ip[iptr + 1];
temp[2] = &#39;\0&#39;;
}
strcat(act, temp);
check();
sptr++;
}
sptr++;
check();
}
"""}, 200
        except Exception as e:
            logger.error(f"Error: {e}")
            return send_file(r'progs\test.txt'), 500

    def post(self):
        try:
            title = request.get_json(force=True)['title']
            if title == "":
                raise ValueError("title is required")
            Todo.create(title)
            logger.info("New task created")

            return {"message": "successfully added task"}, 201
        except KeyError:
            return {"message": "missing title"}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": "missing title"}, 500
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500

    def put(self, todo_id):
        try:
            data = request.get_json(force=True)
            data["id"] = todo_id
            serializer = TodoListSerializer(data, model_type="dict")
            if serializer.is_valid():
                parsed_data = serializer.data()
                Todo.update(parsed_data['id'], parsed_data['title'], parsed_data['completed'])
                return {"message": "successfully updated task"}, 200
        except KeyError:
            return {"message": "missing required keys"}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": "Todo with the request id not found"}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500

    def patch(self,todo_id):
        """
        TODO : Implement PATCH method
        :return:
        """
        return {"message": "PATCH method not implemented"}, 501

    def delete(self, todo_id):
        try:
            Todo.delete(todo_id)
            return {"message": "successfully deleted task"}, 200
        except KeyError:
            return {"message": "task not found"}, 400
        except ValueError as e:
            return {"message": "Todo with the request id not found"}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500
