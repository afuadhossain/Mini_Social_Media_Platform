#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    printf("Content-Type:text/html\n\n");

    char buffer[100];
    fgets(buffer,99,stdin);
    char username[21];
    sscanf(buffer,"username=%s",username);
    FILE *fp;
    char line[100];

    printf("<html><head><title>See Friends</title>");
    printf("<link rel=\"stylesheet\" type=\"text/css\" href=\"../ass4/style.css\">"
    "</head>"
    "<body>"
    "<div id=\'cssmenu\'>"
    "<ul>"
      "<li>"
        "<form action=\"http://cs.mcgill.ca/~mrosen51/ass4/dashboard.py\" method=\"post\">"
          "<a href=\"javascript:;\" onclick=\"parentNode.submit();\">Dashboard</a>"
          "<input type=\"hidden\" name=\"username\" value=\"%s\">"
        "</form>"
      "</li>"
      "<li>"
        "<form action=\"http://cs.mcgill.ca/~hlee168/cgi-bin/makefriends.py\" method=\"post\">"
          "<a href=\"javascript:;\" onclick=\"parentNode.submit();\">Add friends</a>"
          "<input type=\"hidden\" name=\"username\" value=\"%s\">"
        "</form>"
      "</li>"
      "<li>"
        "<form action=\"http://cs.mcgill.ca/~hlee168/cgi-bin/seefriends.cgi\" method=\"post\">"
          "<a href=\"javascript:;\" onclick=\"parentNode.submit();\">See Friends</a>"
          "<input type=\"hidden\" name=\"username\" value=\"%s\">"
        "</form>"
      "</li>"
        "<li>"
          "<form>"
            "<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/welcome.html\">Logout</a>"
          "</form>"
        "</li>"
    "</ul>"
    "</div>"

    "<hr>",username,username,username);

    fp = fopen("../ass4/friends.txt", "rt");
    if(fp == NULL) printf("Oops, something went wrong. We can't find your friends list...");
    else {
        printf("<form action=\"./loadprofile.py\" method=\"get\">");
        while(fgets(line,99,fp)) {
            char *p = line;
            char usernamebuffer[21];
            int i = 0;
            while(*p!=' ' && *p!='\0' && *p!='\n') {
                usernamebuffer[i] = *p;
                i++;
                p++;
            }
            usernamebuffer[i] = '\0';
            if(strcmp(usernamebuffer,username)==0) {
                char *copy = strdup(line);
                char *friend = strtok(copy," ");
                while(friend!=NULL) {
                    char *newline = strchr(friend,'\n');
                    if(newline) *newline = 0;
                    printf("<input type=\"radio\" name=\"friend\" value=\"%s\">%s<br>",friend,friend);
                    friend = strtok(NULL," ");
                }
                break;
            }
        }
        printf("<input type=\"hidden\" name=\"username\" value=\"%s\">",username);
        printf("<input type=\"submit\" value=\"See profile\">");
        printf("</form>");
    }
    fclose(fp);
    printf("</body></html>");
    return 0;
}
